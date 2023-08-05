import setuptools

setuptools.setup(
    name="digiDownload",
    url="https://github.com/DaniD3v/digiDownload",
    author="DaniD3v",

    description="API to download books from digi4school.at.",
    keywords=["digi4school", "books", "api"],

    version="0.0.3",
    license='MIT',

    packages=["digiDownload"],
    install_requires=["requests", "beautifulsoup4"],

    download_url='https://github.com/DaniD3v/digiDownload/archive/refs/tags/0.0.3.tar.gz',
)
