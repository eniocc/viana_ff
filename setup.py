#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

test_requirements = ['pytest>=3', ]

setup(
    author="Ênio Viana",
    author_email='eniocc@gmail.com',
    python_requires='==3.10',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.10',
    ],
    description="A comprehensive framework designed for forensic analysis of video, image, and audio data, powered by neural networks. VIANA Forensic Framework provides tools for the automated and assisted identification, authentication, and enhancement of multimedia evidence, leveraging state-of-the-art machine learning techniques. Ideal for professionals working in digital forensics, security, and law enforcement, this framework offers an efficient and scalable solution for analyzing media with precision and accuracy.",
    install_requires=requirements,
    license="Creative Commons NonCommercial Attribution License (CC BY-NC 4.0)",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='viana_ff',
    name='viana_ff',
    packages=find_packages(include=['viana_ff', 'viana_ff.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/eniocc/viana_ff',
    version='1.0.0',
    zip_safe=False,
)
