#3
print("Program number 3")


int_rate = 0.063 #6.3%
initial_debt = 21.46 #21.46 billion in 2018
years = 2018
add = 0

while years < 2035:
     calc = initial_debt * int_rate
     add = initial_debt + calc
     years = years + 1
     initial_debt = add
     print('In', years, "the debt will increase by", round(add,2), "billion")


