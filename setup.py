from setuptools import setup, find_packages

setup(
    name='smolbpe',
    version='0.3.1',
    description='A GPT-4 compatible Byte Pair Encoding (BPE) tokenizer.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown', 
    author='Vover',
    author_email='vovatara123@gmail.com',
    url='https://github.com/T4ras123/SmolBPE',
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
            'gpt4tokenizer=smolbpe.gpt4Tokenizer:main', 
        ],
    },
)
