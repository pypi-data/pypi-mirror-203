# Source: https://github.com/hmeine/qimage2ndarray/blob/master/setup.py

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from pathlib import Path

# TODO: Modify path when refactoring
for line in open(Path("src") / "GUI" / "__init__.py"):
    if line.startswith("__version__"):
        exec(line)

install_requires: list[str]

print(f"cwd: {Path().cwd()}")

# with open(Path("requirements.txt")) as f:
#     install_requires = f.read().splitlines()

install_requires: list[str] = [
    "setuptools",
    "sphinx",
    "sphinx_rtd_theme",
    "SimpleITK",
    "numpy",
    "argparse",
    "opencv-python",
    "pytest",
    "PyQt6",
    "qimage2ndarray",
    "screeninfo",
    "black",
    "pre-commit",
    "build",
    "twine",
]

setup(
    name="NeuroRuler",
    version=__version__,
    description="A program that calculates head circumference from MRI data (`.nii`, `.nii.gz`, `.nrrd`).",
    # Cannot use multiple authors
    # https://stackoverflow.com/questions/9999829/how-to-specify-multiple-authors-emails-in-setup-py
    author="COMP523 Team D",
    author_email="comp523d@gmail.com",
    url="https://github.com/COMP523TeamD/HeadCircumferenceTool",
    download_url="https://github.com/COMP523TeamD/HeadCircumferenceTool/releases",
    keywords=[
        "MRI",
        "NIfTI",
        "NRRD",
        "brain",
        "circumference",
        "PyQt6",
    ],
    install_requires=install_requires,
    # We don't need extras_require
    # See https://stackoverflow.com/questions/41268863/what-is-the-difference-between-extras-require-and-install-requires-in-se
    # extras_require=dict(),
    tests_require="pytest",
    # TODO: Change after refactoring
    packages=["src.GUI"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
