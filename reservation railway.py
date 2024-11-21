import random
import pickle
import sys

# Global variables for logged-in status
logged_in = False
uid = 0
pwd = ''

# Train class definition
class Train:
    def __init__(self, name='', num=0, src='', dest='', dep_time='', arr_time='', seats=None, fares=None):
        self.name = name
        self.num = num
        self.src = src
        self.dest = dest
        self.dep_time = dep_time
        self.arr_time = arr_time
        self.seats = seats or {'1AC': 0, '2AC': 0, 'SL': 0}
        self.fares = fares or {'1AC': 0, '2AC': 0, 'SL': 0}

    def check_availability(self, coach, num_tickets):
        if self.seats[coach] >= num_tickets:
            return True
        return False

    def book_ticket(self, coach, num_tickets):
        if self.check_availability(coach, num_tickets):
            self.seats[coach] -= num_tickets
            return True
        return False

    def cancel_ticket(self, coach, num_tickets):
        self.seats[coach] += num_tickets


# User class definition
class User:
    def __init__(self, uid, name, pwd):
        self.uid = uid
        self.name = name
        self.pwd = pwd
        self.history = {}

    def add_ticket(self, ticket):
        self.history[ticket.pnr] = ticket


# Ticket class definition
class Ticket:
    def __init__(self, train, user, num_tickets, coach):
        self.pnr = f"{train.num}{user.uid}{random.randint(1000, 9999)}"
        self.train_num = train.num
        self.coach = coach
        self.user_name = user.name
        self.num_tickets = num_tickets
        self.user_uid = user.uid
        user.add_ticket(self)


# Function to load data from file
def load_data():
    try:
        with open('data.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {'trains': {}, 'users': {}}


# Function to save data to file
def save_data():
    with open('data.pkl', 'wb') as f:
        pickle.dump({'trains': trains, 'users': users}, f)


# Accept user input for different operations
def accept_input(prompt, data_type, valid_values=None):
    while True:
        user_input = input(prompt)
        try:
            if data_type == 'int':
                user_input = int(user_input)
            if valid_values and user_input not in valid_values:
                raise ValueError
            return user_input
        except ValueError:
            print(f"Invalid input. Please enter a valid {data_type}.")


# Login function
def login():
    global logged_in, uid, pwd
    uid = accept_input("Enter your User ID: ", 'int')
    pwd = input("Enter your password: ")

    if uid in users and users[uid].pwd == pwd:
        logged_in = True
        print(f"Welcome, {users[uid].name}!")
    else:
        print("Invalid User ID or Password!")
        login()


# Function to book a ticket
def book_ticket():
    if not logged_in:
        login()

    print("Available Trains:")
    for train in trains.values():
        print(f"{train.num} - {train.name} ({train.src} to {train.dest})")

    train_num = accept_input("Enter train number: ", 'int')
    if train_num not in trains:
        print("Invalid train number.")
        return book_ticket()

    train = trains[train_num]
    coach = accept_input("Enter coach type (1AC/2AC/SL): ", 'str', ['1AC', '2AC', 'SL'])
    num_tickets = accept_input("Enter number of tickets: ", 'int')

    if train.book_ticket(coach, num_tickets):
        ticket = Ticket(train, users[uid], num_tickets, coach)
        print(f"Booking successful! Your PNR is {ticket.pnr}")
        save_data()
    else:
        print("Not enough seats available!")
        book_ticket()


# Function to cancel a ticket
def cancel_ticket():
    if not logged_in:
        login()

    pnr = input("Enter your PNR: ")
    user = users[uid]

    if pnr in user.history:
        ticket = user.history[pnr]
        train = trains[ticket.train_num]
        train.cancel_ticket(ticket.coach, ticket.num_tickets)
        del user.history[pnr]
        print(f"Ticket with PNR {pnr} has been cancelled.")
        save_data()
    else:
        print("Invalid PNR!")


# Function to view ticket history
def view_history():
    if not logged_in:
        login()

    user = users[uid]
    print(f"Booking history for {user.name}:")
    for pnr, ticket in user.history.items():
        print(f"PNR: {pnr}, Train: {ticket.train_num} {ticket.coach} ({ticket.num_tickets} tickets)")


# Function to check train seat availability
def check_availability():
    print("Available Trains:")
    for train in trains.values():
        print(f"{train.num} - {train.name} ({train.src} to {train.dest})")
    
    train_num = accept_input("Enter train number: ", 'int')
    if train_num not in trains:
        print("Invalid train number.")
        return check_availability()

    train = trains[train_num]
    coach = accept_input("Enter coach type (1AC/2AC/SL): ", 'str', ['1AC', '2AC', 'SL'])
    print(f"Seats available in {coach}: {train.seats[coach]}")


# Main menu
def menu():
    while True:
        print("\n1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. View Booking History")
        print("4. Check Seat Availability")
        print("5. Exit")
        option = accept_input("Choose an option: ", 'int', [1, 2, 3, 4, 5])

        if option == 1:
            book_ticket()
        elif option == 2:
            cancel_ticket()
        elif option == 3:
            view_history()
        elif option == 4:
            check_availability()
        elif option == 5:
            print("Thank you for using the Railway Reservation System!")
            sys.exit()


# Initialize data
trains = {}
users = {}

# Preload data
data = load_data()
trains = data['trains']
users = data['users']

# Sample data for testing
if not trains:
    trains[12345] = Train("Odisha Express", 12345, "CTC", "KGP", "12:00", "18:00", {'1AC': 30, '2AC': 40, 'SL': 100}, {'1AC': 2200, '2AC': 1200, 'SL': 500})
    trains[54321] = Train("Howrah Express", 54321, "HWR", "KOL", "14:00", "20:00", {'1AC': 20, '2AC': 25, 'SL': 50}, {'1AC': 2500, '2AC': 1500, 'SL': 700})

if not users:
    users[1111] = User(1111, "Kiran", "kiran123")
    users[2222] = User(2222, "Alex", "alex123")
menu()
