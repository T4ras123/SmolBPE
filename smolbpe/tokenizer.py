import regex as re
import argparse 
import json


class GPT4Tokenizer():
    def __init__(self, output='vocab.json', special_tokens=None, pattern=r"""'(?i:[sdmt]|ll|ve|re)|[^\r\n\p{L}\p{N}]?+\p{L}+|\p{N}{1,3}| ?[^\s\p{L}\p{N}]++[\r\n]*|\s*[\r\n]|\s+(?!\S)|\s+"""):
        self.vocab = {idx : bytes([idx]) for idx in range(256)}
        self.merges = dict()
        self.pattern = pattern
        self.splitby = re.compile(self.pattern)
        self.output_file = output
        self.special_tokens = special_tokens if special_tokens else []
        self.special_token_ids = {}
        for i, token in enumerate(self.special_tokens):
            token_id = 256 + i
            self.vocab[token_id] = token.encode('utf-8')
            self.merges[(token_id, token_id)] = token_id
            self.special_token_ids[token] = token_id


    def train(self, text, vocab_size):
 
        assert vocab_size > len(self.vocab), "Vocab size must be greater than the number of tokens in the vocab"
        num_merges = vocab_size - len(self.vocab)
        text_splitted = re.findall(self.splitby, text)
        ids = [list(self.encode(chunk)) for chunk in text_splitted]
        vocab_len = max(self.vocab.keys()) + 1
        for i in range(num_merges):
            stats = {}
            for _ in ids:
                self.get_pairs(_, stats)
            if not stats:
                print(f"No more pairs to merge at iteration {i}. Stopping early.")
                break
            pair = max(stats, key=stats.get)
            idx = vocab_len + i
            self.merges[pair] = idx
            self.vocab[idx] = self.vocab[pair[0]] + self.vocab[pair[1]]
            ids = [self.merge(chunk_ids, pair, idx) for chunk_ids in ids]
        self.save_vocab_and_merges(self.output_file)

    
    def encode(self, text):
        tokens = []
        i = 0
        while i < len(text):
            matched = False
            for token in self.special_tokens:
                if text.startswith(token, i):
                    token_id = self.special_token_ids[token]
                    tokens.append(token_id)
                    i += len(token)
                    matched = True
                    break
            if not matched:
                next_positions = [text.find(st, i) for st in self.special_tokens if text.find(st, i) != -1]
                next_special = min(next_positions) if next_positions else len(text)
                substring = text[i:next_special]
                ids = list(substring.encode('utf-8'))
                ids = self.apply_bpe(ids)
                tokens.extend(ids)
                i = next_special
        return tokens
    
    
    def apply_bpe(self, ids):
        while True:
            pairs = self.get_pairs(ids)
            mergeable_pairs = {p: self.merges[p] for p in pairs if p in self.merges}

            if not mergeable_pairs:
                break

            pair = min(mergeable_pairs, key=self.merges.get)
            ids = self.merge(ids, pair, self.merges[pair])

        return ids
        
    
    def decode(self, ids):
        tokens = b"".join(self.vocab[idx] for idx in ids)
        text = tokens.decode("utf-8", errors="replace")
        return text


    def get_pairs(self, ids, counts=None):

        counts = {} if counts is None else counts
        for pair in zip(ids, ids[1:]):
            counts[pair] = counts.get(pair, 0) + 1

        return counts


    def save_vocab_and_merges(self, path):
        data = {
            'vocab': {},
            'merges': {}
        }
        # Save vocab
        for idx, byte_val in self.vocab.items():
            try:
                data['vocab'][str(idx)] = byte_val.decode('utf-8')
            except UnicodeDecodeError:
                data['vocab'][str(idx)] = byte_val.hex()
        # Save merges
        for (first, second), idx in self.merges.items():
            key = f"{first},{second}" 
            data['merges'][key] = idx
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
            
            
    def load_vocab(self, path='vocab.json'):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.vocab = {}
        for idx_str, value in data['vocab'].items():
            idx = idx_str
            self.vocab[idx] = value.encode('utf-8')
        self.merges = {}
        for pair_str, idx in data['merges'].items():
            first_str, second_str = pair_str.split(',')
            first, second = int(first_str), int(second_str)
            self.merges[(first, second)] = idx
    
    
    def merge(self, ids, pair, idx):
        id = 0
        newids = []
        while id<len(ids):
            if id < len(ids)-1 and ids[id]==pair[0] and ids[id+1]==pair[1]:
                newids.append(idx)
                id += 2
            else:
                newids.append(ids[id])
                id+=1
        return newids


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text', type=str, help='Text to train tokenizer on')
    parser.add_argument('-v', '--vocab_size', type=int, help='Vocab size for tokenizer')
    parser.add_argument('-o', '--output', default='vocab.json', type=str, help='Output path for vocab and merges')
    parser.add_argument('-p', '--pattern', type=str, default=r"""'(?i:[sdmt]|ll|ve|re)|[^\r\n\p{L}\p{N}]?+\p{L}+|\p{N}{1,3}| ?[^\s\p{L}\p{N}]++[\r\n]*|\s*[\r\n]|\s+(?!\S)|\s+""", help='Regex pattern to split text')
    parser.add_argument('-s', '--special_tokens', nargs='*', default=None, help='Special tokens to add to vocab')
    args = parser.parse_args()
    
    with open(args.text, 'r') as f:
        args.text = f.read()
    print(args.special_tokens)
    tokenizer = GPT4Tokenizer(args.output, special_tokens=args.special_tokens, pattern=args.pattern)
    tokenizer.train(args.text, args.vocab_size)
    print(f"Tokenizer trained and saved to {args.output}")