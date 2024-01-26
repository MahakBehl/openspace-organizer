from src.openspace import OpenSpace
import random
import json

if __name__ == "__main__":

    # Getting Openspace Table & Seat inputs and FIle location from json config file
    with open('config.json') as config_file:
        config_data = json.load(config_file)

    no_of_tables = config_data["no_of_tables"]
    no_of_seats = config_data["no_of_seats"]
    file_location = config_data["file_location"]
    file_name = file_location + "colleagues.txt"

    # Taking Input for number of Tables and Number of Seats per Table
    check_input = input(f"OpenSpace has {no_of_tables} Tables & {no_of_seats} Seats per Table. Do you want to change it (Y/N):")
    print("**********************************************************************************")
    if check_input.upper() == "N":
        print("OpenSpace have : \n\tTables = 6 \n\tSeats per Table = 4")
    elif check_input.upper() == "Y":
        no_of_tables = int(input("Enter number of tables in the OpenSpace: "))
        no_of_seats = int(input("Enter number of seats on each table: ")) 
        print(f"OpenSpace have : \n\tTables = {no_of_tables}   \n\tSeats per Table = {no_of_seats}")
    else:
        print("Wrong Input Entered. Considering Default values : \n\tTables = 6 \n\tSeats per Table = 4")
    
    #Calculating Number of Seats and number of Colleagues to check the occupancy of Openspace
    total_seats = no_of_tables * no_of_seats
    my_file = open(file_name,"r")
    colleauge_names = my_file.readlines()
    no_of_colleauges = len(colleauge_names)

     #Number of Colleagues are more then number of Seats. Considring Adding Extra tables
    if no_of_colleauges > total_seats:
        print("Number of people are more than number of seats in the openspace. ")
        print(f"Total seats = {total_seats} \nNumber of colleagues = {no_of_colleauges}")
        colleauge_without_seat = no_of_colleauges-total_seats
        print(f"Colleagues will not have seat = {colleauge_without_seat}")
        check_extra_table = input("Do you want to add Extra Tables (Y/N):")
        if check_extra_table.upper() == "Y":
            extra_table_req = (colleauge_without_seat // no_of_seats) + 1
            no_of_tables += extra_table_req
            total_seats = no_of_tables * no_of_seats
            print(F"Added New Tables = {extra_table_req}")
            print(f"Total seats after adding new tables = {total_seats} \nNumber of colleagues = {no_of_colleauges}")
        elif check_extra_table.upper() == "N":
            print(f"Assigning Seats to random {total_seats} colleagues. No Extra tables added.")
        else:
            print("Wrong Input!! Extra Tables are not added")
            print(f"Assigning Seats to random {total_seats} colleagues.")
    else:
        print(f"All the people can fit in Openspace, seats left = {total_seats-no_of_colleauges} ")
        print(f"Total seats = {total_seats} \nNumber of colleagues = {no_of_colleauges}")

    print("**********************************************************************************")
   
    #Creating Nested Dictornary for tables & Seats seatup
    table_organized = {}
    for i in range(no_of_tables):
        inner_dict = {}
        for j in range(no_of_seats):
            inner_dict["Seat" + str(j+1)] = ""
        table_organized["Table" + str(i+1)]=inner_dict
    
    #Creating List with colleauge Names and Randomly selecting them to assign seats
    colleauge_list = []
    for names in colleauge_names:
        colleauge_list.append(names.strip())

    random.shuffle(colleauge_list)

    #Creating object of Openspace and calling Organize method to assign seats to all colleauges
    openspace1 = OpenSpace(table_organized.items(),no_of_tables)
    for name in colleauge_list:
        openspace1.organize(name)  


    #Calling display method to show the table & seat layout with colleauge Names assigned
    openspace1.display()

    #Adding the ouput to the file
    output_file_indicator = input("Do you want to create an output file (Y/N):")
    if output_file_indicator.upper() == "Y":
        output_filename = input("Enter expected output filename (.txt): ")
        if output_filename[-4:] == ".txt": 
            openspace1.store(output_filename)
        else:
            print("Entered Wrong File Type!! Seat Allocation are not saved in file.")
    elif output_file_indicator.upper() == "N":
        print("Seat Allocation are not saved in file.")
    else:
        print("Wrong Input!!! Seat Allocation are not saved in file.")
