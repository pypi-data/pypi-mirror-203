import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name                = 'deepilab',
    version             = '0.0.2',
    author              = 'jskim1102',
    author_email        = 'deepi.contact.us@gmail.com',
    long_description=long_description,
    url                 = 'https://github.com/jskim1102/deepi-yolov8',
    download_url        = 'https://github.com/jskim1102/deepi-yolov8/archive/0.0.tar.gz',
    install_requires    =  [],
    packages=setuptools.find_packages(),
    python_requires     = '>=3.8',
)