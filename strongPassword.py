#!/bin/python3

# Complete the minimumNumber function below.

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    score = []
    for i in password:
        if i in numbers:
            if 'numbers' not in score:
                score.append('numbers')
        elif i in lower_case:
            if 'lower_case' not in score:
                    score.append('lower_case')
        elif i in upper_case:
            if 'upper_case' not in score:
                score.append('upper_case')
        elif i in special_characters:
            if 'special_characters' not in score:
                score.append('special_characters')
    return max(4-len(score), 6-len(password))

n = int(input())

password = input()

print(minimumNumber(n, password))
