
# Amazon reviews Sentiment Analysis

In notebook I will execute a Natural Language Processing Python Project creating a Sentiment Analysis classifier with NLTK's VADER and Huggingface Roberta Transformers. The project is to classify the seniment of amazon customer reviews. 🤗  provides some great open source models for NLP: https://huggingface.co/models. We will look at the difference between model outputs from the two packages and compare the results. Seniment analysis is an important tool for data scientists to use in laguage modeling.

Steps in the notebook:
1. VADER (Valence Aware Dictionary and sEntiment Reasoner) - Bag of words approach
2. Roberta Pretrained Model from 🤗
3. Huggingface Pipeline

### Dateset used
[Amazon Fine Food Reviews](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)


## Installation

You may need to install the following:

```bash
  pip install ipywidgets
```
or in conda
```bash
  conda install -c conda-forge ipywidgets
```
    
## Demo
Compound Score
![alt text]()
* Larger scores have larger compound values as we would expect

PNP Score
![alt text]()
* Increasing scores have increasing positive values
* All scores are somehow the same neutral values
* Increasing scores hace decreasing negative values

Comparisions
![alt text](https://github.com/aryanaarav/aa_repo/blob/master/Sentiment%20Analysis/Amazonreviews/ss/Comparision.jpg)
* Shows vigorous comparisions in larger areas of interest

## Documentation

1. Check the Roberta Model on Hugging Face [Documentation](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment)

2. Also check out this research paper for reference entitled [TweetEval: Unified Benchmark and Comparative Evaluation for Tweet Classification](https://aclanthology.org/2020.findings-emnlp.148/)
