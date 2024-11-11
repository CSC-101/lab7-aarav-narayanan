import sys

from convert import str_to_float

#purpose of the function is to convert a string to float and add up the numbers into a total value
#Input is the list of string values ["abc","1","2","cde"]
#Output is the added numbers from that list Ex. 3.0
def command_line_arguments(arg: list[str])->float:
    add=0 #Start off with 0
    for i in range(len(arg)): #To check each iteration on the list
        num=str_to_float(arg[i]) #Calls back to the convert function for each value
        if num is not None: #If the exception ValueError wasn't hit then the function can proceed with adding the ones that were converted to a float
            add+=num
    return add


if __name__ == '__main__':
    command_line_arguments(sys.argv)

def test_command_line_arguments():
    result=command_line_arguments(["567","abfj","4","7","24"])
    expected=602
    if result==expected:
        print("Passed")
    else:
        print("Failed")
def test_command_line_arguments2():
    result=command_line_arguments(["abfj","shdhs","6"])
    expected=6
    if result==expected:
        print("Passed")
    else:
        print("Failed")
test_command_line_arguments()
test_command_line_arguments2()


