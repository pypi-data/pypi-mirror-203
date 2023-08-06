from setuptools import setup,find_packages

setup(
    name="failSafePackage",
    version="0.0.4",
    description= "This class is written to handeled fail-safe conditions for all PMS.",
    long_description="",
    author="Rahul Khose",
    packages= find_packages(),
    install_requires=['numpy==1.21.5'],
)
