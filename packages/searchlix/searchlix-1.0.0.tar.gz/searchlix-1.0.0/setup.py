from setuptools import setup, find_packages

setup(
    name='searchlix',
    version='1.0.0',
    description='A package for extract data from websites and text',
    author='Hashem',
    author_email='hashem.a.muhammad@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',

    ],
    keywords=['python', 'web scraping', 'emails', 'phone', 'data', 'search'],
   
)
