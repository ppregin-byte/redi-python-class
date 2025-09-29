# print("Hello world!")
# random_list = ["Milk", 3, 2.3]
# random_list.append("Bread")
# random_list[2] = "Eggs"
# #del random_list[3]
# print(random_list)

def initialize(temperature: int):
    print("Water Kettle Simulation")
    print(f"Starting temperature: {temperature}°C")


def shut_down():
    print("Kettle has reached the boiling point! Turning off...")
    print("Your water is ready! 🫖")


def determine_status(temperature):
    if temperature <= 25:
        status = "Cool"
    elif temperature <= 40:
        status = "Getting warm"
    elif temperature <= 65:
        status = "Hot"
    elif temperature < 100:
        status = "Almost boiling!"
    else:
        status = "Boiling!"
    
    return status


def heat_up(starting_temperature, heating_increment):
    current_temperature = starting_temperature
    while current_temperature < 100:
        current_temperature += heating_increment
        status = determine_status(current_temperature)
        print(f"Heating... Current temperature: {current_temperature}°C - {status}")


def water_kettle():
    initialize(10)
    heat_up(20,5)
    shut_down()


water_kettle()