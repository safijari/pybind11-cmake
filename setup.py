from setuptools import setup, find_packages
from glob import glob

pn = 'pybind11_cmake/'

files = glob(pn + '*.py') + glob(pn + '*.cmake') + glob(pn + '*.sh') + glob(pn + 'clang/*')

files = [f[len(pn):] for f in files]

setup(
    name='pybind11_cmake',
    version='1.0.0',
    author='Jariullah Safi',
    author_email='safijari@isu.edu',
    description='Straightforward boilerplate generation for pybind11 + cmake',
    long_description='https://github.com/safijari/pybind11-cmake',
    zip_safe=False,
    packages=find_packages(),
    scripts=['pybind11_new_project'],
    url='https://github.com/safijari/pybind11-cmake',
    include_package_data=True,
    install_requires=['pybind11>=2,<3', 'argh'],
    package_data={'pybind11_cmake': files},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Programming Language :: C++',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: BSD License'
    ],
    keywords='C++11, Python bindings, CMake, boilerplate',
)
