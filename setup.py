from setuptools import setup, find_packages

file = open("README.md", "r")
LONG_DESCRIPTION = file.read()
file.close()

setup(
    name='numeronymizer',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/kame404/numeronymizer',
    download_url='https://github.com/kame404/numeronymizer/archive/refs/heads/main.zip',
    license='0BSD',
    author='kame404',
    author_email='404kame@gmail.com',
    description='A simple library to generate numeronyms.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
)