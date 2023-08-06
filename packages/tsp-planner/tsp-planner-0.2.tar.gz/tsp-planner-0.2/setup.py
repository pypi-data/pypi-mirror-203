from setuptools import setup, find_packages

setup(
    name='tsp-planner',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'pika',
        'ortools'
    ],
    entry_points={
        'console_scripts': [
            'tsp_planner = tsp_planner.main:main'
        ]
    },
    author='Planning Tech',
    description='A service for solving the Travelling Salesman Problem using OR-tools library',
    url='https://github.com/ghorbani-mohammad/travelling-salesman-problem'
)
