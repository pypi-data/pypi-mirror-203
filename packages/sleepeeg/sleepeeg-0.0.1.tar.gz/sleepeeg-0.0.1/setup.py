from setuptools import setup

setup(
    name="sleepeeg",
    version="0.0.1",
    install_requires=[
        "attrs",
        "mne",
        "mne-qt-browser",
        "pyqt5",
        "yasa==0.6.3",
        "lspopt",
    ],
)
