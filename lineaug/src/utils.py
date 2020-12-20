from pathlib import Path
from typing import Union

import numpy as np
from PIL import Image


def get_gt(path: Path, suffix: str) -> Union[Path, None]:
    """Gets ground truth file associated with line image.

    Args:
        path (Path): Path to the line image.
        suffix (str): Suffix for the ground truth text files.

    Returns:
         Union[Path, None]: Path to the ground truth text file or None if not ground truth text file exists.
    """
    gt_path = Path(path.parent, path.stem).with_suffix(suffix)
    if gt_path.is_file():
        return gt_path
    return None


def data_from_image(image: Path) -> np.ndarray:
    """Converts an image file into a numpy array for augmentation calculations.

    Args:
        image (Path): Path to the image file.
    Returns:
         np.ndarray: Numpy array representing the image.
    """
    data = 255 - np.mean(np.array(Image.open(str(image)).convert("RGB"))[:, :, 0:2], axis=-1)
    return data
