from pathlib import Path
from PIL import Image
import shutil
import os
import pytesseract


class PngImage:
    def __init__(self, image_path):
        image = Image.open(image_path)
        tes_image_string = pytesseract.image_to_string(image)
        lines = tes_image_string.split("\n")
        new_file_tuple = (lines[0].split()[1], lines[0].split()[2], lines[1])
        self.file_name = image_path.name
        self.file_name_without_ext = image_path.stem
        self.image_string = tes_image_string
        self.original_path = image_path
        self.user_first_name = lines[0].split()[1]
        self.user_last_name = lines[0].split()[2]
        self.user_id = lines[1]
        self.new_file_name = "_".join(new_file_tuple)

    def save(self, new_image_directory, keep_og=True, file_extension=None):
        # Set the file extension
        new_file_extension = self.original_path.suffix
        if file_extension:
            new_file_extension = file_extension
        # Create whole new file name
        new_file_name = self.new_file_name + new_file_extension
        exists = Path(new_image_directory, self.new_file_name).exists()
        if exists:
            # Don't do anything - but raise error so user knows!
            raise ValueError(f"This file already exists! {self.new_file_name}")
        if not keep_og:
            # rename file from original location to new one without keeping OG
            os.rename(
                self.original_path,
                Path(new_image_directory, new_file_name),
            )
            # Open image and save (will convert to new extension automatically)
            new_image = Image.open(Path(new_image_directory, new_file_name))
            new_image.save(new_file_name)

        # copy file to new directory
        shutil.copy(self.original_path, new_image_directory)
        # Opening with Image will allow us to save/convert to other formats
        os.rename(
            Path(new_image_directory, self.file_name),
            Path(new_image_directory, new_file_name),
        )
        # Open image and save (will convert to new extension automatically)
        new_image = Image.open(Path(new_image_directory, new_file_name))
        new_image.save(Path(new_image_directory, new_file_name))
