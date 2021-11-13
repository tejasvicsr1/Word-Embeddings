from icecream import ic
import os
import pandas as pd
from collections import Counter

data_train = pd.read_csv('swb-train.csv')
data_train['transcript'] = data_train['transcript'] + " ."

if not os.path.exists('swb/train'):
    os.makedirs('swb/train')
for i in range(0, data_train.shape[0]):
    try:
        text = "\n".join(data_train['transcript'][i:i+6].tolist())
        fp = open("swb/train/"+str(i)+".txt","w")
        fp.write(text)
        fp.close()
    except:
        pass

data_dev = pd.read_csv('swb-dev.csv')
data_dev['transcript'] = data_train['transcript'] + " ."

if not os.path.exists('swb/dev'):
    os.makedirs('swb/dev')
for i in range(0, data_train.shape[0]):
    try:
        text = "\n".join(data_train['transcript'][i:i+6].tolist())
        fp = open("swb/dev/"+str(i)+".txt","w")
        fp.write(text)
        fp.close()
    except:
        pass

texts = " ".join(data_train['transcript'].tolist())
words = texts.split(" ")
print("Number of tokens in Training data = ",len(words))
dictionary = Counter(words)
print("Size of Vocab",len(dictionary))
sorted_vocab = ["<S>","</S>","<UNK>"]
sorted_vocab.extend([pair[0] for pair in dictionary.most_common()])
text = "\n".join(sorted_vocab)
fp = open("swb/vocab.txt","w")
fp.write(text)
fp.close()
