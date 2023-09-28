#read text file
#create dictionary
## keys are individual words
## values are num times each word appears
#'the':128


read_file= open('sometext.txt', 'r')

textdict={}

textcounter=1

read=read_file.read()
lower=read.lower()
strip=lower.strip()
words= lower.split()
word_list=[]
for word in words:
  word_list.append(word.strip()) 

#print(word_list) 
   

for text in word_list:
    if text == textdict:
         textdict[text]=textcounter+1
    else:
        textdict[text]=textcounter
       

print(textdict)

read_file.close()