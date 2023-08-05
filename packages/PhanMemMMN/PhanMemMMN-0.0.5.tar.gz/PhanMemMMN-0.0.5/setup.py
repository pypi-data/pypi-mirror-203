from setuptools import setup, find_packages

setup(
    name='PhanMemMMN',
    version='0.0.5',
    author='ViDat',
    author_email='tiendatopip@gmail.com',
    description='A music player package for Linux',
    packages=find_packages(),
    package_data={
        'PhanMemMMN' : ['img/*']
    },
    py_modules=['MusicApp'],
    install_requires=[
        'pygame',
        'numpy',
        'Pillow',
        'customtkinter',

    ],
)