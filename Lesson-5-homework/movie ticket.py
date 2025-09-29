# Movies with available show slots: M = Morning, A = Afternoon, E = Evenin
movies = {
        "Terminator 2": ["M", "E"],
        "Interstellar" : ["M", "A"],
        "Blacklist": ["M", "A", "E"],
        "Home Alone": ["E"],
        "The Pursuit of Happiness": ["M", "A"]
    }
# Dictionary of seat types and their prices 
seat_types = {
    "regular": 15,
    "vip": 18,
    "dbox": 20
}
# Function to display available movies and their showtimes to the user
def movie_program():
    print("This is today's movie program:")
    for movie in movies:
        print(f"{movie} at show slot {movies[movie]}")
# Function to ask user for chosen movie and showtime, and validate the input
def ask_movie_time():
    while True:
        title = input(f"What movie?")
        if title in movies:
            print(f"Movie is valid. The available showtimes are: {movies[title]}")                
            while True:
                show_time = input(f"What time?")
                if show_time in movies[title]:
                    print("Time is valid!")
                    return title, show_time # return both title and show_time as a tuple      
                else:
                    print("Time is invalid :( Try Again")
        else:
            print("Invalid :( Try Again")
# Function to ask user for number of tickets and seat type, and validate the input
def ask_ticket_info():
    while True:
        number = input(f"How many tickets?")
        if number.isdigit() and int(number) > 0:
            print(f"We offer the following types of seats: {list(seat_types.keys())}")
            while True:
                seat_type = input(f"What type of seat?")
                if seat_type in seat_types.keys():
                    print("Seat type is valid!")
                    return int(number), seat_type 
                else:
                    print("Seat type is invalid :( Try Again")
        else:
            print("Invalid number of tickets! Try Again")
# Function to calculate total price based on number of tickets and seat type           
def calculate_total_price(numb, seat):
    return numb * seat_types[seat]            
# Function to display booking confirmation with all details
def show_booking_confirmation(movie_info, seat_info, total_price):
    print("\nBooking Confirmation:")
    print(f"Film: {movie_info[0]}")
    print(f"Time: {movie_info[1]}")
    print(f"Number of tickets: {seat_info[0]}")
    print(f"Seat type: {seat_info[1]}")
    print(f"Total price: {total_price}$")
# Main program execution 
movie_program()
movie_info = ask_movie_time() # Call the ask_movie_time function and store the returned value
seat_info = ask_ticket_info() # Call the ask_ticket_info function and store the returned value
total_price = calculate_total_price(seat_info[0], seat_info[1]) # Call the calculate_total_price function. Store the returned total price
show_booking_confirmation(movie_info, seat_info, total_price) # Call the show_booking_confirmation function with the collected information


