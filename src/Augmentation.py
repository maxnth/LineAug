import libs.ocrodeg as ocrodeg

import numpy as np
from PIL import Image


class Augmentation:
    def __init__(self, img_data: np.array, mean_bg: False):
        self.img_data = img_data.T
        self.mean_bg = mean_bg

        self.aug_data = self.augment_line()

    def augment_line(self) -> np.ndarray:
        original_dtype = self.img_data.dtype
        data = self.img_data.astype(np.float)
        m = data.max()
        data = data / (1 if m == 0 else m)
        data = ocrodeg.random_pad(data, (0, data.shape[1] * 2))

        for sigma in [2, 5]:
            noise = ocrodeg.bounded_gaussian_noise(data.shape, sigma, 3.0)
            data = ocrodeg.distort_with_noise(data, noise)

        if self.mean_bg:
            data = ocrodeg.printlike_multiscale(data, blur=1, inverted=True)
        data = (data * 255 / data.max()).astype(original_dtype)
        return data.T

    def export(self, out_filename: str):
        formatted = (255 - self.aug_data * 255 / np.max(255 - self.aug_data)).astype('uint8')
        img = Image.fromarray(formatted).convert("RGB")
        img.save(out_filename)
