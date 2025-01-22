from setuptools import setup, find_packages

setup(
    name="owl-eye",
    version="0.1.4",
    author="Ishan Oshada",
    description="A WHOIS lookup tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ishanoshada/Owl-Eye",
    packages=find_packages(),
    install_requires=[
        "colorama",
        "pyfiglet",
        "requests",
        "beautifulsoup4"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "owl-eye=owl_eye.main:main",
        ],
    }
)
