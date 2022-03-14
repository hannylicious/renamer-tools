"Module for dealing with renaming images / PDFs"
import argparse
from datetime import datetime
from pathlib import Path
import logging
import os
import pdb

from models import PngImage


def setup_logger(name, log_file, level=logging.INFO):
    """
    This setups a new logger - giving us the ability to log to various files

    Args:
        name (_type_): _description_
        log_file (_type_): _description_
        level (_type_, optional): _description_. Defaults to logging.INFO.
    """
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger


png_logger = setup_logger("png_logger", datetime.now().strftime("png_%d_%m_%Y.log"))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d" "--directory", help="The directory to rename images within"
    )
    args = parser.parse_args()
    return args


def main(args=None):
    # TODO: Setup ability to specify other directories
    # TODO: Setup ability to keep original copies in place
    # TODO: Setup ability to specify file extensions
    # For now we specify the directory explicitly
    working_directory = "."
    if args.directory:
        working_path = Path(args.directory)
        if working_path.is_dir():
            working_directory = working_path
        else:
            exit(f"{args.directory} did not exist!")
    # set the directory for new images
    new_image_directory = Path(working_directory, "renamed_images")
    # Check that the renamed_images directory exists
    if not new_image_directory.is_dir():
        os.mkdir(new_image_directory)
    # get all the pngs in directory

    pngs = Path(working_directory).glob("*.png")
    for png_path in pngs:
        png_image = PngImage(png_path)
        png_image.save(new_image_directory, file_extension=".TIFF")


if __name__ == "__main__":
    main()
