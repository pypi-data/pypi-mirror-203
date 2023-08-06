from setuptools import setup, find_packages
from pathlib import Path

here = Path(__file__).resolve().parent
README = (here / "README.md").read_text(encoding="utf-8")
VERSION = (here / "VERSION").read_text(encoding="utf-8").strip()

setup(
    name='blossomai',
    packages=['blossomai',
              ] + find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    entry_points={
        "console_scripts": ["blossomai=blossomai.cli:execute_cli"],
    },
    version=VERSION,
    license='mit',
    description='blossomAI automates data exploration and visualization',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Sherif Abdulkader Tawfik Abbas',
    author_email='sherif.tawfic@gmail.com',
    url='https://github.com/sheriftawfikabbas/blossomai',
    keywords=['ai', 'data visualization',
              'data science'],
    install_requires=['xgboost',
                      'pandas',
                      'numpy'],

)
