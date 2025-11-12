from datetime import datetime
import json

def create_record(city, comment, date):
    return {
        "city": city,
        "comment": comment,
        "date": date
    }

# Create list of travel records
records = [
    create_record("Paris", "Romantic city with great food", "05-06-2022"),
    create_record("Tokyo", "Amazing mix of tradition and technology", "10-09-2023"),
    create_record("New York", "Loved the skyline and energy", "15-01-2025")
]

# Convert date strings to readable format
for record in records:
    date_obj = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_obj.strftime("%B %d, %Y")  # e.g. "June 05, 2022"

# Convert list to JSON string
records_json = json.dumps(records, indent=4)
print("JSON String:\n", records_json)

# Parse JSON back to Python object
parsed_records = json.loads(records_json)

# Display each record on a new line
print("\nParsed Records:")
for rec in parsed_records:
    print(rec)
