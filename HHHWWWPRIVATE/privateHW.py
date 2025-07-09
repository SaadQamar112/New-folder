class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

text = "Hello world this is Python"
reverser = StringReverser(text)
print(reverser.reverse_words())