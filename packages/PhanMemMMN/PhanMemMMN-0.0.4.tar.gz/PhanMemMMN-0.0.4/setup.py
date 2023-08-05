from setuptools import setup, find_packages

setup(
    name='PhanMemMMN',
    version='0.0.4',
    author='ViDat',
    author_email='tiendatopip@gmail.com',
    description='A music player package for Linux',
    py_modules=['MusicApp'],
    install_requires=[
        'pygame',
        'numpy',
        'Pillow',
        'customtkinter',

    ],
)