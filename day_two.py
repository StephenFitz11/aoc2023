import re
from Solution import Solution
from inputs.two import day_two_inputs


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

test_inputs = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]

# env = 'test'
env = 'solve'
day_two = DayTwo(day_two_inputs, test_inputs, env)
day_two.solve_part_one()
day_two.solve_part_two()