def get_shortest_word(str):
    array = list()
    word = ""
    arrayoflen = list()
    length = 0
    for letter in str:
        if letter == " ":
            array.append(word)
            arrayoflen.append(length)
            word = ""
            length = 0
        else:
            word += letter
            length += 1
    array.append(word)
    arrayoflen.append(length)
    i = 0
    p = arrayoflen[0]
    wordnumber = 0
    for element in arrayoflen:
        if (p < arrayoflen[i]):
            p = arrayoflen[i]
            wordnumber = i
        i += 1
    return(array[wordnumber])

str = "Python is simple and effective!"
print(str)
print(get_shortest_word(str))
strone = "Any pythonista like namespaces a lot."
print(strone)
print(get_shortest_word(strone))