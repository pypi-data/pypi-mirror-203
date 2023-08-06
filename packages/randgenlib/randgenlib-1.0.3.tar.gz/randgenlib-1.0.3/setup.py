from setuptools import setup, find_packages

VERSION = '1.0.3'
DESCRIPTION = "Random gen lib"
LONG_DESCRIPTION = "Random gen lib"

# Setting up
setup(
    name="randgenlib",
    version=VERSION,
    author="GigaAlex",
    author_email="nick.faltermeier@gmx.de",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Operating System :: Microsoft :: Windows",
    ]
)