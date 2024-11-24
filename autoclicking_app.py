# Auto clicker with GUI

# Import necessary modules
import pyautogui
import threading
import time
import tkinter as tk
from tkinter import messagebox

# Define a class for the auto clicker
class AutoClicker(threading.Thread):
    """
    A class that simulates mouse clicks at a specified interval and duration.
    """
    def __init__(self, click_interval, run_duration, pause_duration, click_area):
        """
        Initialize the auto clicker with the following parameters:
        - click_interval: Time between clicks in seconds
        - run_duration: Run duration in seconds
        - pause_duration: Pause duration in seconds
        - click_area: (x1, y1, x2, y2) coordinates of the area to click
        """
        super().__init__()
        self.click_interval = click_interval  # Time between clicks in seconds
        self.run_duration = run_duration  # Run duration in seconds
        self.pause_duration = pause_duration  # Pause duration in seconds
        self.click_area = click_area  # (x1, y1, x2, y2) coordinates of the area
        self.running = False  # Flag to indicate whether the clicker is running
        self.program_running = True  # Flag to indicate whether the program is running

    # Start the auto clicker
    def start_clicking(self):
        """
        Start the auto clicker.
        """
        self.running = True

    # Stop the auto clicker
    def stop_clicking(self):
        """
        Stop the auto clicker.
        """
        self.running = False

    # Exit the auto clicker and stop the program
    def exit(self):
        """
        Exit the auto clicker and stop the program.
        """
        self.stop_clicking()
        self.program_running = False

    # Main loop for the auto clicker
    def run(self):
        """
        Main loop for the auto clicker.
        """
        while self.program_running:
            if self.running:
                # Wait for 15 seconds before starting to click
                time.sleep(15)
                time.sleep(15)  # Wait for 15 seconds before starting to click
                end_time = time.time() + self.run_duration
                while time.time() < end_time and self.running:
                    # Click at the specified coordinates
                    pyautogui.click(self.click_area[0], self.click_area[1])
                    # Wait for the specified click interval
                    time.sleep(self.click_interval)
                # Wait for the specified pause duration
                time.sleep(self.pause_duration)
            else:
                # If the clicker is not running, wait for 0.1 seconds before checking again
                time.sleep(0.1)

class GUI:
    """
    Class for the graphical user interface.
    """
    def __init__(self, master):
        """
        Initialize the GUI with the following parameters:
        - master: The root window of the GUI
        """
        self.master = master
        self.master.title("Auto Clicker")

        self.click_interval_label = tk.Label(master, text="Click Interval (s):")
        self.click_interval_label.pack()
        self.click_interval_entry = tk.Entry(master)
        self.click_interval_entry.pack()

        self.run_duration_label = tk.Label(master, text="Run Duration (s):")
        self.run_duration_label.pack()
        self.run_duration_entry = tk.Entry(master)
        self.run_duration_entry.pack()

        self.pause_duration_label = tk.Label(master, text="Pause Duration (s):")
        self.pause_duration_label.pack()
        self.pause_duration_entry = tk.Entry(master)
        self.pause_duration_entry.pack()

        self.get_coords_button = tk.Button(master, text="Get Coordinates", command=self.get_coords)
        self.get_coords_button.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_clicking)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_clicking)
        self.stop_button.pack()

        self.exit_button = tk.Button(master, text="Exit", command=self.exit)
        self.exit_button.pack()

        self.click_area = None
        self.clicker = None

    # Get the coordinates of the mouse
    def get_coords(self):
        """
        Get the coordinates of the mouse.
        """
        self.click_area = pyautogui.position()
        messagebox.showinfo("Coordinates", f"Coordinates: {self.click_area}")

    # Start the clicker
    def start_clicking(self):
        """
        Start the clicker.
        """
        if self.click_area:
            try:
                click_interval = float(self.click_interval_entry.get())
                run_duration = float(self.run_duration_entry.get())
                pause_duration = float(self.pause_duration_entry.get())
                self.clicker = AutoClicker(click_interval, run_duration, pause_duration, self.click_area)
                self.clicker.start()
                self.clicker.start_clicking()
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers for click interval, run duration, and pause duration.")
        else:
            messagebox.showerror("Error", "Please get the coordinates first!")

    # Stop the clicker
    def stop_clicking(self):
        """
        Stop the clicker.
        """
        if self.clicker:
            self.clicker.stop_clicking()
        else:
            messagebox.showerror("Error", "Auto clicker is not running!")

    # Exit the program
    def exit(self):
        """
        Exit the program.
        """
        if self.clicker:
            self.clicker.exit()
        self.master.destroy()

root = tk.Tk()
gui = GUI(root)
root.mainloop()

