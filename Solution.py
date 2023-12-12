class Solution:
    def __init__(self, inputs, test_inputs, env):
        self.inputs = inputs if env == 'solve' else test_inputs
        self.answer = None

    def print_answer(self):
        print(self.answer)
