import pickle

response = {
    'inputs': "In computer science, the general meaning of input is to provide or give something to the computer, in"
              " other words, when a computer or device is receiving a command or signal from outer sources, the event"
              " is referred to as input to the device. ",
    'data': "Data are individual facts, statistics, or items of information, often numeric."
            " We store it in a secure server",
    'search': "You can search all kinds of queries using this AI helper",
    'hello': "Hello Human. I am an AI designed to answer your queries",
    'Help': "I can help with many issues, try being more specific.",
    'password': "If you forget your password, you can reset it at (http://datasec/passwords/reset.com)",
    'gdpr': "The General Data Protection Regulation (EU) 2016/679 (GDPR) is a regulation in EU law on data protection"
            " and privacy in the European Union (EU) and the European Economic Area (EEA). It also addresses the "
            "transfer of personal data outside the EU and EEA areas. The GDPR's primary aim is to enhance individuals' "
            "control and rights over their personal data and to simplify the regulatory environment for international "
            "business. Superseding the Data Protection Directive 95/46/EC, the regulation contains provisions and"
            " requirements related to the processing of personal data of individuals (formally called data subjects"
            " in the GDPR) who are located in the EEA, and applies to any enterprise—regardless of its location and"
            " the data subjects' citizenship or residence—that is processing the personal information of individuals"
            " inside the EEA. ",
    'Human': "This is an AI helper. To speak to a real human please call 072 2923 001",
    'Network': "Network science is an academic field which studies complex networks such as telecommunication networks, "
               "computer networks, biological networks, cognitive and semantic networks, and social networks, considering "
               "distinct elements or actors represented by nodes (or vertices) and the connections between the elements or"
               " actors as links (or edges).",
    'digital marketing': "Digital marketing is the component of marketing that utilizes internet and online based "
                         "digital technologies such as desktop computers, mobile phones and other digital media and "
                         "platforms to promote products and services",
    'time': f"The current time is: {datetime.now()}",
    'questions': "I am designed to answer questions, try asking me one",
    'data usage': "Data from customers is never used out side of our internal program. The data is always encrypted.",
    'learning': "Our AI is constantly learning. By searching new queries you are contributing.",
    'develop': "Our developers are constantly evaluating our current code and attempting to improve and optimise it.",

}
# reset data
output = open('responses.pkl', 'wb')
pickle.dump(response, output)
output.close()