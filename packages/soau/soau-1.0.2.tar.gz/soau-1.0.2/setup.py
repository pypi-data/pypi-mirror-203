from setuptools import setup, find_packages

setup(
    name='soau',
    version='1.0.2',
    author='dajokep275',
    packages=find_packages(),
    keywords='soau python',
    python_requires='>=3.7'
)

install_requires = [
    'tqdm~=4.65.0',
    'PyAutoGUI~=0.9.53',
    'sounddevice~=0.4.6',
    'psutil~=5.9.4',
    'GPUtil~=1.4.0',
    'tabulate~=0.9.0',
    'scipy~=1.10.1',
    'setuptools~=65.5.0'
]
