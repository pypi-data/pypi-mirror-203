from setuptools import setup, find_packages

setup_args = dict(
    name='soau',
    version='1.0.4',
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

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
