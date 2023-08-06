from setuptools import setup

setup(
    name='typewriter2',
    version='1.0.0',
    description='A library for printing messages with typewriter effects.',
    py_modules=['typewriter'],
    entry_points={
        'console_scripts': [
            'typewriter = typewriter:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
