from setuptools import setup, find_packages
from pip._internal.req.req_file import parse_requirements

install_reqs = parse_requirements("requirements.txt", session=False)
requirements = [str(ir.requirement) for ir in install_reqs]

setup(
    name='package02yxx',
    version='0.1.0',
    description='My awesome module',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=requirements,
)