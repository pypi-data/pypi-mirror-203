#!/usr/bin/env python
import setuptools

setuptools.setup(
    name='sunnyday-IZPy',
    packages=setuptools.find_packages(),
    version='2.0.0',
    license='MIT',
    description='Weather forecast data',
    author='Ivo Zelic',
    author_email='izpy81@gmail.com',
    url='https://github.com/DevIvo81/App-011-WeatherApp',
    keywords=['weather', 'forecast', 'openweather'],
    install_requires=['requests', ],

    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ]
)
