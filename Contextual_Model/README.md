# Advanced Natural Language Processing
---
---
## Assignment 2

### Tejasvi Chebrolu
### 2019114005

---
---

## Implementing Embedding from Language Model

For implementing ``ELMO`` from scratch we need to understand the architecture of the language model. The architecture of the language model is the same as the TensorFlow implementation of the pretrained biLM used to compute ELMo representations. The model was further trained on the Switchboard dataset.

To prepare the dataset run the command:
```bash
python trial.py
cp -r swb/ bilm-tf
```

The command to fine-tune the model further is as follows:
```bash
python bin/run_test.py --test_prefix='swb/dev/*' --vocab_file 'swb/vocab.txt' --save_dir='swb/checkpoint'
```

To run the predictions and get the embeddings, run the Jupyter notebook ```Assignment_2.ipynb```.

---

## Calculating Cosine and Euclidean Distances

> The Euclidean distance is calculated as follows:
```python
def euclidean(a, b):
  return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(len(a))))
```
> The Cosine distance is calculated as follows:
```python
from sklearn.metrics.pairwise import cosine_similarity
def cosine(a, b):
  return cosine_similarity([a], [b])[0][0]
```

---

## Directory Structure

```
..
├── Assignment_2.ipynb
├── bilm-tf
│   ├── bilm
│   ├── bilm.egg-info
│   ├── bin
│   ├── build
│   ├── dist
│   ├── Dockerfile
│   ├── LICENSE
│   ├── README.md
│   ├── run_tests_before_shell.sh
│   ├── setup.py
│   ├── tests
│   ├── usage_cached.py
│   ├── usage_character.py
│   └── usage_token.py
├── embeddings.txt
├── README.md
├── Report.md
├── Report.pdf
├── swb-dev.csv
├── swb-test.csv
├── swb-train.csv
└── trial.py

```
---
---