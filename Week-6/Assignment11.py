"""
Assignment 11: Python Week 6
"""
# import json
# from pathlib import Path

# Function to create the request details for the automotive API based on the brand name
def automotiveResponse(brandName):
    return{
        "endpoint": "/car",
        "query": {"brand": brandName}
    }

# Function to choose specific automotive values from the API response
def choose_automotive_values(response):
    current = response["Current"]
    return{
        "carPrice": current["carPrice"],
        "carCondition": current["carCondition"]
    }
# Get the request details for the automotive brand "Ford"
request_details = automotiveResponse("Ford")

# Simulate a response from the automotive API for the chosen brand
simulated_response = {
    "Current": {
        "carPrice": 25000,
        "carCondition": "New"
    }
}
# Choose the automotive values from the simulated response
chosen_values = choose_automotive_values(simulated_response)

# Print the request details and the chosen automotive values
print("Request endpoint:", request_details["endpoint"])
print("Request query:", request_details["query"])
print("Chosen values:", chosen_values)


#Input data from a json and create an error message.
# input_file = Path(__file__).with_name("car_brand.json")

# Open the input JSON file and load its contents
# with input_file.open("r", encoding="utf-8") as file:
    # input_data = json.load(file)

    
    # Check if the input data contains an error status
    # if input_data["status"] == "error":
        # Print a message indicating that an error was found
        # print("Error message:", input_data["message"])
    # else:
        # Print a message indicating that no error was found
        # print("No error found.")