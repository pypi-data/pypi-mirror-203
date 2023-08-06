import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='bitkub-v2',
    version='2.1.0',
    description='A Python library for Bitkub API v2',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/appcorner/bitkub',
    author='appcorner',
    author_email='appcorner@yahoo.com',
    license='MIT',
    scripts=[],
    keywords=['bitkub', 'bitkub-python', 'bitkub-python-sdk'],
    packages=['bitkub-v2'],
    install_requires=['requests'],
)
