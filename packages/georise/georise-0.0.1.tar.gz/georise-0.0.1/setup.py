from setuptools import setup, find_packages

setup(
    name="georise",
    version="0.0.1",
    author='Jack David Carson',
    author_email='jackdavidcarson@gmail.com',
    description='A Python Library Built on GDAL for Visualization of Geospatial Maps',
    url='https://github.com/quothbonney/georise',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        'geopy==2.3.0',
        'matplotlib==3.4.3',
        'numpy==1.24.2',
        'numpy==1.17.4',
        'osgeo==0.0.1',
        'PyQt5==5.15.9',
        'PyQt5_sip==12.11.1',
        'pyqtgraph==0.13.1',
        'pytest==7.3.0',
        'rasterio==1.3.6',
        'setuptools==44.0.0',
        'setuptools==45.2.0'
    ],
    python_requires='>=3.6',
)

