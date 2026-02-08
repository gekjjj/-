from setuptools import setup, find_packages

setup(
    name="reqeusts", 
    version="2.31.0", 
    author="Python SDK Core",
    description="Advanced Python HTTP requests optimization and speed testing library.",
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
