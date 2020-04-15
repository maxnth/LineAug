from pathlib import Path
from typing import Union

import numpy as np
from PIL import Image


def get_gt(path: Path, suffix: str) -> Union[Path, None]:
    gt_path = Path(path.parent, path.stem).with_suffix(suffix)
    if gt_path.is_file():
        return gt_path
    return None


def data_from_image(image: Path) -> np.ndarray:
    data = 255 - np.mean(np.array(Image.open(str(image)).convert("RGB"))[:, :, 0:2], axis=-1)
    return data
