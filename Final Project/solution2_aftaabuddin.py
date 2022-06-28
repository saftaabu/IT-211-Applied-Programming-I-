#2
print("Program number: 2")

def long_words(n, filename):
    print('Opening file words.txt')
    with open(filename, 'r') as infile:
            words = infile.read().split()
    word_len = []
  #  txt = filename.split(" ")
    for x in words:
        if len(x) >= n:
            word_len.append(x)
    return word_len 	
print("The words with more than 20 characters are ", long_words(20, 'words.txt'))
