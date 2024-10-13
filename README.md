# SmolBPE

Tokenization for Deep Learning and Large Language Models (LLMs).
## Description

SmolBPE is a repository focused on providing efficient tokenization techniques for deep learning and large language models. This project is composed primarily of Jupyter Notebooks and Python scripts.

## Features

- Efficient tokenization algorithms.

---- 

## Byte pair encoding

Byte pair encoding (also known as digram coding) is an algorithm, first described in 1994 by Philip Gage for encoding strings of text into tabular form for use in downstream modeling. Its modification is notable as the large language model tokenizer with an ability to combine both tokens that encode single characters (including single digits or single punctuation marks) and those that encode whole words (even the longest compound words). This modification, in the first step, assumes all unique characters to be an initial set of 1-character long n-grams (i.e. initial "tokens"). Then, successively, the most frequent pair of adjacent characters is merged into a new, 2-character long n-gram and all instances of the pair are replaced by this new token. This is repeated until a vocabulary of prescribed size is obtained. Note that new words can always be constructed from final vocabulary tokens and initial-set characters. This algorithmic approach has been extended from spoken language to sign language in recent years.

All the unique tokens found in a corpus are listed in a token vocabulary, the size of which, in the case of GPT-3.5 and GPT-4, is 100256. 

![image](https://github.com/user-attachments/assets/27cf64e5-42a1-470b-baee-fc5a170bb4eb)
