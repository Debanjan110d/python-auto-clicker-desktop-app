import pyautogui
import threading
import time

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

    def start_clicking(self):
        """
        Start the auto clicker.
        """
        self.running = True

    def stop_clicking(self):
        """
        Stop the auto clicker.
        """
        self.running = False

    def exit(self):
        """
        Exit the auto clicker and stop the program.
        """
        self.stop_clicking()
        self.program_running = False

    def run(self):
        """
        Run the auto clicker in a separate thread.
        """
        while self.program_running:
            if self.running:
                # Calculate the end time for the current run
                end_time = time.time() + self.run_duration
                while time.time() < end_time and self.running:
                    # Calculate the center of the click area
                    x = self.click_area[0] + (self.click_area[2] - self.click_area[0]) // 2
                    y = self.click_area[1] + (self.click_area[3] - self.click_area[1]) // 2
                    # Simulate a mouse click at the center of the click area
                    pyautogui.click(x, y)
                    # Wait for the specified click interval
                    time.sleep(self.click_interval)
                # Wait for the specified pause duration
                time.sleep(self.pause_duration)
            else:
                # If the clicker is not running, wait for 0.1 seconds before checking again
                time.sleep(0.1)

# Get user input for the sleep time and clicking time
print("Enter the sleep time (in seconds): ")
sleep_time = float(input())
print("Enter the clicking time (in seconds): ")
clicking_time = float(input())
print("Enter the pause time (in seconds): ")
pause_time = float(input())
print("Enter the click area coordinates (x1, y1, x2, y2): ")
click_area = tuple(map(int, input().split(',')))

# Create an instance of the auto clicker
clicker = AutoClicker(clicking_time, sleep_time, pause_time, click_area)
# Start the auto clicker in a separate thread
clicker.start()

# Wait for the specified sleep time before starting the clicker
time.sleep(sleep_time)
# Start the clicker
clicker.start_clicking()

try:
    # Run the program indefinitely
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Exit the auto clicker and stop the program when Ctrl+C is pressed
    clicker.exit()
    print("Auto clicker stopped.")