import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')))

# Import the text variable from the text module
from text import text

tokenized_text = text.split()

dictionary = list(set(tokenized_text))

wtoi = {w:i for i,w in enumerate(dictionary)}
itow = {i:w for w, i in wtoi.items()}

encode = lambda text: [wtoi[i] for i in text.split()]
decode = lambda ids: " ".join(itow[i] for i in ids)

print(decode(encode("Introduction to Unicode")))
