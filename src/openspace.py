from src.table import Table

class OpenSpace:
    """
        Class has the list of table object. It check each table if it has an empty seat.
        If it has it takes the name of one colleauge and assign the colleauge to a seat by 
        calling the function of table class.
        It also display the final setup of the opensapce with Table details and its Seats with 
        Colleauges assign to it on the screen using display method. 
        The final openspace setup can written to an output file using store method.
    """
    def __init__(self,tables,number_of_tables):
        self.tables = tables
        self.number_of_tables = number_of_tables

    def organize(self,name):
        #will randomly assign people in the different Table objects
        self.name = name
        for table_list in self.tables:
            current_table = Table(self.number_of_tables,table_list[1])
            free_spot_result = current_table.has_free_spot()
            if free_spot_result:
                current_table.assign_seat(name)
                break 
        
    def display(self):
        #display the different tables and Seats with colleagues in a readable way
        for table_details in self.tables:
            print(table_details[0],end="\n")
            for key,val in table_details[1].items():
                print(f"\t \t {key} is allocated to {val}",end="\n")
    
    def store(self,filename):
        #Write the Allocation of Tables & Seats to colleauges in the output file
        self.filename = filename
        output_file = open(self.filename,"w")
        for table_details in self.tables:
            output_file.write(table_details[0] + ": \n")
            for key,val in table_details[1].items():
                output_file.write("\t \t " + key + " is allocated to : " + val + "\n")
        output_file.close()



        