from text import text

tokenized_text = text.split()

dictionary = list(set(tokenized_text))

wtoi = {w:i for i,w in enumerate(dictionary)}
itow = {i:w for w, i in wtoi.items()}

encode = lambda text: [wtoi[i] for i in text.split()]
decode = lambda ids: " ".join(itow[i] for i in ids)

print(decode(encode("Introduction to Unicode")))