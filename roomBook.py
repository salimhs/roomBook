import json
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# File to store user preferences
CONFIG_FILE = "room_booking_config.json"

# Function to ask for user input and save it to a configuration file
def get_user_input():
    print("Setting up your booking preferences...\n")
    
    username = input("Enter your Carleton username: ")
    password = input("Enter your Carleton password: ")
    
    # Get and validate floor preference
    print("Available floors:\nSilent Floor (3rd or 5th)\nConversational Floor (2nd or 4th)")
    floor_preference = ""
    while floor_preference not in ["silent", "conversational"]:
        floor_preference = input("Enter floor preference (silent/conversational): ").lower()
        if floor_preference not in ["silent", "conversational"]:
            print("Invalid input. Please enter 'silent' or 'conversational'.")

    # Scrape rooms based on the selected floor
    rooms = get_rooms_by_floor(floor_preference)
    print(f"Available rooms on {floor_preference} floor: {', '.join(rooms)}")
    
    # Get room preference
    room_preference = ""
    while room_preference not in rooms:
        room_preference = input(f"Enter the room you want to book from the list: ").strip()

    # Get start time for booking
    start_time = input("Enter the start time for booking (e.g., '12:00 PM'): ").strip()

    # Save the user preferences in a JSON file
    preferences = {
        "username": username,
        "password": password,
        "floor_preference": floor_preference,
        "room_preference": room_preference,
        "start_time": start_time
    }

    with open(CONFIG_FILE, "w") as f:
        json.dump(preferences, f)
    
    print("\nPreferences saved! The script will now use these settings for future bookings.")

# Function to load user preferences from the configuration file
def load_user_preferences():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    else:
        print("No preferences found. Please set them up first.")
        get_user_input()
        return load_user_preferences()

# Function to get available rooms based on floor selection
def get_rooms_by_floor(floor_preference):
    if floor_preference == "silent":
        return [
            "324A", "324B", "324C", "324D",
            "561", "562", "563", "564", "565", "566", "567", "568", "569", "570",
            "571", "572", "573", "574"
        ]
    elif floor_preference == "conversational":
        return [
            "234A", "234B", "234C", "234D", "420", "421", "422", "423", "424",
            "462", "463", "464", "465", "466", "467", "468", "469", "470", "471", 
            "472", "473"
        ]

# Step 1: Log in to the Carleton system
def login_to_carleton(driver, username, password):
    print("Logging into the Carleton booking system...")

    # Open the login page
    driver.get("https://carletonu.libcal.com/spaces?lid=2986&gid=0&c=0")
    
    # Locate username and password input fields, and login button (Update selectors as necessary)
    driver.find_element(By.ID, "username_input_field_id").send_keys(username)
    driver.find_element(By.ID, "password_input_field_id").send_keys(password)
    
    # Click the login button
    driver.find_element(By.ID, "login_button_id").click()
    
    # Wait for login to complete
    time.sleep(3)

# Step 2: Select the floor
def select_floor(driver, floor_preference):
    print(f"Selecting the {floor_preference} floor...")
    
    # Adjust based on real selectors from the website
    driver.find_element(By.XPATH, f"//button[contains(text(), '{floor_preference.capitalize()} Floor')]").click()
    
    time.sleep(3)

# Step 3: Select the specific room and time slot
def select_room_and_time(driver, room_preference, start_time):
    print(f"Selecting the room '{room_preference}' and the start time '{start_time}'...")
    
    # Find and click the preferred room
    driver.find_element(By.XPATH, f"//span[contains(text(), '{room_preference}')]").click()
    time.sleep(2)
    
    # Assuming a 2-hour booking duration (adjust as needed)
    time_slot = f"{start_time} - (2 hours later)"  # You can add real logic for duration if needed
    driver.find_element(By.XPATH, f"//button[contains(text(), '{time_slot}')]").click()
    time.sleep(2)

# Step 4: Submit the booking
def submit_booking(driver):
    print("Submitting the booking...")
    
    driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]").click()
    time.sleep(2)
    print("Booking submitted successfully!")

# Main script execution
def main():
    # Load user preferences
    preferences = load_user_preferences()
    
    # Start the Selenium WebDriver with error handling
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        
        try:
            # Perform the login
            login_to_carleton(driver, preferences["username"], preferences["password"])
            
            # Select the appropriate floor
            select_floor(driver, preferences["floor_preference"])
            
            # Select the desired room and time slot
            select_room_and_time(driver, preferences["room_preference"], preferences["start_time"])
            
            # Submit the booking
            submit_booking(driver)
        
        finally:
            # Close the browser after everything
            driver.quit()
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the script
if __name__ == "__main__":
    main()
