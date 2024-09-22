#!/usr/bin/env python

"""The setup script."""
from pathlib import Path

from setuptools import setup


def _get_version() -> str:
    """Read cookiecutter/VERSION.txt and return its contents."""
    path = Path("version").resolve()
    version_file = path / "VERSION.txt"
    return version_file.read_text().strip()


version = _get_version()

readme = Path('README.md').read_text(encoding='utf-8')

requirements = []

setup(
    author="Ênio Viana",
    author_email='eniocc@gmail.com',
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: Creative Commons NonCommercial Attribution License (CC BY-NC 4.0)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.10',
    ],
    description="A comprehensive framework designed for forensic analysis of video, image, and audio data, powered by "
                "neural networks. VIANA Forensic Framework provides tools for the automated and assisted "
                "identification, authentication, and enhancement of multimedia evidence, leveraging state-of-the-art "
                "machine learning techniques. Ideal for professionals working in digital forensics, security, "
                "and law enforcement, this framework offers an efficient and scalable solution for analyzing media "
                "with precision and accuracy.",
    install_requires=requirements,
    license="Creative Commons NonCommercial Attribution License (CC BY-NC 4.0)",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='viana_ff',
    name='viana_ff',
    packages=['viana_ff', 'viana_ff.*'],
    test_suite='tests',
    url='https://github.com/eniocc/viana_ff',
    version='1.0.0',
    zip_safe=False,
)
