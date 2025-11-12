from datetime import datetime
import json

def get_trip(city, date, comment):
    return {
        "city": city,
        "date": date,
        "comment": comment
    }

# Create list of trips
trips = [
    get_trip("Paris", "15-05-2023", "Beautiful spring weather and great food!"),
    get_trip("Tokyo", "20-09-2024", "Loved the culture and tech scene."),
    get_trip("New York", "10-01-2025", "Snowy but amazing city life.")
]

# Convert date strings to formatted date objects
for trip in trips:
    date_obj = datetime.strptime(trip["date"], "%d-%m-%Y")
    trip["date"] = date_obj.strftime("%B %d, %Y")  # Format: "Month Day, Year"

# Convert list to JSON string
trips_json = json.dumps(trips, indent=4)

# Print JSON
print(trips_json)

