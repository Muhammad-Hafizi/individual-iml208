import json
import os
import tkinter as tk
from tkinter import messagebox, ttk

# Sample data file
DATA_FILE = 'car_data.json'

# Ensure the file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as file:
        pass

# Function to create a new booking
def create_data(name, date, duration, car_model, booking_status):
    data = {
        'name': name,
        'date': date,
        'duration': duration,
        'car_model': car_model,
        'booking_status': booking_status
    }
    try:
        with open(DATA_FILE, 'a') as file:
            json.dump(data, file)
            file.write('\n')
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Error creating booking: {e}")
        return False

# Function to read all bookings
def read_data():
    try:
        with open(DATA_FILE, 'r') as file:
            lines = file.readlines()
            return [json.loads(line) for line in lines]
    except Exception as e:
        messagebox.showerror("Error", f"Error reading bookings: {e}")
        return []

# Function to update an existing booking
def update_data(name, new_data):
    updated = False
    try:
        with open(DATA_FILE, 'r') as file:
            lines = file.readlines()

        with open(DATA_FILE, 'w') as file:
            for line in lines:
                booking = json.loads(line)
                if booking['name'] == name:
                    booking.update(new_data)
                    updated = True
                file.write(json.dumps(booking) + '\n')

        return updated
    except Exception as e:
        messagebox.showerror("Error", f"Error updating booking: {e}")
        return False

# Function to delete an existing booking
def delete_data(name):
    deleted = False
    try:
        with open(DATA_FILE, 'r') as file:
            lines = file.readlines()

        with open(DATA_FILE, 'w') as file:
            for line in lines:
                booking = json.loads(line)
                if booking['name'] != name:
                    file.write(json.dumps(booking) + '\n')
                else:
                    deleted = True

        return deleted
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting booking: {e}")
        return False

# GUI Application
def main():
    def clear_entries():
        name_var.set("")
        date_var.set("")
        duration_var.set("")
        car_model_var.set("")
        status_var.set("")

    def create_booking():
        name = name_var.get()
        date = date_var.get()
        duration = duration_var.get()
        car_model = car_model_var.get()
        status = status_var.get()

        if not all([name, date, duration, car_model, status]):
            messagebox.showwarning("Warning", "All fields are required!")
            return

        if create_data(name, date, duration, car_model, status):
            messagebox.showinfo("Success", "Booking created successfully!")
            clear_entries()

    def view_bookings():
        bookings = read_data()
        for row in tree.get_children():
            tree.delete(row)

        for booking in bookings:
            tree.insert("", "end", values=(
                booking['name'],
                booking['date'],
                booking['duration'],
                booking['car_model'],
                booking['booking_status']
            ))

    def update_booking():
        name = name_var.get()
        date = date_var.get()
        duration = duration_var.get()
        car_model = car_model_var.get()
        status = status_var.get()

        if not name:
            messagebox.showwarning("Warning", "Name is required to update booking!")
            return

        new_data = {'date': date, 'duration': duration, 'car_model': car_model, 'booking_status': status}

        if update_data(name, new_data):
            messagebox.showinfo("Success", "Booking updated successfully!")
            clear_entries()
            view_bookings()
        else:
            messagebox.showwarning("Warning", "Booking not found!")

    def delete_booking():
        name = name_var.get()

        if not name:
            messagebox.showwarning("Warning", "Name is required to delete booking!")
            return

        if delete_data(name):
            messagebox.showinfo("Success", "Booking deleted successfully!")
            clear_entries()
            view_bookings()
        else:
            messagebox.showwarning("Warning", "Booking not found!")

    # Root window
    root = tk.Tk()
    root.title("Car Booking System")

    # Input Fields
    name_var = tk.StringVar()
    date_var = tk.StringVar()
    duration_var = tk.StringVar()
    car_model_var = tk.StringVar()
    status_var = tk.StringVar()

    tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
    tk.Entry(root, textvariable=name_var).grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Date (YYYY-MM-DD)").grid(row=1, column=0, padx=10, pady=5)
    tk.Entry(root, textvariable=date_var).grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Duration (hours)").grid(row=2, column=0, padx=10, pady=5)
    tk.Entry(root, textvariable=duration_var).grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="Car Model").grid(row=3, column=0, padx=10, pady=5)
    tk.Entry(root, textvariable=car_model_var).grid(row=3, column=1, padx=10, pady=5)

    tk.Label(root, text="Status").grid(row=4, column=0, padx=10, pady=5)
    tk.Entry(root, textvariable=status_var).grid(row=4, column=1, padx=10, pady=5)

    # Buttons
    tk.Button(root, text="Create", command=create_booking).grid(row=5, column=0, padx=10, pady=10)
    tk.Button(root, text="Update", command=update_booking).grid(row=5, column=1, padx=10, pady=10)
    tk.Button(root, text="Delete", command=delete_booking).grid(row=6, column=0, padx=10, pady=10)
    tk.Button(root, text="View", command=view_bookings).grid(row=6, column=1, padx=10, pady=10)

    # Treeview for displaying bookings
    columns = ("Name", "Date", "Duration", "Car Model", "Status")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)

    tree.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

if __name__ == '__main__':
    main()
