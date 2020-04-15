# LineAug
Augment line images for improving OCR datasets 

## CLI
```
usage: augment.py [-h] -i [IMAGES [IMAGES ...]] [-o OUTPUT] [-gt GROUND_TRUTH] [-n N] [-mbg] [-e]

Augment OCR in the form of line images.

optional arguments:
  -h, --help            show this help message and exit
  -i [IMAGES [IMAGES ...]], --images [IMAGES [IMAGES ...]]
                        Path to line image(s).
  -o OUTPUT, --output OUTPUT
                        Output path where augmented images will be saved.
  -gt GROUND_TRUTH, --ground_truth GROUND_TRUTH
                        Extension of the ground truth text files.
  -n N                  Number of augmented line image variants to create for each input.
  -mbg, --mean_background
                        Whether to set the background to the mean color of the input line image.
  -e, --enumerate       Enumerate output file names instead of using input file names.
```
