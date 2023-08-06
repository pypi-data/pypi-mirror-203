"""
End-to-End Multi-Lingual Optical Character Recognition (OCR) Solution
"""
from io import open
from setuptools import setup

with open('requirements.txt', encoding="utf-8-sig") as f:
    requirements = f.readlines()

def readme():
    with open('README.md', encoding="utf-8-sig") as f:
        README = f.read()
    return README

setup(
    name='nocv2easyocr',
    packages=['nocv2easyocr'],
    include_package_data=True,
    version='0.1.1',
    install_requires=requirements,
    entry_points={"console_scripts": ["easyocr= nocv2easyocr.cli:main"]},
    license='Apache License 2.0',
    description='This is a fork of the EasyOCR library without the opencv requirement',
    long_description=readme(),
    long_description_content_type="text/markdown",
    author='Rakpong Kittinaradorn',
    author_email='r.kittinaradorn@gmail.com',
    url='https://github.com/jaidedai/easyocr',
    download_url='https://github.com/jaidedai/nocv2easyocr.git',
    keywords=['ocr optical character recognition deep learning neural network'],
    classifiers=[
        'Development Status :: 5 - Production/Stable'
    ],

)
