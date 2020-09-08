from hashtable import HashTable
from linkedlist import LinkedList
import string


def repeated_word(text_string):
    ht = HashTable()
    x = text_string.split()
    count = 0
    
    for word in x:
        if word[-1] in string.ascii_letters: 
            if ht.contains(word.lower()):
                return word
            ht.add(word.lower(), count)
        else:
            if ht.contains(word[:-1].lower()):
                return word[-1]
            ht.add(word[:-1], count)
        count += 1




print(repeated_word('Once upon? nopu upon a time, there was a brave princess who'))
#print(repeated_word('It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only'))
#print(repeated_word('It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York'))
