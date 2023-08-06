from setuptools import setup, find_packages

setup(
    name='AliveHelper',
    version='1.3',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*.*']
    },
    install_requires=[
        'flask'
    ],
    python_requires='>=3.9'
)
