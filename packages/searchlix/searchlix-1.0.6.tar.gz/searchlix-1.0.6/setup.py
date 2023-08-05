from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='searchlix',
    version='1.0.6',
    description='A package for extract data from websites and text',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Hashem',
    author_email='hashem.a.muhammad@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'dnspython==2.3.0'

    ],
    keywords=['python', 'web scraping', 'emails', 'phone', 'data', 'search'],
   
)
