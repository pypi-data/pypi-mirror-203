from setuptools import setup, find_packages

setup(
    name='headfuck',
    version='1.0',
    packages=find_packages(),
    # metadata
    author='JJPMaster',
    author_email='ssatjyrbusiness@gmail.com',
    description='An esoteric programming language similar to Brainfuck',
    url='https://github.com/JJPMaster/headfuck',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Unlicense',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'headfuck=headfuck.interpreter:interpret',
        ],
    },
)
