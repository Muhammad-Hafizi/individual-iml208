import json

# Sample data file
DATA_FILE = 'car_data.json'

# Function to create a new booking
def create_data(name, date, duration, car_model, booking_status):
    data = {
        'name': name,
        'date': date,
        'duration': duration,
        'car_model': car_model,
        'booking_status': booking_status
    }
    with open(DATA_FILE, 'a') as file:
        json.dump(data, file)
        file.write('\n')

# Function to read all bookings
def read_data():
    with open(DATA_FILE, 'r') as file:
        lines = file.readlines()
        bookings = [json.loads(line) for line in lines]
        for booking in bookings:
            print(booking)

# Function to update an existing booking
def update_data(name, new_data):
    with open(DATA_FILE, 'r') as file:
        lines = file.readlines()
    
    with open(DATA_FILE, 'w') as file:
        for line in lines:
            booking = json.loads(line)
            if booking['name'] == name:
                booking.update(new_data)
            file.write(json.dumps(booking) + '\n')

# Function to delete an existing booking
def delete_data(name):
    with open(DATA_FILE, 'r') as file:
        lines = file.readlines()
    
    with open(DATA_FILE, 'w') as file:
        for line in lines:
            booking = json.loads(line)
            if booking['name'] != name:
                file.write(json.dumps(booking) + '\n')

# Main function to prompt user inputs
def main():
    while True:
        action = input("Choose an action (Create, Read, Update, Delete, Exit): ").lower()
        if action == 'create':
            name = input("Enter name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            duration = input("Enter duration (hours): ")
            car_model = input("Enter car model: ")
            booking_status = input("Enter booking_status: ")
            create_data(name, date, duration, car_model, booking_status)
        elif action == 'read':
            read_data()
        elif action == 'update':
            name = input("Enter name to update: ")
            new_data = {}
            new_data['date'] = input("Enter new date (YYYY-MM-DD): ")
            new_data['duration'] = input("Enter new duration (hours): ")
            new_data['car_model'] = input("Enter new car model: ")
            new_data['booking_status'] = input("Enter new booking_status: ")
            update_data(name, new_data)
        elif action == 'delete':
            name = input("Enter name to delete: ")
            delete_data(name)
        elif action == 'exit':
            break
        else:
            print("Invalid action. Please choose again.")

if __name__ == '__main__':
    main()
