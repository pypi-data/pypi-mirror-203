import csv
import random


class DailyPrompt:
    # initialize the object and load the prompts from a CSV file.
    def __init__(self, prompts_file):
        self.prompts_file = prompts_file
        self.prompts = []
        with open(prompts_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.prompts.append(row[0])

    # randomly select a prompt from the list of prompts and return it to the user.
    def get_prompt(self):
        return random.choice(self.prompts)

    # allow the user to add a new prompt to the list of prompts.
    def add_prompt(self, prompt):
        self.prompts.append(prompt)

    # allow the user to remove a prompt from the list of prompts.
    def remove_prompt(self, prompt):
        self.prompts.remove(prompt)
