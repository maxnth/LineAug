from src.Augmentation import Augmentation
from src.utils import get_gt, data_from_image

from pathlib import Path
import shutil
import argparse

parser = argparse.ArgumentParser(description="Augment OCR in the form of line images.")

parser.add_argument("-i", "--images", required=True, type=str, nargs="*", help="Path to line image(s).")
parser.add_argument("-o", "--output", default=Path("."), type=str,
                    help="Output path where augmented images will be saved.")
parser.add_argument("-gt", "--ground_truth", type=str, help="Extension of the ground truth text files.")
parser.add_argument("-n", type=int, default=1, help="Number of augmented line image variants to create for each input.")
parser.add_argument("-mbg", "--mean_background", action="store_true",
                    default=False, help="Whether to set the background to the mean color of the input line image.")
parser.add_argument("-e", "--enumerate", action="store_true",
                    default=False, help="Enumerate output file names instead of using input file names.")

args = parser.parse_args()

if __name__ == "__main__":
    counter = 1

    for image in args.images:
        img_counter = 1
        image = Path(image)

        img = data_from_image(image)

        for n in range(args.n):
            out_filename = Path(args.output, str(counter).zfill(5)).with_suffix("".join(image.suffixes)) if args.enumerate else \
                Path(args.output, f"{image.name.split('.')[0]}_{str(img_counter).zfill(4)}").with_suffix("".join(image.suffixes))

            aug = Augmentation(img, args.mean_background)
            aug.export(out_filename)

            if args.ground_truth:
                gt = get_gt(image, args.ground_truth)
                shutil.copyfile(str(gt), str(Path(out_filename.parent,
                                                  out_filename.stem).with_suffix("".join(gt.suffixes))))

            counter += 1
            img_counter += 1
