class Seat:
    """
        Check the Seat is free, if yes assign a colleague to seat using set_occupant method.
        To make seat free remove someone from a seat using remove_occupant method.
    """
    def __init__(self,free,occupant):
        self.free = free
        self.occupant = occupant

    def set_occupant(self,name):
        #check seat is free and assign someone to seat
        if self.free:
            self.occupant = name
            self.free = False
        return f"Seat is allocated to {self.occupant}"

    def remove_occupant(self):
        #removes someone from a seat and returns the name of the person occupying the seat before
        if not self.free:
            self.free = True
            prev_name = self.occupant 
            self.occupant = ''
        return prev_name

class Table:
    """
        Class will check if a table has free spot using method has_free_spot.
        It will assign seat of a specific table to a colleague using assign_seat method.
        It can find the count of empty setas on each table using capacity_left method.
    """
    def __init__(self,capacity,seats):
        self.capacity = capacity
        self.seats = seats
    
    def has_free_spot(self):
        #Checks if any seat is empty on the table. It seat is empty return True else False
        free_count = 0
        for val in self.seats.values():
            if val == '':
                free_count += 1
        
        if free_count > 0:
            return True
        else:
            return False


    def assign_seat(self,name):
        #Check if the seat on the table is empty. If yes, assign colleague to that seat.
        self.name = name
        for key,val in self.seats.items():
            if val == '':
                #seat_object1 = Seat(True,val)
                #seat_object1.set_occupant(self.name)
                self.seats[key] = self.name
                break

    def capacity_left(self):
        #returns the capacity available on the table"
        empty_seats = 0
        for key,val in self.seats.items():
            if val == '':
                empty_seats += 1
        return empty_seats



    
