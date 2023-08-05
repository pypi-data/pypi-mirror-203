import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

ver_string = os.environ['CI_COMMIT_TAG'][1:]

setuptools.setup(
    name="cdp-py",
    version=ver_string,
    author="Ciholas, Inc.",
    author_email="cuwb.support@ciholas.com",
    description="Ciholas Data Protocol",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ciholas/cdp-py",
    license="CC BY 4.0",
    keywords="cdp ciholas data protocol",
    python_requires='>=3',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
