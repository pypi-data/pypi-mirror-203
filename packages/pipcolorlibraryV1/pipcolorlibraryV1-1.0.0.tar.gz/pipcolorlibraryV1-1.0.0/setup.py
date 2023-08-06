from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = "pipcolorlibraryV1 is a Python package that provides a comprehensive collection of color-related functionalities for developers and designers alike. With this package, you can easily manipulate and work with various color formats such as RGB, HEX, and HSL."
LONG_DESCRIPTION = "pipcolorlibraryV1 is a Python package that provides a comprehensive collection of color-related functionalities for developers and designers alike. With this package, you can easily manipulate and work with various color formats such as RGB, HEX, and HSL."

# Setting up
setup(
    name="pipcolorlibraryV1",
    version=VERSION,
    author="Bluescreen",
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