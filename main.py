# Fergus Haak 11/10/21

from datetime import datetime
import Levenshtein as lev
import pickle

words_to_strip = [
    'what',
    'is',
    'the',
    'a',
    'why',
    'tell,'
    'can',
    'please',
    'explain',
    'how',
    'does',
    'it',
    'do',
    'does',
    'get',
    'on',
    'my'
]


def fuzzy_search(user_input: str, response) -> float:
    # strip input

    user_input_words = user_input.lower().split(' ')
    user_input = ""
    for word in user_input_words:
        if word not in words_to_strip:
            user_input += word + " "

    # set minimum similarity %
    best_result = 0.3

    # create unknown response default
    output_str = "I'm having trouble with this question, try being more specific"

    # find most similar term in responses
    for fuzzy_term, output in response.items():
        ratio = lev.ratio(user_input.lower(), fuzzy_term.lower())
        if ratio > best_result:
            best_result = ratio
            output_str = output
    print("Helper Bot: " + output_str)
    # learn if useful
    if output_str != "I'm having trouble with this question, try being more specific":
        helpful_response_input = ""
        while helpful_response_input != "n" and helpful_response_input != "y":
            helpful_response_input = input('Was this response useful (y or n): ').lower()
        if helpful_response_input == "y":
            response[user_input] = output_str  # remove faulty final space
            # update new response file
            output = open('responses.pkl', 'wb')
            pickle.dump(response, output)
            output.close()


while True:
    # load response file
    pkl_file = open('responses.pkl', 'rb')
    response_list = pickle.load(pkl_file)
    pkl_file.close()

    fuzzy_search(input("Type query: "), response_list)
