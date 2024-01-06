# Queens College
# Internet and Web Technology (CSCI 355)
# Winter 2024
# Assignment 03 - Front End Technologies
# Essmer Sanchez
# Worked With Class

import OutputUtil as OU

# [0] Perform the usual preliminary tasks as outlined in Assignment #1
# [1] Define a function to read in the United States data from file "us-states.csv" into a two-dimensional list..
def read_file(fileName):
    with open(fileName) as file:
        lines = file.readlines()
        states = [line.strip().split(',') for line in lines]
        return states[0],states[1:]
        # print(states)


def main():
    title = "US States"
    alignments = ["l", "l", "l", "r"]
    types = ["S", "S", "S", "N"]
    outputFile = "Assignment03.html"
    headers, states = read_file('States.csv')
    OU.write_html_file(outputFile, title, headers, types, alignments, states, True)

    # read_file('States.csv')


if __name__ == '__main__':
    main()
