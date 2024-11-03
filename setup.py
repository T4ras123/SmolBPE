from setuptools import setup, find_packages

setup(
    name='gpt4tokenizer',
    version='0.1.0',
    description='A GPT-4 compatible Byte Pair Encoding (BPE) tokenizer.',
    author='Vover',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/gpt4tokenizer',  # Replace with your repository URL
    packages=find_packages(include=['smolbpe', 'smolbpe.*']),
    install_requires=[
        'regex>=2021.4.4',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    include_package_data=True,
    package_data={
        'smolbpe': ['data/*.txt', 'data/*.json'],
    },
    entry_points={
        'console_scripts': [
            'gpt4tokenizer=smolbpe.gpt4Tokenizer:main',  # If you have a main function
        ],
    },
)