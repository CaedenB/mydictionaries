#read text file
#create dictionary
## keys are individual words
## values are num times each word appears
#'the':128


read_file= open('sometext.txt', 'r')

textdict={}

read=read_file.read()
lower=read.lower()
lower = lower.replace(',','')
lower=lower.replace('.','')
lower=lower.replace("'",'')
word_list = lower.split()

#print(word_list) 
   
for text in word_list:
    if text in textdict:
         textdict[text]+=1
    else:
        textdict[text]=1
       


print(textdict)

read_file.close()