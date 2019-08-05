from setuptools import setup, find_packages
from glob import glob

pn = 'pybind11_tools/'

files = glob(pn + '*.py') + glob(pn + '*.cmake') + glob(pn + '*.sh') + glob(pn + 'clang/*')

files = [f[len(pn):] for f in files]

setup(
    name='pybind11_cmake',
    version='0.0.1',
    author='Jariullah Safi',
    author_email='safijari@isu.edu',
    description='A package to contain the minimum required cmake config for pybind11',
    long_description='',
    zip_safe=False,
    packages=find_packages(),
    scripts=['pybind11_new_project'],
    include_package_data=True,
    install_requires=['pybind11>=2,<3', 'argh'],
    package_data={'pybind11_tools': files},
)
