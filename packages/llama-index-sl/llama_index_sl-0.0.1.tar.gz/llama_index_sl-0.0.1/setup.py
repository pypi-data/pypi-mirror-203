from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'llama_index edited for unicode support'

# Setting up
setup(
    name="llama_index_sl",
    version=VERSION,
    author="sl",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pdfminer'],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)