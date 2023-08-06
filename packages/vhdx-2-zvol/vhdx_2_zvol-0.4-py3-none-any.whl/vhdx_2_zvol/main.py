import argparse
import logging
import os
import shutil
import subprocess

# Logging configuration
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def try_except(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return False

    return wrapper


def parse_args():
    import sys

    script_name = sys.argv[0]
    parser = argparse.ArgumentParser(
        description="Convert Hyper-V VHDX files to QCOW2 format and further convert"
        + " QCOW2 files to ZVOL datasets in a specified ZFS pool."
    )

    # Required arguments
    parser.add_argument("vhdx_path", type=str, help="Path to the Hyper-V VHDX file")
    parser.add_argument("qcow2_path", type=str, help="Path to the QCOW2 file")

    # Optional arguments
    parser.add_argument(
        "--zpool",
        type=str,
        default="zpool",
        help='Name of the ZFS pool (default: "zpool")',
    )
    parser.add_argument(
        "--zvol",
        type=str,
        default="zvol",
        help='Name of the ZVOL dataset (default: "zvol")',
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    parser.add_argument(
        "-r", "--dry-run", action="store_true", default=True, help="Enable dry run mode"
    )
    parser.add_argument(
        "-w", "--disable-dry-run", action="store_true", help="Disable dry run mode"
    )

    args = parser.parse_args()

    # Check if required arguments are provided
    if not args.vhdx_path or not args.qcow2_path:
        input_values = f"vhdx_path='{args.vhdx_path}', qcow2_path='{args.qcow2_path}'"
        cmd = f"python {script_name}"
        req = f"--vhdx_path {args.vhdx_path} --qcow2_path {args.qcow2_path}"
        if args.zpool:
            input_values += f", zpool='{args.zpool}'"
            cmd += f", --zpool='{args.zpool}'"
        if args.zvol:
            input_values += f", zvol='{args.zvol}'"
            cmd += f" --zvol='{args.zvol}'"
        if args.debug:
            input_values += f", debug='{args.debug}'"
            cmd += " --debug"
        if args.dry_run:
            input_values += f", dry_run='{args.dry_run}'"
            cmd += " -r"
        if args.disable_dry_run:
            input_values += f", disable-dry_run='{args.dry_run}'"
            cmd += " -w"
        msg = (
            "The following arguments are required: vhdx_path, qcow2_path."
            + f" Provided input values: {input_values}. Please provide the "
            + f"required input values.\n\nExample usage: {cmd} {req}"
        )
        print(msg)
        parser.error(msg)

    if args.dry_run == args.disable_dry_run:
        args.dry_run = not args.disable_dry_run
    return args


def setup_logging(debug):
    """Configure logging based on debug flag."""
    if debug:
        logging.basicConfig(
            format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG
        )
    else:
        logging.basicConfig(
            format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
        )


@try_except
def convert_vhdx_to_qcow2(vhdx_path, qcow2_path):
    """
    Converts a Hyper-V VHDX file to QCOW2 format using qemu-img command.

    Args:
        vhdx_path (str): Path to the input VHDX file.
        qcow2_path (str): Path to the output QCOW2 file.

    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    if not shutil.which("qemu-img"):
        logging.error(
            "qemu-img command not found in os PATH. Please ensure that the qemu-img"
            + " command is installed and available in the PATH."
        )
        return False
    try:
        # Execute qemu-img command to convert VHDX to QCOW2
        subprocess.run(
            ["qemu-img", "convert", "-f", "vhdx", "-O", "qcow2", vhdx_path, qcow2_path],
            check=True,
        )
        logging.info(
            f"Successfully converted VHDX to QCOW2: {vhdx_path} -> {qcow2_path}"
        )
        return True
    except subprocess.CalledProcessError as e:
        logging.error(
            f"Failed to convert VHDX to QCOW2: {vhdx_path} -> {qcow2_path}. Error: {e}"
        )
        return False


@try_except
def convert_qcow2_to_zvol(qcow2_path, zpool, zvol):
    """
    Convert QCOW2 file to ZVOL dataset in a specified ZFS pool.

    Args:
        qcow2_path (str): Path to the QCOW2 file.
        zpool (str): Name of the ZFS pool.
        zvol (str): Name of the ZVOL dataset.

    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    logging.info(
        f"Converting QCOW2 file '{qcow2_path}' to ZVOL dataset '{zpool}/{zvol}'"
    )

    # Check if zvol command is present in the os PATH
    if not shutil.which("zfs"):
        logging.error(
            "zvol command not found in os PATH. Please ensure that the zvol"
            + " command is installed and available in the PATH."
        )
        return False

    # Construct the zvol command
    zvol_cmd = f"zfs create {zpool}/{zvol} {qcow2_path}"

    # Run the zvol command
    try:
        subprocess.run(zvol_cmd, shell=True, check=True)
        logging.info("ZVOL conversion successful.")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to convert QCOW2 to ZVOL: {e}")
        return False


@try_except
def remove_file(file_path):
    """
    Removes a file from the file system.

    Args:
        file_path (str): Path to the file to be removed.

    Returns:
        bool: True if file removal is successful, False otherwise.
    """
    try:
        # Remove the file using os.remove()
        os.remove(file_path)
        logging.info(f"Successfully removed file: {file_path}")
        return True
    except OSError as e:
        logging.error(f"Failed to remove file: {file_path}. Error: {e}")
        return False


# Function to parse command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Convert Hyper-V VHDX files to QCOW2 format, and then further"
        + " convert QCOW2 files to ZVOL datasets in a specified ZFS pool."
    )
    parser.add_argument("vhdx_path", type=str, help="Path to the input VHDX file")
    parser.add_argument("qcow2_path", type=str, help="Path to the output QCOW2 file")
    parser.add_argument(
        "zvol_path",
        type=str,
        help="Path to the output ZVOL dataset in the format <zpool>/<zvol>",
    )
    parser.add_argument("zpool", type=str, help="Name of the ZFS pool")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("--dry-run", action="store_true", help="Enable dry run mode")
    return parser.parse_args()


# Main function
def main():
    # Parse command line arguments
    args = parse_arguments()

    # Set up logging
    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Convert VHDX to QCOW2
    if convert_vhdx_to_qcow2(args.vhdx_path, args.qcow2_path):
        # Convert QCOW2 to ZVOL
        if convert_qcow2_to_zvol(args.qcow2_path, args.zpool, args.zvol_path):
            # Remove original files if not in dry run mode
            if not args.dry_run:
                remove_file(args.vhdx_path)
                remove_file(args.qcow2_path)


if __name__ == "__main__":
    main()
