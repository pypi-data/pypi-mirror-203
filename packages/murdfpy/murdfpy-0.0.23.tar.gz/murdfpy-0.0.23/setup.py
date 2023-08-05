"""
Author: Matthew Matl
"""
from setuptools import setup

requirements = [
    'lxml',             # For XML DOM Tree
    'networkx',    # For joint graph
    'numpy',            # Numpy
    'pillow',           # For texture image loading
    'pycollada',   # COLLADA (.dae) mesh loading via trimesh
    'pyrender>=0.1.20', # For visualization
    'scipy',            # For trimesh, annoyingly
    'six',              # Python 2/3 compatability
    'trimesh',          # Mesh geometry loading/creation/saving
]

dev_requirements = [
    'flake8',            # Code formatting checker
    'pre-commit',        # Pre-commit hooks
    'pytest',            # Code testing
    'pytest-cov',        # Coverage testing
    'tox',               # Automatic virtualenv testing
]

docs_requirements = [
    'sphinx',            # General doc library
    'sphinx_rtd_theme',  # RTD theme for sphinx
    'sphinx-automodapi'  # For generating nice tables
]

exec(open('murdfpy/version.py').read())

setup(
    name='murdfpy',
    version=__version__,
    description='URDF parser and manipulator for Python',
    long_description='URDF parser and manipulator for Python',
    author='Matthew Matl',
    author_email='matthewcmatl@gmail.com',
    mantainer='Silvio Traversaro',
    mantainer_email='silvio.traversaro@iit.it',
    license='MIT License',
    url='https://github.com/ami-iit/murdfpy',
    keywords='robotics ros urdf robots parser',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering'
    ],
    packages=['murdfpy'],
    setup_requires = requirements,
    install_requires=requirements,
    extras_require={
        'dev': dev_requirements,
        'docs': docs_requirements,
    }
)
