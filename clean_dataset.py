import re
import string
import pandas as pd

import nltk
nltk.download('stopwords')


from nltk.corpus import stopwords

data = pd.read_csv('dataset/new_dataset.csv', low_memory=False)
df = data.copy()
# df = data.iloc[:200]
#print (string.punctuation)
arabic_punctuations = '''«»`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
english_punctuations = string.punctuation
punctuations_list = arabic_punctuations + english_punctuations
print (punctuations_list)

arabic_diacritics = re.compile("""
                             ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)

print (arabic_diacritics)


stopword = set(stopwords.words('arabic'))
print( len (stopword) ,"len stop word")
#print (stopword)

# turn a doc into clean tokens
def remove_Stopword(doc):    
    # split into tokens by white space
    tokens = doc.split()    
    # filter out stop words
    tokens = [w for w in tokens if not w in stopword]
    # filter out short tokens
    tokens = [word for word in tokens if len(word) > 1]    
    #return tokens
    return  " ".join(tokens) +"\n" 

# function to clean and normalize text
def clean_text(text):
    search = ["أ","إ","آ","ة","_","-","/",".","،"," و "," يا ",'"',"ـ","'","ى","\\",'\n', '\t','&quot;','?','؟','!']
    replace = ["ا","ا","ا","ه"," "," ","","",""," و"," يا","","","","ي","",' ', ' ',' ',' ? ',' ؟ ',' ! ']

    p_tashkeel = re.compile(r'[\u0617-\u061A\u064B-\u0652]')
    text = re.sub(p_tashkeel,"", text)
    p_longation = re.compile(r'(.)\1+')
    subst = r"\1\1"
    text = re.sub(p_longation, subst, text)
    #for remove stopword arabic
    text = remove_Stopword(text)
    
    text = text.replace('وو', 'و')
    text = text.replace('يي', 'ي')
    text = text.replace('اا', 'ا')

    for i in range(0, len(search)):
       #print (search[i], replace[i])
        text = text.replace(search[i], replace[i])
    text = text.strip()
    return text



def remove_punctuations(text):
    translator = str.maketrans('', '', punctuations_list)
    return text.translate(translator)

def normalize_arabic(text):
    text = re.sub("[إأآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "ء", text)
    text = re.sub("ئ", "ء", text)
    text = re.sub("ة", "ه", text)
    text = re.sub("گ", "ك", text)
    return text

def remove_diacritics(text):
    text = re.sub(arabic_diacritics, '', text)
    return text

def remove_repeating_char(text):
    return re.sub(r'(.)\1+', r'\1', text)


# clean and normalize text
df["poem_text_clean"]  = df.poem_text.apply(lambda x: clean_text(x))

# remove punctuation
df.poem_text_clean  = df.poem_text_clean.apply(lambda x: remove_punctuations(x))

# remove diacritics
df.poem_text_clean  = df.poem_text_clean.apply(lambda x: remove_diacritics(x))

# remove repeating char
df.poem_text_clean  = df.poem_text_clean.apply(lambda x: remove_repeating_char(x))

# remove english letters
df.poem_text_clean = df.poem_text_clean.apply(lambda x: re.sub(r'[a-zA-Z]', '', x))

# remove a special character
df.poem_text_clean = df.poem_text_clean.apply(lambda x: re.sub(r'[_]+', '', x))

# remove english numbers
df.poem_text_clean = df.poem_text_clean.apply(lambda x: re.sub(r'/[0-9\u0621-\u064A]+/u', '', x))

# remove space
df.poem_text_clean  = df.poem_text_clean.str.replace(r'\d+','', regex=True)

df.to_csv("dataset/new_dataset_clean.csv",encoding='utf-8-sig', index=False, header=True)
print("Done")