#!/usr/bin/env python
# coding: utf-8

# In[3]:


def remove_punc(input_text):
    punc_marks = ['.', ',', '"', "'", '?', '!', '@', '#', \
                  ':', ';', '_', '*', '$', '/', '{', '}', \
                  '[',']','(',')','|', '&', '\\']
    
    output_text = ""
    for char in input_text:
        if char not in punc_marks:
            output_text += char
    
    return output_text 

input_text = "The fable concerns a grasshopper (in the original, a cicada) that has spent the summer singing and dancing while the ant (or ants in some versions) worked to store up food for winter. When winter arrives, the grasshopper finds itself dying of hunger and begs the ant for food. However, the ant rebukes its idleness and tells it to dance the winter away now.[3] Versions of the fable are found in the verse collections of Babrius (140) and Avianus (34), and in several prose collections including those attributed to Syntipas and Aphthonius of Antioch. The fable's Greek original cicada is kept in the Latin and Romance translations. A variant fable, separately numbered 112 in the Perry Index,[4] features a dung beetle as the improvident insect which finds that the winter rains wash away the dung on which it feed"

output_text = remove_punc(input_text)
print(output_text)


# In[13]:


def remove_stopwords(input_text):
    stop_words=["a","the","is","of","and","for","in","to","it","as","that"]
    words=input_text.split()
    filtered_words=[]
    for word in words:
        if word.lower()  not in stop_words:
            filtered_words.append(word)
    output_text = " ".join(filtered_words)
    return output_text  
input_text = "The fable concerns a grasshopper (in the original, a cicada) that has spent the summer singing and dancing while the ant (or ants in some versions) worked to store up food for winter. When winter arrives, the grasshopper finds itself dying of hunger and begs the ant for food. However, the ant rebukes its idleness and tells it to dance the winter away now.[3] Versions of the fable are found in the verse collections of Babrius (140) and Avianus (34), and in several prose collections including those attributed to Syntipas and Aphthonius of Antioch. The fable's Greek original cicada is kept in the Latin and Romance translations. A variant fable, separately numbered 112 in the Perry Index,[4] features a dung beetle as the improvident insect which finds that the winter rains wash away the dung on which it feed"
output_text = remove_stopwords(input_text)
print(output_text)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




