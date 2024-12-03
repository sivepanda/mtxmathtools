from setuptools import setup, find_packages
print(find_packages())

setup(
    name='mtxmathtools',
    version='0.4.0',
    packages=find_packages(include=['mtxmathtools']),
    install_requires=[
        'sympy',
    ],
    entry_points={
        'console_scripts': [
            'mtxmathtools=mtxmathtools.computemtx:main',
        ],
    },
)
