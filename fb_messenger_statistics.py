import json
import numpy as np
import matplotlib.pyplot as plt
import random
import io
import datetime
import pandas as pd
import files

# Unicode values for each of the seven reactions available in messenger
thumbs_up = "\u00f0\u009f\u0091\u008d"
thumbs_down = "\u00f0\u009f\u0091\u008e"
heart = "\u00f0\u009f\u0098\u008d"
laugh = "\u00f0\u009f\u0098\u0086"
wow = "\u00f0\u009f\u0098\u00ae"
cry = "\u00f0\u009f\u0098\u00a2"
mad = "\u00f0\u009f\u0098\u00a0"


def get_num_messages(filename):
    people = []
    num_messages = []
    message_count_by_person = {}
    with open(filename) as json_file:
        data = json.load(json_file)
        group_name = data["title"]

        # Initializes message count fields for each person
        for member in data["participants"]:
            message_count_by_person[member["name"]] = 0

        # Adds to the count for each message for that sender
        for message in data["messages"]:
            message_count_by_person[message["sender_name"]] += 1


    # Displays amount of messages sent by each person
    for k, v in message_count_by_person.items():
        print(f"{k} has sent {v} messages")
        people.append(k)
        num_messages.append(v)


    # Plots number of messages
    y_pos = np.arange(len(people))
    plt.bar(y_pos, num_messages, align='center', alpha=0.5)
    plt.xticks(y_pos ,people)
    plt.ylabel('Number of Messages')
    plt.title(f'Messages per Person ({group_name})')
    plt.show()    


