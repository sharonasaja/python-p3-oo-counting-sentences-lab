#!/usr/bin/env python3
import re
class MyString:
    def __init__(self, value):
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("Value must be a string.")

    def is_sentence(self,):
        return self.value.endswith('.')

    def is_question(self,):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self,):
        # Split the string into sentences based on '.', '?', and '!'
        sentences = re.split(r'[.!?]', self.value)
        # Filter out any empty sentences 
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        return len(sentences)
