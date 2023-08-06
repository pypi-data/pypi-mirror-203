
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
    name="test-bmi",
    version="1.0",
    packages=find_packages(),
    py_modules=['test_bmi'],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'test_bmi = test_bmi:main',
        ],
    },
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',)
