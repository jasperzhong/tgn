import setuptools

setuptools.setup(
    name="meme",
    version="0.0.1",
    description="TGN: Temporal Graph Networks",
    url="https://github.com/jasperzhong/tgn",
    packages=setuptools.find_packages(exclude=("tests")),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6'
)
