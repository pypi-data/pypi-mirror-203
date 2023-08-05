from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Send messages, files or raw data between python codes(servers, computers, ...).'
LONG_DESCRIPTION = 'A package that allows to build simple server with listening and handling all data.'

# Setting up
setup(
    name="interlinking",
    version=VERSION,
    author="AdioSs (Daniel Karlík)",
    author_email="<karlik.dan@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['tqdm'],
    keywords=['python', 'server', 'client', 'data sending', 'servers communication', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)