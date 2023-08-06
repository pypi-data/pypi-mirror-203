from setuptools import setup, find_packages

setup(
    name="smart-scrap",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "scrap = scrap.main:main",
        ],
    },
    install_requires=[
        # Add any required dependencies here
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
