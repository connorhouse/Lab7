# Exercise 8.9 (in the Chapter) - Now that you have seen the details of the railDecrypt function you can make it smarter in two ways:
    # You do not need to check cases where the number of rails is greater than the message length divided by two. Can you explain why?
    # - After a while it starts to rebuild the one rail decrypt that it started with then no longer works which makes the encryption easier to crack.

    # You only need to check cases where the number of rails evenly divides the total message length. Can you explain why?
    # - in the odd numbers the spaces would be moved and some could be placed next to each other and would leave you with a large grouping of letters which makes the encryption more difficult to crack.


# Exercise 8.14 (in the Chapter) - Write a function wordPop that accepts a text and a length N and returns the list of all the words that are N letters long, sorted by their length.
def wordPop(text, n):
    nwords = []
    words = text.split()
    for word in words:
        if (len(word) == n):
            nwords.append(word)
    return (nwords)

w = 'This is a test for a length of words of different sizes'
print(wordPop(w.lower(), 5))

# Exercise 8.18 - Write a regular expression pattern to match all words ending in ing.
import re
expression = input("enter an expression: ")
print(re.findall(r'\b(\w+ing)\b',expression))


# Exercise 8.20 - Write a regular expression pattern to match all words beginning and ending with the letter a.
import re
expression = input("enter an expression: ")
print(re.findall(r'\b(A+\w+a)\b',expression))