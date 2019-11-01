# from https://github.com/paubric/python-sirajnet
from textblob import Word
import random
import argparse

def make_mine(yours, swap_rate):
    mine = []
    for string_word in yours:
        word_object = Word(string_word)
        if random.randint(0, swap_rate - 1) == 0:
            meaning_count = len(word_object.synsets)
            if meaning_count > 0:
                meaning_selected = random.randint(0, meaning_count - 1)
                lemmas = word_object.synsets[meaning_selected].lemmas()
                synonym_count = len(lemmas)
                mine += [lemmas[random.randint(0, synonym_count - 1)].name()]
            else:
                mine += [string_word]
        else:
            mine += [string_word]

    return ' '.join(mine)

parser = argparse.ArgumentParser()
parser.add_argument("--text", help="your original text", type=str, default="SaaS has dramatically lowered the intrinsic total cost of ownership for adopting software, solved scaling challenges and taken away the burden of issues with local hardware. ")
parser.add_argument("--file", help="path to text file containing text", type=str, default=None)
parser.add_argument("--chance", help="one in N swap chance", type=int, default=5)
args = parser.parse_args()

if args.file is None:
    your_text = args.text.split()
    my_text = make_mine(your_text, args.chance)
    print(my_text)
else:
    with open(args.file, 'r') as f:
        for line in f:
            your_text = line.strip().split()
            my_text = make_mine(your_text, args.chance)
            print(my_text)