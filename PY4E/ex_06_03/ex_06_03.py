def count(w):
    count = 0
    for letter in w:
        count = count + 1
    print(count)

letter = input("Enter word to be counted: ")
count(letter)
