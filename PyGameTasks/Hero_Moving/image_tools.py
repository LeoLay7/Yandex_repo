from pygame import image
from pathlib import Path

ROOT = Path(__file__).parent


def load_image(filename, data_path=None):
    if data_path is None:
        data_path = "data"
    file = ROOT.joinpath(data_path, filename)
    if not file.exists():
        print(f"File {file} does not exist!")
        exit(1)
    return image.load(file)