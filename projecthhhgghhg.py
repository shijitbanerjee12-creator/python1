class WordReverser:
   

    def __init__(self, input_string):
        
        self.input_string = input_string

    def reverse_words(self):
       
       
        words = self.input_string.split()
        
        words.reverse()
       
        reversed_string = ' '.join(words)
        
 
sentence = "Python is a powerful and versatile language"
reverser_instance = WordReverser(sentence)

reversed_sentence = reverser_instance.reverse_words()

print(f"Original string: \"{sentence}\"")
print(f"Reversed string: \"{reversed_sentence}\"")

sentence2 = "   Hello   world!  "
reverser_instance2 = WordReverser(sentence2)
reversed_sentence2 = reverser_instance2.reverse_words()
print(f"\nOriginal string: \"{sentence2}\"")
print(f"Reversed string: \"{reversed_sentence2}\"")
