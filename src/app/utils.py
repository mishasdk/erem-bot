from random import randint


class Utils:
    @staticmethod
    def choose_random(data):
        return data[randint(0, len(data) - 1)]

    @staticmethod
    def to_markdown(text):
        chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
        result = ""
        for ch in text:
            if ch in chars:
                result += '\\' + ch
            else:
                result += ch
        return result
