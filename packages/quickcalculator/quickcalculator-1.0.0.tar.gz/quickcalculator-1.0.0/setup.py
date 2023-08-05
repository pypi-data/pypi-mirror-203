from setuptools import setup, find_packages

setup(
    name='quickcalculator',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'quick_calculator = quick_calculator:main'
        ]
    },
    install_requires=[
        # list any dependencies your package requires here
    ],
    description='A quick calculator program'
)
