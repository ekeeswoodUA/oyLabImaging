from setuptools import setup, find_packages
from pathlib import Path

CU111_EXTRAS = [
    "cupy-cuda111 ; platform_system!='Darwin' and python_version<'3.10'",
    # PY38 - LINUX
    "torch@https://download.pytorch.org/whl/cu111/torch-1.8.1%2Bcu111-cp38-cp38-linux_x86_64.whl ; platform_system>='Linux' and python_version>='3.8'",
    "torchvision@https://download.pytorch.org/whl/cu111/torchvision-0.9.1%2Bcu111-cp38-cp38-linux_x86_64.whl ; platform_system>='Linux' and python_version>='3.8'",
    "torchaudio@https://download.pytorch.org/whl/torchaudio-0.8.1-cp38-cp38-linux_x86_64.whl ; platform_system>='Linux' and python_version>='3.8'",
    # PY38 - WINDOWS
    "torch@https://download.pytorch.org/whl/cu111/torch-1.8.1%2Bcu111-cp38-cp38-win_amd64.whl ; platform_system>='Windows' and python_version>='3.8'",
    "torchvision@https://download.pytorch.org/whl/cu111/torchvision-0.9.1%2Bcu111-cp38-cp38-win_amd64.whl ; platform_system>='Windows' and python_version>='3.8'",
    "torchaudio@https://download.pytorch.org/whl/torchaudio-0.8.1-cp38-cp38-win_amd64.whl ; platform_system>='Windows' and python_version>='3.8'",
]


setup(
    name="oyLabImaging",
    version="0.2.6",
    description="data processing code for the Oyler-Yaniv lab @HMS",
    author="Alon Oyler-Yaniv",
    url="https://github.com/alonyan/oyLabImaging",
    packages=find_packages(include=["oyLabImaging", "oyLabImaging.*"]),
    python_requires=">=3.8", #Commenting out cap to get lastest python so it doesn't conflict with python version in conda env, <3.12", #Changed from <3.9 to <3.12
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    dependency_links=["https://download.pytorch.org/whl/torch_stable.html"],
    install_requires=[
        "opencv-python-headless>=4.7.0.68",
        "cellpose>=0.7.2",
        "cloudpickle>=1.6.0",
        "dill>=0.3.4",
        "ipython>=7.27.0",
        "ipywidgets>=7.6.5",
        #"lap05", commenting out because lap05 relies on numpy.distutils. Hopefully the overall code doesn't rely on it too much
        "lap", #instead of lap05 I'm attempting to use lap
        "matplotlib>=3.3.4",
        "napari[pyqt5]>=0.4.14",
        "pydantic<2", # pinned only because of napari
        "magicgui",
        "nd2>=0.8.0",
        "numba>=0.53.1",
        "numpy>=1.22.4",#changed to be less than 1.23.0 beacuse numpy.distutils has deprecated after 1.23.0
        "pandas>=1.2.4",
        "Pillow>=8.3.1",
        "poppy>=1.0.1",
        "setuptools>=59.8.0", #Changed to be less than 60.0 because numpy.distutils is deprecated after that
        "scikit-image",
        "scikit-learn>=1.0.2",
        "scipy>=1.6.2",
        "tqdm>=4.59.0",
        "zernike>=0.0.32",
        "multiprocess>=0.70",
        "jupyter>=1.0.0",
        "tensorflow-cpu>=2.10.0 ; platform_machine!='arm64'",
        "stardist>=0.8.3",
    ],
    extras_require={
        "cuda": CU111_EXTRAS,
        "test": ["pytest", "pytest-cov"],
    },
)
