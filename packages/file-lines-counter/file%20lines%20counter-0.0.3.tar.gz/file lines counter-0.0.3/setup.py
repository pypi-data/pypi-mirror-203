import setuptools


setuptools.setup(
    name="file lines counter",
    version="0.0.3",
    author="me",
    author_email="aa@example.com",
    description=("lines  counter"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["typer"],
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "count = src.wc_util:app",
        ]
    },
)
