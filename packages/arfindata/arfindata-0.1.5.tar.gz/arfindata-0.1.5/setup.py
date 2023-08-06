# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 05:01:25 2023

@author: Napstablook
"""
from setuptools import find_packages, setup
# Package meta-data.
NAME = 'arfindata'
DESCRIPTION = "Python package for the aquisition and pre-treatment of China's listed companies' annual reports"
URL = 'https://github.com/napstablook04/ARfindata'
EMAIL = 'linkfr@163.com'    # 你的邮箱
AUTHOR = 'linkfr'     # 你的名字
REQUIRES_PYTHON = '>=3.6.0' # 项目支持的python版本
VERSION = '0.1.5'           # 项目版本号
REQUIRED = ['pandas','selenium','fitz','pdfplumber','requests']

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(),
    install_requires=REQUIRED,
    license="MIT"
)

