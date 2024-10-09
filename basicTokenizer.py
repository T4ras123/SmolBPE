
class BasicTokenizer():


    def __init__(self):
        self.vocab = {idx : bytes([idx]) for idx in range(256)}
        self.merges = dict()
        self.special_characters = []
        self.decoded_text = "Pop"
        self.encoded_text = []


    def train(self, text, vocab_size, verbose = False):
        tokens = self.tokenize(text)
        steps = vocab_size - 256
        for _ in range(steps):
            bigrams = self.get_bigrams(tokens)
            pair = max(bigrams, key=bigrams.get)
            idx = 256 + _
            tokens = self.merge(tokens, pair, idx)
            self.merges[pair] = idx

        for (p1,p2), idx in self.merges.items():
            self.vocab[idx] = self.vocab[p1]+self.vocab[p2]
        return tokens


    def encode(self, text):
        tokens = self.tokenize(text)
        while len(tokens)>=2:
            bigrams = self.get_bigrams(tokens)
            pair = min(bigrams, key = lambda p: bigrams.get(p, float("inf")))
            if pair not in self.merges:
                break
            idx = self.merges[pair]
            tokens = self.merge(tokens, pair, idx)
        self.encoded_text = tokens
        return tokens


    def decode(self, ids):
        tokens = b"".join(self.vocab[idx] for idx in ids)
        text = tokens.decode("utf-8", errors="replace")
        self.decoded_text = text
        return text


    def get_bigrams(self, tokens):
        bigrams = {}
        for pair in zip(tokens, tokens[1:]):
            bigrams[pair] = bigrams.get(pair, 0) + 1
        return bigrams


    def merge(self, text, pair, idx):
        newids = []
        id = 0 
        while id<len(text):
            if id<len(text)-1 and text[id]==pair[0] and text[id+1]==pair[1]:
                newids.append(idx)
                id+=2
            else:
                newids.append(text[id])
                id+=1
        return newids


    def tokenize(self, text):
        tokens = text.encode("utf-8")
        tokens = list(tokens)
        return tokens


t = BasicTokenizer()

with open("taylorswift.txt", "r") as f:
    text = f.read()

t.train(text, 400)
print(t.vocab)
t.encode("Hello World Taylor Swift:    ")
t.decode([72,101,108,108,111,32,87,111,114,108,100])
print(t.encoded_text)
print(t.decoded_text)