def get_most_reacted(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        most_reactions = 0
        most_reacted_message = {}
        reactions_by_member = {}
        group_name = data["title"]

        # Sets the reaction count for every person to zero
        for member in data['participants']:
            reactions_by_member[member['name']] =   {
                                                    "thumbup": 0,
                                                    "thumbdown": 0,
                                                    "heart": 0,
                                                    "wow": 0,
                                                    "cry": 0,
                                                    "mad": 0,
                                                    "laugh": 0
                                                    }
        
        for message in data["messages"]:
            # Check if message has any reactions
            if "reactions" in message:
                # View list of reactions and add them to each member's current count
                for react in message['reactions']:
                    person = react['actor']
                    react_type = react['reaction']

                    if react_type == thumbs_down:
                        reactions_by_member[person]['thumbdown'] += 1
                    elif react_type == thumbs_up:
                        reactions_by_member[person]['thumbup'] += 1
                    elif react_type == wow:
                        reactions_by_member[person]['wow'] += 1
                    elif react_type == mad:
                        reactions_by_member[person]['mad'] += 1
                    elif react_type == cry:
                        reactions_by_member[person]['cry'] += 1
                    elif react_type == laugh:
                        reactions_by_member[person]['laugh'] += 1
                    elif react_type == heart:
                        reactions_by_member[person]['heart'] += 1
                # Update the most reacted message (not including media)
                if 'content' in message:
                    if len(message["reactions"]) > most_reactions:
                        most_reacted_message = message
                        most_reactions = len(message['reactions'])


        # Prints most reacted message and the number of reactions it received
        print(most_reacted_message['content'])
        print(f"Number of reactions: {len(most_reacted_message['reactions'])}")


        # Prints all reactions for every member
        # for ppl in reactions_by_member:
        #     for react in reactions_by_member[ppl]:
        #         print(f'{ppl} reacted {react} {reactions_by_member[ppl][react]} times')

    return group_name, reactions_by_member

# Saddest
def plot_sad_reacts(filename):
    gp_name, reactions = get_most_reacted(filename)
    x_people = []
    y_reacts = []

    for person in reactions:
        x_people.append(person)
        y_reacts.append(reactions[person]['cry'])
        
    y_pos = np.arange(len(x_people))
    plt.bar(y_pos, y_reacts, align='center', alpha=0.5)
    plt.xticks(y_pos ,x_people)
    plt.ylabel('Number of Sad Reacts')
    plt.title(f'Sad Reacts per Person ({gp_name})')
    plt.show()

# Biggest Heart
def plot_heart_reacts(filename):
    gp_name, reactions = get_most_reacted(filename)
    x_people = []
    y_reacts = []

    for person in reactions:
        x_people.append(person)
        y_reacts.append(reactions[person]['heart'])
        
    y_pos = np.arange(len(x_people))
    plt.bar(y_pos, y_reacts, align='center', alpha=0.5)
    plt.xticks(y_pos ,x_people)
    plt.ylabel('Number of Heart Reacts')
    plt.title(f'Heart Reacts per Person ({gp_name})')
    plt.show()    

# Strongest lungs
def plot_laugh_reacts(filename):
    gp_name, reactions = get_most_reacted(filename)
    x_people = []
    y_reacts = []

    for person in reactions:
        x_people.append(person)
        y_reacts.append(reactions[person]['laugh'])
        
    y_pos = np.arange(len(x_people))
    plt.bar(y_pos, y_reacts, align='center', alpha=0.5)
    plt.xticks(y_pos ,x_people)
    plt.ylabel('Number of Laughing Reacts')
    plt.title(f'Laughing Reacts per Person ({gp_name})')
    plt.show()    

# Most agreeable
def plot_thumbup_reacts(filename):
    gp_name, reactions = get_most_reacted(filename)
    x_people = []
    y_reacts = []

    for person in reactions:
        x_people.append(person)
        y_reacts.append(reactions[person]['thumbup'])
        
    y_pos = np.arange(len(x_people))
    plt.bar(y_pos, y_reacts, align='center', alpha=0.5)
    plt.xticks(y_pos ,x_people)
    plt.ylabel('Number of Thumbs Up Reacts')
    plt.title(f'Thumbs Up Reacts per Person ({gp_name})')
    plt.show()    

# Biggest rejector
def plot_thumbdown_reacts(filename):
    gp_name, reactions = get_most_reacted(filename)
    x_people = []
    y_reacts = []

    for person in reactions:
        x_people.append(person)
        y_reacts.append(reactions[person]['thumbdown'])
        
    y_pos = np.arange(len(x_people))
    plt.bar(y_pos, y_reacts, align='center', alpha=0.5)
    plt.xticks(y_pos ,x_people)
    plt.ylabel('Number of Thumbs Down Reacts')
    plt.title(f'Thumbs Down Reacts per Person ({gp_name})')
    plt.show()    

# Most surprised
def plot_wow_reacts(filename):
    gp_name, reactions = get_most_reacted(filename)
    x_people = []
    y_reacts = []

    for person in reactions:
        x_people.append(person)
        y_reacts.append(reactions[person]['wow'])
        
    y_pos = np.arange(len(x_people))
    plt.bar(y_pos, y_reacts, align='center', alpha=0.5)
    plt.xticks(y_pos ,x_people)
    plt.ylabel('Number of Wow Reacts')
    plt.title(f'Wow Reacts per Person ({gp_name})')
    plt.show()    

# Angriest person
def plot_mad_reacts(filename):
    gp_name, reactions = get_most_reacted(filename)
    x_people = []
    y_reacts = []

    for person in reactions:
        x_people.append(person)
        y_reacts.append(reactions[person]['mad'])
        
    y_pos = np.arange(len(x_people))
    plt.bar(y_pos, y_reacts, align='center', alpha=0.5)
    plt.xticks(y_pos ,x_people)
    plt.ylabel('Number of Angry Reacts')
    plt.title(f'Angry Reacts per Person ({gp_name})')
    plt.show()    




class MarkovText:
    # person = person whose messages will be used
    # convo = filename of fb json message log
    # whatComesNext = dictionary of first two words to third word
    # real_messages = copy of real messages so that they aren't 
    #                 duplicated in the output
    def __init__(self, person, convos):
        self.person = person
        self.convos = convos
        self.whatComesNext = {}
        self.real_messages = []
        self.output = files.OUTPUT_FILE + f"original_{person}_phrases.txt"

    # Uses text to update whatComesNext dictionary
    def learn_from_text(self, whatComesNext, text):
        next_words = text[1:]
        third_word = text[2:]
        curr_and_next = zip(text, next_words, third_word)

        for first, second, third in curr_and_next:
            first_second = [first, second]
            if repr(first_second) in self.whatComesNext:
                self.whatComesNext[repr(first_second)].append(third)
            else:
                self.whatComesNext[repr(first_second)] = [third]

    # Generates the result sentences using a random next word from the whatComesNext dictionary
    def generate_text(self, whatComesNext):
        result = ['<START>', '<START>']

        while result[-1] != "<END>":
            sublist = result[-2:]
            result.append(random.choice(self.whatComesNext[repr(sublist)]))

        return result

    # Returns a list without <START> and <END> markers
    def exclude_side_markers(self, list):
        return list[2:len(list)-1]

    # Creates and formats text to be sent to learn_from_text
    def learn_from_file(self, whatComesNext, files):
        text = []
        text.append("<START>")
        text.append("<START>")
        self.add_to_list(text, files, self.person)
        text.append("<END>")

        self.learn_from_text(whatComesNext, text)

    # Adds messages from a specific person to the text
    # Adds to the list of real messages to check against created messages
    def add_to_list(self, text, files, person):
        for chat in files:
            with open(chat) as json_file:
                data = json.load(json_file)
                for message in data['messages']:
                    if message['sender_name'] == person and "content" in message: # Get specific person's messages
                    # if "content" in message: # Get all messages
                        self.real_messages.append(message['content'])
                        words = message['content'].split()
                        for word in words:
                            text.append(word)
                        text.append("\n")
                
        self.real_messages = [x.split() for x in self.real_messages]        


    # Creates original sentences from the text history of the selected person
    def produce(self):
        self.learn_from_file(self.whatComesNext, self.convos)
        result = self.generate_text(self.whatComesNext)
        sentence = []
        with io.open(self.output, 'w', encoding='utf8') as output_file:
            output_file.write(f'{self.person} Bot')
            output_file.write('\n~~~~~~~~~~~~~~~~\n')
            for word in result:
                if word != "\n":
                    sentence.append(word)
                else:
                    if sentence not in self.real_messages:
                        for phrase in sentence:
                            output_file.write(phrase + " ")
                            # print(phrase, end=" ")
                        # print('\n')
                        output_file.write('\n')
                    sentence = []
                # print(word, end=" ")


def get_frequency(filename):
    dates = {}
    with open(filename) as json_file:
        data = json.load(json_file)
        group_name = data['title']
        for message in data['messages']:
            time = message['timestamp_ms']
            day = str(datetime.datetime.fromtimestamp(time/1000.0))[0:10]
            if day not in dates:
                dates[day] = 0
            else:
                dates[day] += 1
    
    x, y = zip(*dates.items())
    x = list(reversed(list(x)))
    y = list(reversed(list(y)))

    plt.bar(x, y, align='center')
    plt.ylabel('Number of Messages')
    plt.xlabel('Date')
    plt.title(f'Messages by Date ({group_name})')
    plt.show()    


