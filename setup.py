import setuptools
import re

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("facebooklogger/_version.py", "r") as f:
    version_match = re.search(
        r'^version \s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    )
    if version_match is None:
        raise ValueError("Version not found in facebooklogger/_version.py")
    version = version_match.group(1)

setuptools.setup(
    name="facebooklogger",
    version=version,
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
        "License :: OSI Approved :: MIT License",
        "Topic :: System :: Logging",
        "Topic :: System :: Monitoring",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Development Status :: 4 - Beta",
    ],
    python_requires=">=3.6",
)
