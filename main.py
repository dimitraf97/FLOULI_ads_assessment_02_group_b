"""
Multiplication Table
"""
# Provide your solution here

def print_multiplication_table(number:int, rownumber:int):
    if number <=0:
        print("Number and rows cannot be less than one.Please use a positive number.")
    elif rownumber <=0:
        print("Number and rows cannot be less than one.Please use a positive number.")
    else:
        for i in range(1, rownumber+1):
            print(f"{i} * {number} = {i*number}.")
print_multiplication_table(6,3)
print_multiplication_table(10,2)
print_multiplication_table(-10,2)
print_multiplication_table(2,-2)

"""
Palindromes
"""

# Provide your solution here
def is_palindrome():
    word=str(input("Please type in a word: "))
    for i in range(len(word)):
        if (word[i]) == (word[-i]):
            print(True)
        else:
            print(False)
is_palindrome()
"""
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

