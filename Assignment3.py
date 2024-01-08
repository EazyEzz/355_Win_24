# Queens College
# Internet and Web Technology (CSCI 355)
# Winter 2024
# Assignment 03 - Front End Technologies
# Essmer Sanchez
# Worked With Class

import OutputUtil as OU


# [1] Define a function to read in the United States data from file "us-states.csv" into a two-dimensional list..
def read_file(fileName):
    with open(fileName) as file:
        lines = file.readlines()
        states = [line.strip().split(',') for line in lines]
        return states[0], states[1:]
        # print(states)


def main():
    title = "Essmer Sanchez's US States Page"
    alignments = ["l", "l", "l", "r"]
    types = ["S", "S", "S", "N"]
    output_file = "Assignment3.html"
    headers, states = read_file('States.csv')
    for i in range(len(states)):
        name = states[i][0]
        if name == "New York":
            wikiname = "New_York_(state)"
        else:
            wikiname = name
        href = "https://en.wikipedia.org/wiki/" + wikiname.replace(' ', '_')
        a_attributes = 'href="' + href + '" target="_blank"'
        # td_cont = OU.create_element(OU.TAG_A, states[i][0], a_attributes)
        states[i][0] = OU.create_element(OU.TAG_A, name, a_attributes)
    OU.write_html_file(output_file, title, headers, types, alignments, states, True)

    # read_file('States.csv')


if __name__ == '__main__':
    main()
