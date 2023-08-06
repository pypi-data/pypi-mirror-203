# Module imports
from setuptools import setup

# Arguments
version = "0.0.0" # update __init__.py
python_version = ">=3.10"

# Long description from README.md
with open("README.md", "r") as fh:
    long_description = fh.read()

# Define list of submodules
py_modules = [""]

# Run stup function
setup(
    name = 'augmenting',
    version = version,
    description = 'An image dataset augmentation package.',
    license='BSD',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = 'Jordan Welsman',
    author_email = 'welsman@lbl.gov',
    url = 'https://pypi.org/project/augmenting/',
    download_url='https://github.com/JordanWelsman/augmenting/tags',
    classifiers = [
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    package_data = {
      'augmenting': py_modules
      },
    python_requires=python_version,
    install_requires = [
        "jutl",
        "numpy",
    ],
    keywords='python, augmenting, dataset, training, deep learning, cleaning'
)