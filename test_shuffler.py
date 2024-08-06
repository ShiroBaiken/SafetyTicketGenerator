import random as r

from test_manipulator import QestionGetter


class TestShuffler:

    def __init__(self, manipulator):
        self.manipulator: QestionGetter = manipulator

    def get_block(self, no_of_questions):
        limit = self.manipulator.get_range()
        indexes = r.sample(range(1, limit + 1), no_of_questions)
        block = []
        for i in indexes:
            block.append(self.manipulator.retrieve_one(i))
        return list(x['question'] for x in block)
