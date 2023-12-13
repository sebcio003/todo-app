import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    with zipfile.ZipFile(pathlib.Path(dest_dir, "compressedby3000.zip"), 'w') as archive:
        for i in filepaths:
            file_name = pathlib.Path(i)
            archive.write(i, arcname=file_name.name)

