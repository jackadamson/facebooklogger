import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="facebooklogger",
    version="0.1.0",
    author="Jack Adamson",
    author_email="jack@mrfluffybunny.com",
    description="A logging handler that sends you log entries on Facebook Messenger",
    install_requires=["pymessenger", "environs", "requests"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jackadamson/facebooklogger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.6",
)
