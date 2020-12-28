from random import randint

class Utils:
    @staticmethod
    def random_answer_from_list(possible_answers):
        return possible_answers[randint(0, len(possible_answers) - 1)]
