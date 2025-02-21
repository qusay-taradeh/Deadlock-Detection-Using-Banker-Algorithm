# * Note: The required files must be in same file of project or same file where .py file stored!

# importing library that get the values from .csv files
import pandas


def check_dimensions(allocation, request, available):
    # to check dimensions
    if len(allocation) == len(request):  # check # of rows "# of processes"
        for index in range(len(allocation)):  # check # of columns "# of resources"
            if len(allocation[index]) == len(request[index]) and len(allocation[index]) == len(available) + 1:
                continue
            else:
                return False

        print("The dimensions are consistent")
        return True

    else:
        return False


"""=======================================BANKER ALGORITHM======================================"""


def banker(allocation, request, available):
    """ Banker Algorith:
    Take Allocation, Request, and available
    instances of resources of all processes
    """
    sequence = []  # sequence of possible in safe
    deadlocked = []  # deadlocked processes
    possible_flag = True  # flag for deadlock status

    i = 0
    while i < len(allocation):  # loop to check all process
        if allocation[i][-1] == 1:  # check if process executed then continue to next one
            i += 1
            continue

        alloc = allocation[i][1:-1]  # give just allocation values of each process
        req = request[i][1:]  # give just request values of each process

        possible_flag = True  # initially there is no deadlock
        for j in range(len(alloc)):  # to check if possible to execute requirements of process
            if req[j] > available[j]:  # if there is no enough available resources to execute then process not exec.
                possible_flag = False
                break

        if possible_flag is True:  # if process can execute then execute and add it to the sequence
            available = [x + y for x, y in zip(available, alloc)]  # update available
            sequence.append(allocation[i][0])  # add name of process which is first index
            allocation[i][-1] = 1  # set status 1 such that this process executed
            i = 0  # return to check from start
            continue
        i += 1

    # now check if the system deadlocked or not
    possible_flag = True  # initially there is no deadlock
    for p in allocation:  # to check if the system deadlocked or not
        if p[-1] == 0:  # that's mean if anyone deadlocked
            deadlocked.append(p[0])
            possible_flag = False

    if possible_flag is True:  # if there is no deadlock print series possible in safe
        print("There is no deadlock\nThe possible series without deadlock is:")
        for s in sequence:
            print(s, end=', ')

    else:  # if there is deadlock print just deadlocked processes
        print("Deadlocked System!\nThe processes deadlocked:")
        for d in deadlocked:
            print(d, end=',')

# =============================================================================================


def print_content(table):
    """ function to print the contents
    of the given table in right form """

    print("  P#   A  B  C  D  E")
    for p in table:
        print(p)
    print()


# Main execution
''' Defining required files as its names to read their contents using 'panda' library in python '''
allocation_file = pandas.read_csv('Allocation.csv')
available_file = pandas.read_csv('Available.csv')
request_file = pandas.read_csv('Request.csv')

''' make a 2-D list of Processes vs. Resources given from each file'''
Allocation = list(allocation_file.values.tolist())
Available = list(available_file.values.tolist())
Available = Available[-1]  # last available row in available list
Request = list(request_file.values.tolist())

''' Displaying contents of files '''
print("Allocation file:")
print_content(Allocation)
print("Request file:")
print_content(Request)
print("Available file:")
print(" A  B  C  D  E")
print(Available)

print("\nCheck dimensions:")
check = check_dimensions(allocation=Allocation, request=Request, available=Available)
print()

for element in Allocation:  # adding new cell to check if finished or not in last index i.e. True or False
    element.append(0)

if check is True:  # if dimensions is identical then apply banker's algorithm
    banker(allocation=Allocation, request=Request, available=Available)
else:
    print("The dimensions are not consistent")

print("\n\n======================Thx=======================")