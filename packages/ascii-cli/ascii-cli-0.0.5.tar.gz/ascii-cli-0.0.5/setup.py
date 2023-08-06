from setuptools import setup, find_packages

setup(
    name="ascii-cli",
    author="mrq-andras",
    version="0.0.5",
    packages=find_packages(),
    install_requires=["Pillow"],
    entry_points={
        "console_scripts": [
            "ascii-cli = ascii:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    url="https://github.com/mrq-andras/ascii-cli",
    license="MIT",
    description="A command-line tool that converts images to ASCII art.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
