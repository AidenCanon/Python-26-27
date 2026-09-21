"""
Assignment 11: Python Week 6
"""
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