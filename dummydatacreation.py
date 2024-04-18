import random

# Function to generate sample data
def generate_sample_data(num_records):
    data = []
    for i in range(num_records):
        timestamp = "1/27/2024 23:32:02"  # Assuming fixed timestamp for all records
        email = f"dummy_{i}@gmail.com"
        preferred_name = f"dummy{i}"
        age = random.randint(18, 70)
        skills = random.choice(["Nothing", "Dancing","Acting", "Direction"])
        whatsapp_number = f"8999022979{i:03}"  # Adding a unique suffix to make it distinct
        location = f"Pune_{i % 10}"  # Adding a variation to the location
        language = "Hindi"  # Assuming same language for all records
        referred_by = "Google"  # A ssuming same referral for all records
        row = {
            "Timestamp": timestamp,
            "Email Address": email,
            "Preferred Name": preferred_name,
            "What is your age?": age,
            "What are your skills?": skills,
            "Whatsapp Number": whatsapp_number,
            "Location": location,
            "What language do you speak?": language,
            "Who referred you to this agency?": referred_by
        }
        data.append(row)
    return data

# Number of sample records to generate
num_records = 1000

# Generate sample data
sample_data = generate_sample_data(num_records)

# Print sample data
for record in sample_data:
    print(record)
