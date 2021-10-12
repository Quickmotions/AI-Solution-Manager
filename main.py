# Fergus Haak 11/10/21

import Levenshtein as lev
import pickle

words_to_strip = [
    'what',
    'the',
    'why',
    'tell,'
    'can',
    'please',
    'explain',
    'how',
    'does',
    'does',
    'get',
    'what\'s',
    'who',
    'whats',
    'hows',
    'whos',
    'its',
    'can',
]


class AIHelper:
    """"Calculates similar search terms and handles user inputs"""
    def __init__(self):
        self.user_input = ""
        self.minimum_ratio = 0.3

    def strip_input(self):
        full_input = self.user_input
        user_input_stripped = ""
        for word in full_input.split():
            if word not in words_to_strip and len(word) > 2:
                user_input_stripped += word + " "
        self.user_input = user_input_stripped

    def fuzzy_search(self, user_input, response_manager):
        self.user_input = user_input
        self.strip_input()
        responses_ratios = []

        index = 0
        for fuzzy_term, output in response_manager.responses.items():
            ratio = lev.ratio(user_input.lower(), fuzzy_term.lower())
            responses_ratios.append([output, ratio])
            index += 1

        self.output_and_learn(sorted(responses_ratios, key=lambda x: x[1], reverse=True),
                              response_manager)

    def output_and_learn(self, sorted_responses, response_manager):
        attempted_index = 0
        while attempted_index < 4:
            if sorted_responses[attempted_index][1] > self.minimum_ratio:
                print(f"Helper Bot: {sorted_responses[attempted_index][0]} ({sorted_responses[attempted_index][1]})")
                if input("This this response useful. (y/n): ").lower() == "y":
                    response_manager.update_responses_dictionary(self.user_input,
                                                                 sorted_responses[attempted_index][0])
                    return
            attempted_index += 1
        print("Helper Bot: I don't know the answer to that, try being more specific.")


class ResponseDictionary:
    """Handles responses and stores responses in a pkl file"""
    def __init__(self):
        # load response file
        responses_file = open('responses.pkl', 'rb')
        self.responses = pickle.load(responses_file)
        responses_file.close()

    def show_responses(self):
        for search_term, response_str in self.responses.items():
            print(f"{search_term} : {response_str}")

    def update_responses_dictionary(self, search_term, response_str):
        self.responses[search_term] = response_str
        output = open('responses.pkl', 'wb')
        pickle.dump(self.responses, output)
        output.close()


response_dictionary = ResponseDictionary()
helper_bot = AIHelper()

# testing
response_dictionary.show_responses()

while True:
    helper_bot.fuzzy_search(input('Ask a question: '), response_dictionary)
