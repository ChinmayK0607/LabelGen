
from transformers import pipeline
import os 
folder_path = "images\Test"
def img2text(url):
    img_text = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")
    text = img_text(url)
    return text

def get_caption(data):
    return data[0]['generated_text']

file = open("embeddings.txt",'a')
for filename in os.listdir(folder_path):
    
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
       
        file_path = os.path.join(folder_path, filename)
        get_t = img2text(file_path)
        file.write(get_caption(get_t) + '\n')
f = open("embeddings.txt",'r')
for t in f:
    print(t)
#print(get_text)