import pickle

responses_file = open('responses.pkl', 'rb')
responses = pickle.load(responses_file)
responses_file.close()


while True:
    responses[input("Search Term: ")] = input("Output string: ")

    output = open('responses.pkl', 'wb')
    pickle.dump(responses, output)
    output.close()
