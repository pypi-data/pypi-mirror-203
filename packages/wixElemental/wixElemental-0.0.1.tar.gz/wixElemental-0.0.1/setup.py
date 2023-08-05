from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'WIX API Request Module to Use with Elemental Apps in your Wix Store WebSite'
LONG_DESCRIPTION = 'A package that allows to request WIX API with ease, in order to use Elemental Apps in your WIX WebSite'

setup(
    name="wixElemental",
    version=VERSION,
    author="Elemental (Tom Neto)",
    author_email="<info@elemental.run>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'WIX', 'Store', 'API', 'Request'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.11",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)