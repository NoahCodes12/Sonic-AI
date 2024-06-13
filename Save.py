import json
import os
from colorama import Fore, Style

filename = "user_data.json"

# Function to save the user information to a JSON file
def save_to_json(new_data, filename="user_data.json"):
    try:
        # Check if the file exists and read the existing data
        if os.path.exists(filename):
            print(f"File {filename} exists")
            with open(filename, "r") as file:
                existing_data = json.load(file)
        else:
            print(f"File {filename} does not exist")
            existing_data = []

        # Update the existing data with new data if it doesn't already exist
        updated_data = existing_data.copy()
        for user in new_data:
            # Check if the user already exists in the existing data
            if not any(existing_user['name'] == user['name'] for existing_user in existing_data):
                updated_data.append(user)
            else:
                print(f"{Fore.RED}User {user['name']} already exists. Skipping save.{Style.RESET_ALL}")

        # Write the updated data back to the file
        with open(filename, "w") as file:
            json.dump(updated_data, file, indent=4)
            print(f"{Fore.BLUE}User information {Style.BRIGHT}saved successfully.{Style.RESET_ALL}")

    except Exception as e:
        print(f"Exception raised: {e}")
    finally:
        print("Call ended")

# Function to collect user information
def collect_user_info(name, age, lvl):
    user = {
        "name": name,
        "age": age,
        "English Knowledge Level": lvl
    }
    save_to_json([user])

# Example usage
collect_user_info("John Doe", 30, "Intermediate")
collect_user_info("Jane Smith", 25, "Advanced")
collect_user_info("John Doe", 30, "Intermediate")  # This should not be saved again
