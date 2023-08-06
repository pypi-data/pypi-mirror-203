
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
    name="to-cloud-run",
    version="1.6",
    packages=find_packages(),
    py_modules=['to_cloud_run'],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'to_cloud_run = to_cloud_run:main',
        ],
    },
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',)
