class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        reversed_text = ' '.join(self.text.split()[::-1]) #sequence[start:stop:step] step=how the sequence will traversed
        return reversed_text

text = input("Enter a string: ")
reverser = StringReverser(text)
print("Reversed string:", reverser.reverse_words())
