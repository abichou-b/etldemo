from setuptools import setup, find_packages

setup(
    name="demo",
    version="0.0.1",
    description="etl with python", 
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'demo = demo.etl:demo_etl'
        ],
    },
    license="MIT"
)