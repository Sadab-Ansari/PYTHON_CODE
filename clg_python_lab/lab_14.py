class StringReverser:
    def reverse_word(self, input_string):
        word = input_string.split()
        reverse_word = word [::-1]
        reverse_string=' '.join(reverse_word)
        return reverse_string

reverser =StringReverser()
input_string=input("Enter a string:")
output_string=reverser.reverse_word(input_string)
print(output_string)