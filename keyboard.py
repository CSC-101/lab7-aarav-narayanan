from convert import str_to_float

#Purpose is to create a list with numbers that were converted from string to float
#Input is the user input of strings such as "6" and then if they were to contine with Y/N they would input another one "5"
#Output is the new list with only the numbers [5.0]
def gather_numbers()->list[float]:
    new_list=[] #Start with empty list
    repeat=1 #Keep the repetition as 1 as first
    while repeat==1: #while loop to keep  the loop until user stops
        number=input("Enter one number: ") #Tells user to input number
        new_num=str_to_float(number) #uses the convert function to convert the string to a float
        if new_num is not None: #TO show if the number didn't show up as a ValueError and then it will append to new_list
            new_list.append(new_num)
        again=input("Do you want to enter another number (Y/N):") #asks if user wants to continue with a Y or N answer
        if again=="Y": #If statement for the code to be stuck on the while loop if repeat=1 or 0
            repeat=1
        else:
            repeat=0
    return new_list


if __name__ == '__main__':
    print(gather_numbers())