# SmolBPE

![PyPI Version](https://img.shields.io/pypi/v/smolbpe) ![PyPI - Downloads](https://img.shields.io/pypi/dm/smolbpe) ![GitHub Stars](https://img.shields.io/github/stars/T4ras123/SmolBPE?style=social) ![License](https://img.shields.io/github/license/T4ras123/SmolBPE) ![Python Versions](https://img.shields.io/pypi/pyversions/smolbpe) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/T4ras123/SmolBPE) [![Sponsor](https://img.shields.io/badge/sponsor-GitHub%20Sponsors-critical)](https://github.com/sponsors/T4ras123) [![Twitter Follow](https://img.shields.io/twitter/follow/vover163?style=social)](https://twitter.com/Vover163) ![Made with Love](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)

## Overview

**SmolBPE** is a lightweight and efficient Byte Pair Encoding (BPE) tokenizer designed for deep learning applications and large language models (LLMs) such as GPT-4. It provides a simple interface to tokenize textual data, facilitating better handling of out-of-vocabulary words and improving the performance of language models.

## Features

- **Efficient Tokenization**: Implements the BPE algorithm for effective subword tokenization.
- **Customizable Vocabulary Size**: Allows you to specify the desired vocabulary size according to your needs.
- **Unicode Support**: Handles a wide range of characters, including Unicode characters, enabling multilingual tokenization.
- **Easy Integration**: Designed for seamless integration with existing Python projects and NLP pipelines.
- **Command-Line Interface**: Provides a CLI tool for training and using the tokenizer without writing additional code.
- **Open Source**: Licensed under the MIT License, promoting openness and collaboration.

## Installation

You can install SmolBPE using `pip`:

```sh
pip install smolbpe
```

Alternatively, you can install it directly from the source code:

```sh
git clone https://github.com/T4ras123/SmolBPE.git
cd SmolBPE
pip install .
```

## Quick Start Guide

### Using the Tokenizer in Python

1.Importing the Tokenizer

  ```python
  from smolbpe.gpt4Tokenizer import GPT4Tokenizer
  ```

2.Initializing the Tokenizer

  ```python
  tokenizer = GPT4Tokenizer()
  ```

  You can specify a custom output file to save the vocab file to and regex pattern if needed:

  ```python
  tokenizer = GPT4Tokenizer(output='vocab.json', pattern=r"\p{L}+|\p{Z}+|\p{N}+|[\p{P}&&[^.]]")
  ```

3.Training the Tokenizer

  Train the tokenizer on your dataset to build the vocabulary and merge rules:

  ```python
  with open("path_to_your_data", "r", encoding="utf-8") as f:
      text = f.read()

  tokenizer.train(text, vocab_size=400)
  ```

4.Encoding Text

  Convert text into a list of token IDs:

  ```python
  encoded_tokens = tokenizer.encode("Tokenizing isn't real")
  print(encoded_tokens)
  ```

5.Decoding Tokens

Convert token IDs back into human-readable text:

```python
decoded_text = tokenizer.decode(encoded_tokens)
print(decoded_text)
```

### Command-Line Interface

SmolBPE provides a command-line interface for easy tokenization tasks.

#### Training the Tokenizer

```sh
gpt4tokenizer --text data/taylorswift.txt --vocab_size 400 --output vocab.json
```

## Advanced Usage

### Loading a Pre-trained Vocabulary

If you have a pre-trained vocabulary and merges file, you can load them directly:

```python
tokenizer = GPT4Tokenizer()
tokenizer.load_vocab('vocab.json')
```

### Custom Regex Pattern

Customize the tokenization by providing a different regex pattern:

```python
custom_pattern = r"\w+|\s+|[^\s\w]+"
tokenizer = GPT4Tokenizer(pattern=custom_pattern)
```

## Project Structure

```sh
SmolBPE/
├── smolbpe/
│   ├── __init__.py
│   └── gpt4Tokenizer.py
├── LICENSE
├── MANIFEST.in
├── README.md
└── setup.py
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with descriptive commit messages.
4. Push your branch to your forked repository.
5. Open a pull request on the main repository.

Please ensure your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software in accordance with the license.

## Contact

For any inquiries or feedback, please contact the author:

- Author: Vover
- Email: <vovatara123@gmail.com>
- GitHub: [T4ras123](https://github.com/T4ras123)

## Acknowledgments

- Inspired by tokenization techniques used in GPT models.
- Special thanks to the open-source community for continuous support.

----
Happy tokenizing with *SmolBPE*!
