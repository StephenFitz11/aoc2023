import re
from Solution import Solution
from inputs.two import day_two_test_inputs, day_two_inputs


class DayTwo(Solution):
    def __init__(self, inputs, test_inputs, env):
        super().__init__(inputs, test_inputs, env)
        self.MAX_RED_CUBES = 12
        self.MAX_GREEN_CUBES = 13
        self.MAX_BLUE_CUBES = 14

    def is_possible(self, game):
        game_count = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        rounds = re.search(r'(?<=: ).*', game).group().split(';')

        for roundx in rounds: 
            roundx = roundx.strip().split(',')
            for hand in roundx:
                game_count = {
                    'red': 0,
                    'green': 0,
                    'blue': 0
                }
                hand = hand.strip().split(' ')
                game_count[hand[1]] += int(hand[0])
                
                if game_count['blue'] > self.MAX_BLUE_CUBES:
                    return False
                if game_count['green'] > self.MAX_GREEN_CUBES:
                    return False
                if game_count['red'] > self.MAX_RED_CUBES:
                    return False
                
        return True
    
    def find_power(self, game):
        rounds = re.search(r'(?<=: ).*', game).group().split(';')

        game_count = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for roundx in rounds: 
            roundx = roundx.strip().split(',')
            for hand in roundx:
                hand = hand.strip().split(' ')

                if game_count[hand[1]] < int(hand[0]):
                    game_count[hand[1]] = int(hand[0])

        return game_count['blue'] * game_count['green'] * game_count['red']


    def solve_part_one(self):
        answer = 0

        for game in self.inputs:
            if self.is_possible(game):
                game_number = re.search(r'(\d+)\s*:', game).group(1)
                answer += int(game_number)
                
        print("Answer: ", answer)
        

    def solve_part_two(self):
        answer = 0
        for game in self.inputs:
            answer += self.find_power(game)

        print("Answer: ", answer)



# env = 'test'
env = 'solve'
day_two = DayTwo(day_two_inputs, day_two_test_inputs, env)
day_two.solve_part_one()
day_two.solve_part_two()