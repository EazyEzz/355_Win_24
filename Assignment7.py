# Queens College
# Internet and Web Technology (CSCI 355)
# Winter 2024
# Assignment 7 - Internet Network Address and Routing
# Essmer Sanchez
# Collaboration: Worked With Class

from subprocess import check_output


# [1] Write a function execute_command(cmd) to execute a windows shell command ("cmd").
# See https://stackoverflow.com/questions/14894993/running-windows-shell-commands-with-python
def exec_cmd(cmd):
    return check_output(cmd, shell=True)


# [2] Define a function get_routing_table by using the function from the previous step to run
# "route print" and then parsing the output into a table (2-D list).
def get_routing_data(routing_data):
    lines = routing_data.decode().split('\n')
    print(lines)


def main():
    routing_data = exec_cmd("route print")
    get_routing_data(routing_data)


if __name__ == '__main__':
    main()
