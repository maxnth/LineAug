import lineaug.libs as ocrodeg

import numpy as np
from PIL import Image


class Augmentation:
    """Represents a single augmentation of a line image.

    Args:
        img_data (np.ndarray): Numpy array representation of an image.
        bg (bool): Whether to add background noise during the augmentation.

    Attributes:
        img_data (np.ndarray): Numpy array representation of an image.
        bg (bool): Whether to add background noise during the augmentation.
        aug_data (np.ndarray): Numpy array representation of the augmented image. Basis for augmentation calculations.
    """
    def __init__(self, img_data: np.ndarray, bg: False):
        self.img_data = img_data.T
        self.bg = bg

        self.aug_data = self.augment_line()

    def augment_line(self) -> np.ndarray:
        """Calculate augmented line image based on the original image data.

        Returns:
            np.ndarray: Numpy array representation of the augmented image.
        """
        original_dtype = self.img_data.dtype
        data = self.img_data.astype(np.float)
        m = data.max()
        data = data / (1 if m == 0 else m)
        data = ocrodeg.random_pad(data, (0, data.shape[1] * 2))

        for sigma in [2, 5]:
            noise = ocrodeg.bounded_gaussian_noise(data.shape, sigma, 3.0)
            data = ocrodeg.distort_with_noise(data, noise)

        if self.bg:
            data = ocrodeg.printlike_multiscale(data, blur=1, inverted=True)
        data = (data * 255 / data.max()).astype(original_dtype)
        return data.T

    def export(self, out_filename: str):
        """Exports the augmented image to image file.

        Args:
            out_filename (str): Output filename for the generated line image.
        """
        formatted = (255 - self.aug_data * 255 / np.max(255 - self.aug_data)).astype('uint8')
        img = Image.fromarray(formatted).convert("RGB")
        img.save(out_filename)
