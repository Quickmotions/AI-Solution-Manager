# Fergus Haak 11/10/21

import Levenshtein as lev
import pickle

words_to_strip = [
    'what', 'the', 'why', 'tell,' 'can', 'please', 'explain', 'how', 'does',
    'does', 'get', 'what\'s', 'who', 'whats', 'hows', 'whos', 'its', 'can',
    'a', 'it', 'has', 'its'
]


class AIHelper:
    """"Calculates similar search terms and handles user inputs"""

    def __init__(self):
        """
        user_input = temp storage for user input str,
        minimum ratio = minimum similarity to accept for response,
        min_char = cutoff char limit for small words in user input
        """
        self.user_input = ""
        self.minimum_ratio = 0.4
        self.min_char_length = 1

    def strip_input(self):
        """removes short words and restricted words"""
        full_input = self.user_input
        user_input_stripped = ""
        for word in full_input.split():
            if word not in words_to_strip and len(word) > self.min_char_length:
                user_input_stripped += word + " "
        self.user_input = user_input_stripped

    def fuzzy_search(self, user_input: str, response_manager):
        """formats user input and determines ratio % of all responses similarities"""
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

    def output_and_learn(self, sorted_responses: list, response_manager):
        """prints responses and asks user if response is correct and also accepts new answers for unknown questions"""
        attempted_index = 0
        while attempted_index < 4:
            if sorted_responses[attempted_index][1] > self.minimum_ratio:
                print(f"Helper Bot: {sorted_responses[attempted_index][0]} "
                      f"({round(sorted_responses[attempted_index][1], 2)})")
                if input("\nThis this response useful. (y/n): ").lower() == "y":
                    response_manager.update_responses_dictionary(self.user_input.lower(),
                                                                 sorted_responses[attempted_index][0])
                    return
            attempted_index += 1
        users_correct_answer = input("\nSorry, I don't know how to answer this.\n"
                                     "Enter an example answer for this question "
                                     "or press [enter] to cancel.\n>>> ")
        if users_correct_answer != "":
            response_manager.update_responses_dictionary(self.user_input.lower(), users_correct_answer)


class ResponseDictionary:
    """Handles responses and stores responses in a pkl file"""

    def __init__(self):
        """load response file"""
        responses_file = open('responses.pkl', 'rb')
        self.responses = pickle.load(responses_file)
        responses_file.close()

    def show_responses(self):
        """debug only. prints all usable responses"""
        for search_term, response_str in self.responses.items():
            print(f"{search_term} : {response_str}")

    def update_responses_dictionary(self, search_term: str, response_str: str):
        """addes a new search term and response to response dictionary"""
        self.responses[search_term] = response_str
        output = open('responses.pkl', 'wb')
        pickle.dump(self.responses, output)
        output.close()


# create objects
response_dictionary = ResponseDictionary()
helper_bot = AIHelper()

# testing --------------------------
# response_dictionary.show_responses()

while True:
    helper_bot.fuzzy_search(input('\nAsk a question: '), response_dictionary)
