# tire_volume.py

# Import the math module for the value of pi and the datetime module to get the current date.
import math
from datetime import datetime

# --- Enhancement Description ---
# This program exceeds the requirements by asking the user if they would like to
# buy tires with the entered dimensions. If the user answers "yes", the program
# then asks for their phone number and appends it to the entry in the volumes.txt log file.
# This provides a simple way to collect sales leads.

def main():
    """
    Gets tire dimensions from a user, calculates the tire's volume,
    prints the result, and logs all the information to a text file.
    """
    try:
        # Get user input for tire dimensions.
        width = int(input("Enter the width of the tire in mm (ex 205): "))
        aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
        diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

        # --- Tire Volume Calculation ---
        # Calculate the volume using the provided formula:
        # v = (π * w^2 * a + 2540 * d * w * a) / 10,000,000,000
        numerator = (math.pi * width**2 * aspect_ratio) + (2540 * diameter * width * aspect_ratio)
        volume = numerator / 10000000000

        # Display the calculated volume, rounded to two decimal places.
        print(f"\nThe approximate volume is {volume:.2f} liters")

        # --- Exceeding Requirements: Ask to Buy ---
        purchase_interest = input("Would you like to buy tires with these dimensions? (yes/no): ").strip().lower()

        phone_number_info = ""
        if purchase_interest == "yes":
            phone_number = input("Please enter your phone number for a follow-up: ")
            phone_number_info = f", {phone_number}"

        # --- File Logging ---
        # Get the current date from the operating system.
        current_date = datetime.now()

        # Open the volumes.txt file in append mode.
        # The 'with' statement ensures the file is properly closed.
        with open("volumes.txt", "at") as volumes_file:
            # Append the tire information to the file on a new line.
            # The date is formatted as YYYY-MM-DD.
            # The volume is rounded to two decimal places.
            # The phone number is added if the user expressed interest.
            log_entry = (f"{current_date:%Y-%m-%d}, {width}, {aspect_ratio}, "
                         f"{diameter}, {volume:.2f}{phone_number_info}\n")
            volumes_file.write(log_entry)
        
        print("Your information has been logged. Thank you!")

    except ValueError:
        # Handle cases where the user enters non-numeric input.
        print("\nError: Please enter valid numbers for the tire dimensions.")

# This line ensures that the main() function is called only when
# the script is executed directly.
if __name__ == "__main__":
    main() 