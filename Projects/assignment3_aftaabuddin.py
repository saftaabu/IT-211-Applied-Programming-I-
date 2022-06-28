import re

def fruit_list(num_words):        
    
    print("The number of words is", len(num_words))
    print("The longest word is", num_words[4])


    Fruit_sum = len(num_words[0]) + len(num_words[1]) + len(num_words[2]) + len(num_words[3]) + len(num_words[4])
    average = Fruit_sum / len(num_words)
    print("The average word length is ", average)
        
fruit_list(['apple', 'banana', 'kiwi', 'orange', 'pineapple'])



def search(word):
    #read file contents
    print('Opening file movies.txt')
    f = open('movies.txt', 'r')
    lines = f.readlines()
    newline =[]
    for line in lines:
        if re.search(word, line, re.I):
            print(line)
            newline.append(line)
    print("The were", len(newline), "matches")
    f.close()
search('war')


   
class PhonePlan:

    def print_plan(self):

        print('Mins:', self.num_mins, end=' ')

        print('Messages:', self.num_messages)

     # Add constructor
    #Your solution goes after this comment
    def __init__(self, num_mins = 0, num_messages = 0):
        self.num_mins = num_mins
        self.num_messages = num_messages
        
my_plan = PhonePlan(200, 300)

dads_plan = PhonePlan()

print('My plan...', end=' ')

my_plan.print_plan()

print('Dad\'s plan...', end=' ')

dads_plan.print_plan()


    
