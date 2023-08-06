from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='hashcercle',
    version='1.0.1',
    description='Helper to certify database entries, using hashcercle and blockchains',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='',
    author='Seraphin Vandegar',
    author_email='',
    license='MIT',
    packages=['hashcercle','hashcercle.ethereum'],
    zip_safe=False,
    download_url='',
    install_requires=[
        'web3',
        'pysha3'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5'
    ]
)
