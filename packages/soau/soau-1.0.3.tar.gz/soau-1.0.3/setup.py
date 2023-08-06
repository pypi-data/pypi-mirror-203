from setuptools import setup, find_packages

setup(
    name='soau',
    version='1.0.3',
    author='dajokep275',
    packages=find_packages(),
    keywords='soau python',
    python_requires='>=3.7'
)

install_requires = [
    'tqdm',
    'PyAutoGUI',
    'sounddevice',
    'psutil',
    'GPUtil',
    'tabulate',
    'scipy',
    'setuptools'
]
