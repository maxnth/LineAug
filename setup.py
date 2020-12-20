import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lineaug",
    version="0.1",
    license="MIT License",
    author="Maximilian Nöth",
    author_email="maximilian.noeth@protonmail.com",
    description="Augment line images for improving OCR datasets ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maxnth/lineaug",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy>=1.18.2",
        "Pillow>=7.1.1",
        "scipy>=1.4.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "lineaug-augment = lineaug.scripts.augment:main"
        ]
    },
    keywords=["Augmentation", "OCR", "optical character recognition"],
    python_requires='>=3.6',
)
