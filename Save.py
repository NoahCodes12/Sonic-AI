import json
import os
from colorama import Fore, Style

# Function to collect user information
def collect_user_info(name, age):
    users = []
    while True:
        # Save the user information in a dictionary
        user = {
            "name": name,
            "age": age,
        }
        users.append(user)
        return users

# Function to save the user information to a JSON file
def save_to_json(new_data, filename="user_data.json"):
    # Check if the file exists
    if os.path.exists(filename):
        # Read the existing data
        with open(filename, "r") as file:
            existing_data = json.load(file)
    else:
        existing_data = []

    # Update the existing data with new data
    for user in new_data:
        if user not in existing_data:
            existing_data.append(user)

    # Write the updated data back to the file
    with open(filename, "w") as file:
        json.dump(existing_data, file, indent=4)

print(f"{Fore.BLUE}User information {Style.BRIGHT}saved successfully.")
