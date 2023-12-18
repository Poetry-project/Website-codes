# import nltk
import os
import random
from nltk.translate.bleu_score import SmoothingFunction, corpus_bleu, sentence_bleu
from generate_text import GenerateText


def bleu(ref, gen):
    """
    calculate pair wise bleu score. uses nltk implementation
    Args:
        references : a list of reference sentences
        candidates : a list of candidate(generated) sentences
    Returns:
        bleu score(float)
    """
    ref_bleu = []
    gen_bleu = []
    for l in gen:
        gen_bleu.append(l.split())
    for i, l in enumerate(ref):
        ref_bleu.append([l.split()])
    cc = SmoothingFunction()
    score_bleu = corpus_bleu(
        ref_bleu, gen_bleu, weights=(0, 1, 0, 0), smoothing_function=cc.method4
    )    
    return score_bleu


# save tokens to file, one dialog per line
def save_doc(data, filename):
    # data = '\n'.join(lines)
    file = open(filename, "w", encoding="utf-8-sig")
    file.write(data)
    file.close()


# save tokens to file, one dialog per line
def append_doc(data, filename):
    # data = '\n'.join(lines)
    file = open(filename, "a", encoding="utf-8-sig")
    file.write(data)
    file.write("\n=============================================\n")
    file.close()


# load doc into memory
def load_doc(filename):
    # open the file as read only
    file = open(filename, "r", encoding="utf-8-sig")
    # read all text
    text = file.read()
    # close the file
    file.close()
    return text

# res_list = []
# dirPath = r"dataset_text_clean"
# path = os.getcwd()
# dir_path = os.path.join(path, dirPath)
# subDir = ""
# # list to store files
# # Iterate directory
# for file_path in os.listdir(dir_path):
#     subDir = file_path
#     for file in os.listdir(os.path.join(dir_path, file_path)):
#         # check if current file_path is a file
#         if os.path.isfile(os.path.join(dir_path, file_path, file)):
#             # add filename to list
#             res_list.append(os.path.join(dir_path, file_path, file))

# print(len(res_list))
# # print(res)

# # pick a random element from a list of strings.
# item = random.choice(res_list)
# print(item)


# # load document
# text = load_doc(item)

import pandas as pd
data = pd.read_csv('dataset/new_dataset_clean.csv', low_memory=False)
df = data.copy()

# Select one row randomly using sample()
# without give any parameters``

# row = df.sample().to_dict()
row = df.sample()
row = list(row.values[0])
# print (row)
# print (len(row))

# print (row.values)
# print(row['poet_name'])
# print(row[1])
# print(row[2])
# print(row[7])
# # load document
# text =str(list(row["poem_text_clean"])[0])
text = row[7]
# print(text)

# title = str(list(row["poet_name"])[0])
title = row[2]
# print(title)
# length of text is the number of characters in it
# file_name = os.path.basename(item)
# print(file_path)

path = "output_test"
# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:
   # Create a new directory because it does not exist
   os.makedirs(path)
   print("The new directory is created!")
# save_doc(text, file_name)
append_doc(text, os.path.join( path , title +".txt"))


phrase = title
print ( len(phrase) + len(text))
# phrase = str(text).split()[:2]
# print(phrase)
# phrase = " ".join(phrase)
# seqLength = len(text) - len(phrase) + 1
seqLength = len (text)
print(seqLength)
obj = GenerateText()
message = obj.predict(seed_text= phrase, seq_length= seqLength)

# save_doc(message, "output_test\\" +  title + "_predict.txt")
append_doc(message,  os.path.join( path , title +".txt"))

print(f"Length of text orignal: {len(text)} characters")
append_doc(f"Length of text orignal: {len(text)} characters", os.path.join( path , title +".txt"))
print(text[:200])
append_doc(text[:200],  os.path.join( path , title +".txt"))

print(f"Length of text generator: {len(message)} characters")
print (message[:200])
append_doc(f"Length of text generator: {len(message)} characters", os.path.join( path , title +".txt"))
append_doc(message[:200], os.path.join( path , title +".txt"))
ref = phrase + text
scoreBleu = bleu(ref , message)
print (scoreBleu)

append_doc(str(scoreBleu), os.path.join( path , title +".txt"))