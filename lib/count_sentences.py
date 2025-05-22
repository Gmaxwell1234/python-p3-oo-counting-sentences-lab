class MyString:
    def __init__(self, value=""):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        import re
        # Look for sentence-ending punctuation followed by space or end of string
        sentences = re.split(r'[.!?]+', self.value)
        # Filter out empty strings (can happen if punctuation is at the end)
        filtered = [s.strip() for s in sentences if s.strip()]
        return len(filtered)
