import nltk
import pprint

#nltk.data.path.append('./nltk_data/')

tokenizer = None
tagger = None

def init_nltk():
    global tokenizer
    global tagger
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|[^\w\s]+')
    tagger = nltk.UnigramTagger(nltk.corpus.brown.tagged_sents())

def tag(text):
    global tokenizer
    global tagger
    if not tokenizer:
        init_nltk()
    tokenized = tokenizer.tokenize(text)
    tagged = tagger.tag(tokenized)
    tagged.sort(lambda x,y:cmp(x[1],y[1]))
    return tagged

def process(text):
    tagged = tag(text)    
    l = list(set(tagged))
    l.sort(lambda x,y:cmp(x[1],y[1]))
    #pprint.pprint(l)
    return l
