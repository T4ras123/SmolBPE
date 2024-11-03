import sys
import os
sys.path.append(os.path.abspath('../data'))

from smolbpe.data import text

vocab = list(set(text))
stoi = {ch:i for i, ch in enumerate(vocab)} 
itos = {i:ch for ch, i in stoi.items()}

encode = lambda text: [stoi[i] for i in text]
decode = lambda idx: "".join(itos[i] for i in idx)

print(decode(encode("Hello world")))
