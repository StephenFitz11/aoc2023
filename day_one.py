from inputs.one import day_one_inputs
import re


class Solution:
    def __init__(self, inputs, env):
        self.inputs = (
            inputs
            if env == "solve"
            else [
                "two1nine",
                "eightwothree",
                "abcone2threexyz",
                "xtwone3four",
                "4nineeightseven2",
                "zoneight234",
                "7pqrstsixteen",
            ]
        )
        self.num_map = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }
        self.pattern = r"^(one|two|three|four|five|six|seven|eight|nine)"

    def find_first_digit(self, string):
        for idx, char in enumerate(string):
            if char.isdigit():
                return char
            else:
                match = re.match(self.pattern, string[idx:])
                if match:
                    return self.num_map[match.group()]

    def find_last_digit(self, string):
        for i, val in enumerate(string):
            counter = i + 1
            char = string[-counter]
            if char.isdigit():
                return char 
            else:
                match = re.match(self.pattern, string[-counter:])
                if match:
                    return self.num_map[match.group()]

    def day_one(self):
        sum = 0
        for line in self.inputs:
            first_digit = self.find_first_digit(line)
            last_digit = self.find_last_digit(line)
            print(last_digit)
            sum = sum + int(first_digit + last_digit)

        print("Sum:", sum)
        return sum



# env = "test"
env = 'solve'
solution = Solution(day_one_inputs, env)
solution.day_one()
