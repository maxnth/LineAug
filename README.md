# LineAug
Augment line images for improving OCR datasets 

## Getting Started
### PyPi 
`pip install lineaug`
### Manually
Run `python setup.py install` inside the clone repository.

## CLI
```
usage: augment.py [-h] -i [IMAGES [IMAGES ...]] [-o OUTPUT] [-gt GROUND_TRUTH] [-n N] [-bg] [-e]

Augment OCR in the form of line images.

optional arguments:
  -h, --help            show this help message and exit
  -i [IMAGES [IMAGES ...]], --images [IMAGES [IMAGES ...]]
                        Path to line image(s).
  -o OUTPUT, --output OUTPUT
                        Output path where augmented images will be saved.
  -gt GROUND_TRUTH, --ground_truth GROUND_TRUTH
                        Extension of the ground truth text files. Will create new ground truth files for the augmented line images containing the existing ground truth for the associated
                        line (optional).
  -n N                  Number of augmented line image variants to create for each input.
  -bg, --background     Whether to add noise to the background of the line image.
  -e, --enumerate       Enumerate output file names instead of using input file names.
```
