# Advanced Natural Language Processing
---
---
## Assignment 1

### Tejasvi Chebrolu
### 2019114005

---
---

## Question 1

> Words Chosen - laptop, camera, weak, buy, amazing, tv

### Co-Occurence Matrix with SVD

- Laptop
The top 10 words which are similar to laptop are:
    1. headphone
    2. pc
    3. home
    4. ipod
    5. ears
    6. old
    7. head
    8. long
    9. double
    10. network

- Weak
The top 10 words which are similar to Weak are:
    1. loose
    2. slightly
    3. fairly
    4. somewhat
    5. extremely
    6. faster
    7. seconds
    8. 40
    9. otherwise
    10. pearl

- Buy
The top 10 words which are similar to Buy are:
    1. need
    2. why
    3. want
    4. decided
    5. re
    6. are
    7. wanted
    8. always
    9. find
    10. do

- Amazing
The top 10 words which are similar to Amazing are:
    1. awesome
    2. die
    3. gives
    4. true
    5. fantastic
    6. important
    7. annoying
    8. cool
    9. slightly
    10. markup

- TV
The top 10 words which are similar to TV are:
    1. off
    2. right
    3. first
    4. into
    5. belkin
    6. support
    7. plug
    8. phone
    9. card
    10. by

---

### CBOW

- Laptop
The top 10 words which are similar to laptop are:
    1. thatcher
    2. endemic
    3. einkconclusion
    4. carry
    5. sideload
    6. fiber
    7. coverage
    8. annoyance
    9. manuals
    10. crack

- Weak
The top 10 words which are similar to Weak are:
    1. okvery
    2. purely
    3. avoiding
    4. regretted
    5. hear
    6. sides
    7. thanwe
    8. road4
    9. elite
    10. bookmark

- Buy
The top 10 words which are similar to Buy are:
    1. remembered
    2. needs
    3. retailed
    4. neglected
    5. burger
    6. plywood
    7. that
    8. pieces
    9. googled
    10. kunu

- Amazing
The top 10 words which are similar to Amazing are:
    1. displaying
    2. printer
    3. bags
    4. nights
    5. monkey
    6. conclusion
    7. marware
    8. eyesight
    9. chosen
    10. football

- TV
The top 10 words which are similar to TV are:
    1. tricks
    2. different
    3. album
    4. t101mt
    5. superlative
    6. settings
    7. cleaned
    8. 2010after
    9. franklin
    10. tug

**Observations**

From the dataset, it can clearly be seen that most of the words belong to customer reviews.

> Frequency based model

For words like amazing, it has similar words like awesome, important which would be a good similar word. Similarly, even verbs like buy has need as the most similar word which is quite plausible. The word laptop is a great example of how, because of the type of dataset(technical), there are many matching words. Here, the words seemed to have captured both _syntactical_ and _semantic_ meaning in the word representation.

> Prediction based model

The results in the prediction based model were a bit more interesting to analyse. It is important to note here that the prediction based model only had 1 epoch and had a vocabulary of around 10,000 words whereas the frequency based model had 10 epochs and had a vocabulary of around 20,000 words. The embeddings generated in this model seemed to have captured the context very well but have failed to capture the semantics of the embedding. Hence, the words seem to look random. Here, the words seemed to have captured only the _syntactical_ meaning in the word representation.

---
---

## Question 2

### Analysis of the word camera
|Frequency Based Model | Prediction Based Model | Pre-Trained Word2Vec Embedding |
|--|--|--|
| plug | confidence | cameras |
| device | entirely | screen |
| thing | shutter | video |
| unit | 63 | screens |
| radio | 283 | microphone |
| ear | booksyou | digital |
| case | together | images |
| corner | slight | device |
| product | lyrics | window |
| problem | clunkiness | sensor |

**Observations**

Clearly, the best performing model is the pre-trained Word2Vec model. However, between the frequency based model, and the prediction based model, the frequency based model does much better. It is able to capture information so that words like plug, device, unit, product, problem, etc are similar words. The prediction based model fails and has words like 63 and 283 which is probably a number related to the type of camera. It does capture things like shutter which is quite interesting.

This is mostly because of the fact that the prediction based model could not be trained completely. As mentioned earlier, the number of epochs, and more importantly, the vocabulary size of the model was quite low because of computational issues. Increasing these for both the models would make the embeddings much more closer to the pre-trained models.

---
---

## Directory Structure

The directory structure is as follows:
```
.
├── CBOW
│   ├── embeddings.txt
│   └── Q1.ipynb
├── Report.md
└── Report.pdf
└── SVD
    ├── embeddings.txt
    └── Q1.ipynb

```
The embeddings under each model contain the model, and the notebook contains the source code for each model. The code can be run by uploading the dataset onto Google Drive and running the notebook.

---
---

## References

- [CBOW Tutorial](https://github.com/nzw0301/keras-examples/blob/master/CBoW.ipynb)
- [SVD Tutorial](https://blog.statsbot.co/singular-value-decomposition-tutorial-52c695315254?gi=703376979d4)
