passage = input("enter a passage : ")
passage = passage.lower()  # make everything lowercase
words = passage.split()    # split into words (spaces, newlines, etc.)

count = {}  # empty dictionary to count letters

for word in words:
    first_letter = word[0]   # get first letter of each word
    if first_letter.isalpha():  # only count if it's a letter (ignore numbers/punctuation)
        if first_letter in count:
            count[first_letter] += 1
        else:
            count[first_letter] = 1

    # Find the letter with the highest count
most_frequent = max(count, key=count.get)

print(most_frequent)
print(count)