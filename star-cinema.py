""" 
Date: 29/10/2022
Project Type: Cinema Hall Online Ticket Counter
Author: Faysal Ahammed Chowdhury
Email: faysalahammedchowdhury01@gmail.com
"""


# star cinema class
class Star_Cinema:
    __hall_list = []

    # add a new hall when it's created
    def entry_hall(self, hall):
        self.__hall_list.append(hall)


# hall class
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.__hall_no = hall_no
        self.entry_hall(self)

    # seat name to index
    @staticmethod
    def seatname_to_index(seat):
        seat = seat.upper().strip()
        row = seat[0]
        col = ""
        for i in range(1, len(seat)):
            col += seat[i]
        row = ord(row) - 65
        col = int(col) - 1
        return (row, col)

    # index to seat name
    @staticmethod
    def index_to_seat(i, j):
        return chr(i + 65) + str(j + 1)

    # add a new show
    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.__show_list.append(show)
        self.__seats[id] = []
        seat_2d = []
        for i in range(self.rows):
            seat = []
            for j in range(self.cols):
                seat.append(False)
            seat_2d.append(seat)
        self.__seats[id] = seat_2d

    # book seats
    def book_seats(self, name, phone_number, id, seats):
        # making sure id is valid
        if (id in self.__seats) == False:
            print(f"\n\n{'_'*60}\n")
            print("Invalid Show ID. Try Again!!!")
            print(f"\n{'_'*60}\n\n")
            return

        is_empty = True
        for seat in seats:
            # making sure seat is valid
            if seat[0] >= self.rows or seat[1] >= self.cols:
                print(f"\n\n{'_'*60}\n")
                print("Invalid seat. Try Again!!!")
                print(f"\n{'_'*60}\n\n")
                return

            if self.__seats[id][seat[0]][seat[1]] == True:
                print(f"\n\n{'_'*60}\n")
                print(f"{self.index_to_seat(seat[0],seat[1])} seat is already booked")
                print(f"\n{'_'*60}\n\n")
                is_empty = False
                break

        if is_empty:
            for seat in seats:
                self.__seats[id][seat[0]][seat[1]] = True

            print("\n\n##### TICKET BOOKED SUCCESSFULLY #####")
            print(f"{'_'*60}\n")
            print(f"NAME: {name}")
            print(f"PHONE NUMBER: {phone_number}")
            print(
                f"\nMOVIE NAME:  {[movie for movie in self.__show_list if id == movie[0]][0][1]}",
                end="\t\t",
            )
            print(
                f"MOVIE TIME:  {[movie for movie in self.__show_list if id == movie[0]][0][2]}",
            )
            print("TICKETS: ", end="")
            for seat in seats:
                print(f"{self.index_to_seat(seat[0],seat[1])} ", end=" ")
            print(f"\nHALL: {self.__hall_no}")

        print(f"\n{'_'*60}\n\n")

    # will show all show list
    def view_show_list(self):
        print(f"\n\n{'_'*60}\n")
        # show message if no show available
        if len(self.__show_list) == 0:
            print("No shows available at the moment!!!")
            return

        for movie in self.__show_list:
            print(f"MOVIE NAME: {movie[1]}\tSHOW ID: {movie[0]}\t TIME: {movie[2]}")

        print(f"\n{'_'*60}\n\n")

    # will show all available seats
    def view_available_seats(self, id):
        # making sure id is valid
        if (id in self.__seats) == False:
            print(f"\n\n{'_'*70}\n")
            print("Invalid ID. Try Again!!!")
            print(f"\n{'_'*70}\n\n")
            return

        for show in self.__show_list:
            if show[0] == id:
                print(f"\n\nMOVIE NAME: {show[1]}\t\tTime: {show[2]}")
                break

        print('"X" for already booked seats\n')
        print(f"\n{'_'*70}\n")

        for i, row in enumerate(self.__seats[id]):
            for j, col in enumerate(row):
                if col == True:
                    print("X", end="\t\t")
                else:
                    print(self.index_to_seat(i, j), end="\t\t")
            print("\n")

        print(f"\n{'_'*70}\n\n")


sony = Hall(20, 10, 1)
sony.entry_show("12", "Poramon", "26 oct 2022, 12:00 AM")
sony.entry_show("13", "Hawa", "27 oct 2022, 12:00 AM")
sony.entry_show("14", "Dohon", "27 oct 2022, 06:00 PM")


while True:
    print("1. VIEW ALL SHOWS OF TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXIT")
    n = int(input("\nENTER OPTION: "))

    if n == 1:
        sony.view_show_list()
    elif n == 2:
        show_id = input("ENTER SHOW ID: ")
        sony.view_available_seats(show_id)
    elif n == 3:
        name = input("ENTER CUSTOMER NAME: ")
        phone_number = input("ENTER CUSTOMER PHONE NUMBER: ")
        id = input("ENTER SHOW ID: ")
        seats = []
        seat_no = int(input("ENTER NUMBER OF TICKETS: "))
        for i in range(seat_no):
            seat = input("ENTER SEAT NO: ")
            seat = sony.seatname_to_index(seat)
            seats.append(seat)
        sony.book_seats(name, phone_number, id, seats)
    else:
        break
