from pathlib import Path
import pdb
import pytest
import shutil


def setup_files(tmpdir):
    pngs = Path.cwd().glob("*.png")
    for png in pngs:
        # copy file to new directory
        shutil.copy(png, tmpdir)
    pdfs = Path.cwd().glob("*.pdf")
    for pdf in pdfs:
        # copy file to new directory
        shutil.copy(pdf, tmpdir)


def test_image_renames_appropriately_on_save(tmpdir):
    setup_files(tmpdir)
