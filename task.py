import pandas as pd

# Load the .csv file into a pandas DataFrame
data = pd.read_csv('US_Accidents_Dec21_updated.csv')


# Returns result of task as a dictionary
def task(zipcode):
    result = {
        'zip': zipcode,
        'most_common': "",
        'locations': {
        }
    }
    # Filter the data for the specific zipcode
    filtered_data = data[data['Zipcode'] == zipcode]

    # Get longitude and latitude of the first five accidents
    longitudes = filtered_data['Start_Lng'].head(5)
    latitudes = filtered_data['Start_Lat'].head(5)

    for i, (lat, lon) in enumerate(zip(latitudes, longitudes)):
        result['locations'][f'l{i}'] = f'https://www.google.com/maps/search/?api=1&query={lat}%2C{lon}'

    # Count the occurrences of each traffic signal
    traffic_signal_counts = filtered_data['Description'].value_counts()

    # Get the most common traffic signal
    result['most_common'] = traffic_signal_counts.idxmax()

    return result

# Example result
# {
#     "zip": "90018",
#     "most_common": "At Arlington Ave/Exit 10 - Accident.",
#     "locations": {
#         "l0": "https://www.google.com/maps/search/?api=1&query=34.035340000000005%2C-118.32994",
#         "l1": "https://www.google.com/maps/search/?api=1&query=34.03695%2C-118.30427",
#         "l2": "https://www.google.com/maps/search/?api=1&query=34.03674%2C-118.30281",
#         "l3": "https://www.google.com/maps/search/?api=1&query=34.035340000000005%2C-118.32994",
#         "l4": "https://www.google.com/maps/search/?api=1&query=34.036190000000005%2C-118.32057"
#     }
# }
