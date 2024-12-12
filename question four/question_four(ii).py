def count_word_frequencies(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # an empty dictionary
    word_frequencies = {}
    
    #the words
    for word in words:
        # Check if the word is already in the dictionary
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1
    return word_frequencies

# setence
sentence = "python exam"
print(count_word_frequencies(sentence))
    

