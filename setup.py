from distutils.core import setup
from setuptools import find_packages

setup(
    name='mtgobot-api',
    version='0.1',
    packages=find_packages(),
    url='',
    license='',
    author='Andy Levisay',
    author_email='levisaya@gmail.com',
    description='',
    install_requires=[
        'flask==0.12',
        'pywinauto==0.6.2',
        'pywin32==221',
        'comtypes==1.1.3',
        'pillow==4.1.1',
        'imagehash==3.4'
    ]
)
