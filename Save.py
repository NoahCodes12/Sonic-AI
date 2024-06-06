import json
import os

# Function to collect user information
def collect_user_info():
    users = []
    while True:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        english_knowledge = input("Enter your English knowledge level (beginner/intermediate/advanced): ")

        # Save the user information in a dictionary
        user = {
            "name": name,
            "age": age,
            "english_knowledge": english_knowledge
        }
        users.append(user)

        # Ask if the user wants to add another entry
        another = input("Do you want to add another user? (yes/no): ")
        if another.lower() != "yes":
            break
    
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

# Collect user information
user_data = collect_user_info()

# Save the collected information to a JSON file
save_to_json(user_data)

print("User information saved successfully.")
