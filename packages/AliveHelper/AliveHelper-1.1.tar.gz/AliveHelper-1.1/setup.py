from setuptools import setup, find_packages

setup(
    name='AliveHelper',
    version='1.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*.*']
    },
    install_requires=[
        'flask'
    ],
    entry_points={
        'console_scripts': [
            'your_package_name=AliveHelper'
        ]
    },
    python_requires='>=3.9'
)
