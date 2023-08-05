from setuptools import setup
import setuptools
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='SentenceMatcher',
    version='0.0.2',
    description='A simple yet useful module that allows you to match a sentence against a list of sentences and return the closest match',
    author= 'Mahdi Tajwar',
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['sentencematcher', 'sentence', 'matcher', 'ai', 'chatbot', 'language'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    #python_requires='>=3.6',
    py_modules=['SentenceMatcher'],
    package_dir={'':'src'},
)