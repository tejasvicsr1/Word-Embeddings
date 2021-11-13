# Word Embeddings
---
> Word embeddings are a way to represent words in a vector space. In this project, we will implement word embeddings in two ways - contextual and non-contextual. Non-Contextual embeddings are implemented in two ways - a statistical model and a neural network. The Contextual Embedding is basically __ELMo__.

## Implementing Embedding from Language Model
*All the commands should be run from the Contextual_Model directory.*

For implementing ``ELMO`` from scratch we need to understand the architecture of the language model. The architecture of the language model is the same as the TensorFlow implementation of the pretrained biLM used to compute ELMo representations. The model was further trained on the Switchboard dataset.

The command to fine-tune the model further is as follows:
```bash
python bin/run_test.py --test_prefix='swb/dev/*' --vocab_file 'swb/vocab.txt' --save_dir='swb/checkpoint'
```

To run the predictions and get the embeddings, run the Jupyter notebook ```Assignment_2.ipynb```.
The embeddings are saved in ```embeddings.txt``` and are of the form ```word vector```.
The embeddings were generated by the following code:
```python
with open('embeddings.txt', 'w') as f:
   f.write('{} {}\n'.format(len(vocabulary), len(weights[1])))
   for i in range(len(vocabulary)):
    f.write('{}'.format(vocabulary[i]))
    for weight in weights[i]:
      f.write(' {}'.format(weight))
    f.write('\n')
```
---
### PreProcessing

The data was preprocessed in the file ```trial.py```. The training data was randomly split into many training files, each containing one slice of the data. Each file contains pre-tokenized and white space separated text, one sentence per line. White space separated full stops were also added. The training required multiple files with one text sentence per line, we created 20K training files by writing 6 sentences per file. The vocabulary file is a text file with one token per line. It must also include the special tokens ```<S>```, ```</S>``` and ```<UNK>``` (case sensitive) in the file. This was also done.

---
### Hyperparameters

- ```batch_size```: The batch size for the training was set to 128.
- ```num_epochs```: The number of epochs was set to 10.
- ```vocabulary```: The vocabular was set to 19558.
- ```embedding_size```: The embedding size was set to 1024.
- ```activation_function```: The activation function was set to ```relu```.

---

## Implementing Non-Contextual Embeddings
---
### Observations

From the dataset, it can clearly be seen that most of the words belong to customer reviews.

> Frequency based model

For words like amazing, it has similar words like awesome, important which would be a good similar word. Similarly, even verbs like buy has need as the most similar word which is quite plausible. The word laptop is a great example of how, because of the type of dataset(technical), there are many matching words. Here, the words seemed to have captured both _syntactical_ and _semantic_ meaning in the word representation.

> Prediction based model

The results in the prediction based model were a bit more interesting to analyse. It is important to note here that the prediction based model only had 1 epoch and had a vocabulary of around 10,000 words whereas the frequency based model had 10 epochs and had a vocabulary of around 20,000 words. The embeddings generated in this model seemed to have captured the context very well but have failed to capture the semantics of the embedding. Hence, the words seem to look random. Here, the words seemed to have captured only the _syntactical_ meaning in the word representation.

---
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

### Observations

Clearly, the best performing model is the pre-trained Word2Vec model. However, between the frequency based model, and the prediction based model, the frequency based model does much better. It is able to capture information so that words like plug, device, unit, product, problem, etc are similar words. The prediction based model fails and has words like 63 and 283 which is probably a number related to the type of camera. It does capture things like shutter which is quite interesting.

This is mostly because of the fact that the prediction based model could not be trained completely. As mentioned earlier, the number of epochs, and more importantly, the vocabulary size of the model was quite low because of computational issues. Increasing these for both the models would make the embeddings much more closer to the pre-trained models.

---
## References

- [CBOW Tutorial](https://github.com/nzw0301/keras-examples/blob/master/CBoW.ipynb)
- [SVD Tutorial](https://blog.statsbot.co/singular-value-decomposition-tutorial-52c695315254?gi=703376979d4)
- [Model](https://github.com/allenai/bilm-tf)
- [Blog](https://appliedmachinelearning.blog/2019/11/30/training-elmo-from-scratch-on-custom-data-set-for-generating-embeddings-tensorflow/)
- [Docs](https://tfhub.dev/google/elmo/2)