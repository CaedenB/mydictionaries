#use dictionary to assign codes to each letter of alphabet
#"A":'$'

#open file and read it
#use dictonary to write encrypted version of files contents
#put to file encryted.txt

codes = {
    'A': '%', 'B': '@', 'C': '&', 'D': '$', 'E': '!', 'F': '^',
    'G': '*', 'H': '(', 'I': ')', 'J': '-', 'K': '+', 'L': '=',
    'M': '[', 'N': ']', 'O': '{', 'P': '}', 'Q': '<', 'R': '>',
    'S': '/', 'T': '\\', 'U': '|', 'V': ':', 'W': ';', 'X': ',',
    'Y': '.', 'Z': '?',
    'a': '9', 'b': '#', 'c': '1', 'd': '5', 'e': '3', 'f': '7',
    'g': '2', 'h': '8', 'i': '6', 'j': '0', 'k': '4', 'l': '!',
    'm': '@', 'n': '#', 'o': '$', 'p': '%', 'q': '^', 'r': '&',
    's': '*', 't': '(', 'u': ')', 'v': '-', 'w': '+', 'x': '=',
    'y': '[', 'z': ']'
}

in_file=open('info_security.txt','r')
outfile=open('Encrypted.txt','w')

new_text=''

read= in_file.read()
for i in read:
    if i in codes:
        new_text+=codes[i]
    else:
        new_text+=i
        
outfile.write(new_text)



