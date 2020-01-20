import re
import string
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import pandas as pd
stop_words = set(stopwords.words('english'))

# count frequency 
def frequency(word_list, threshold):
    wordfreq = {}
    total = len(word_list)

    for w in word_list:
        if w not in wordfreq:
            if threshold:
                val = word_list.count(w)/total # here
                if val >= threshold[0] and val <= threshold[1]:
                    wordfreq[w] = word_list.count(w)
            else:
                wordfreq[w] = word_list.count(w)

    
    wordfreq = {k: v for k, v in sorted(wordfreq.items(), key=lambda item: item[1], reverse=True)}
    return wordfreq

def preprocess(sent, type):
    # remove punctuation
    result = sent.translate(str.maketrans('', '', string.punctuation))
    result = result.replace("'","")
    result = result.strip()

    # tokenization
    tokens = word_tokenize(result)
    tokens = [i for i in tokens if not i in stop_words]
    
    if type == 'lem':
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(word) for word in tokens]
    else:
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(word) for word in tokens]
    
    return tokens
        



def closeness_search(data, preprocess_type='stem', thld=False):
    # lowering
    result = data.lower()

    # removing numbers
    result = re.sub(r"\d+", "", result)

    #breaking into sentences
    sentences = sent_tokenize(result)


    result = preprocess(result, type=preprocess_type)
    wordfreq = frequency(result, threshold=thld)
    print(wordfreq)

    prev_words = []
    nxt_words = []
    freqs = []
    for key in wordfreq:
        exist = ""
        for sent in sentences:
            if key in sent:
                exist += sent + " "
        
        wordfreq = frequency(preprocess(exist, type=preprocess_type), threshold=False)
        for word, val in wordfreq.items():
            if word == key:
                continue
            else:
                prev_words.append(key)
                nxt_words.append(word)
                freqs.append(val)


    data = {'most_freq': prev_words, 'sub_most_freq': nxt_words, 'frequency': freqs}
    df = pd.DataFrame(data, index=None)

    return df