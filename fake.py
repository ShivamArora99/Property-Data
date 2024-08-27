import random
import csv
from datetime import datetime, timedelta

# List of Sydney suburbs
sydney_suburbs = [
    'Bondi', 'Manly', 'Parramatta', 'Chatswood', 'Surry Hills',
    'Newtown', 'Paddington', 'Glebe', 'Balmain', 'Coogee',
    'North Sydney', 'Mosman', 'Double Bay', 'Rose Bay', 'Woolloomooloo',
    'Redfern', 'Pyrmont', 'Marrickville', 'Leichhardt', 'Waterloo'
]

# Define a list of property types
property_types = ['Apartment', 'House', 'Townhouse']

# Extended list of properties with additional features
properties = [
    {
        'property_id': f'P{str(i + 1).zfill(3)}',
        'property_name': f'Property {i + 1}',
        'location': random.choice(sydney_suburbs),
        'bedrooms': random.randint(1, 5),
        'bathrooms': random.randint(1, 3),
        'property_type': random.choice(property_types),
        'lot_size': random.randint(150, 1000),  # Lot size in square meters
        'year_built': random.randint(1970, 2023)
    }
    for i in range(20)
]

# List of users with demographics and additional features
users = [
    {
        'user_id': f'U{str(i + 1).zfill(3)}',
        'first_name': random.choice(
            ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'Diana', 'Edward', 'Fiona', 'George', 'Hannah']),
        'last_name': random.choice(
            ['Doe', 'Smith', 'Johnson', 'Brown', 'Williams', 'Jones', 'Miller', 'Davis', 'Garcia', 'Martinez']),
        'email': f'user{i + 1}@example.com',
        'phone': f'{random.randint(1000000000, 9999999999)}',
        'age': random.randint(25, 65),
        'gender': random.choice(['Male', 'Female', 'Other']),
        'income_level': random.choice(['Low', 'Middle', 'High']),
        'marital_status': random.choice(['Single', 'Married', 'Divorced', 'Widowed']),
        'children': random.choice([0, 1, 2, 3])
    }
    for i in range(20)
]

# Define feedback and interaction types with mixed text lengths
liking_reasons = [
    "I loved the spacious living area and the modern kitchen.",
    "The property is in a great location, close to public transport and schools.",
    "The price is very reasonable for the size of the property.",
    "I like the quiet neighborhood and the fact that it has a big backyard.",
    "It has all the amenities I was looking for, including a gym and swimming pool.",
    "The house has a lot of potential for renovation and investment.",
    "The views from the balcony are amazing.",
    "It's close to my workplace, which is very convenient.",
    "The community around the property is very friendly.",
    "This property feels like a place I could call home.",
    "The layout of the house is very practical.",
    "I appreciate the energy-efficient features of this property."
]

disliking_reasons = [
    "The property is too expensive for my budget.",
    "The location is not ideal, too far from the city center.",
    "The rooms are smaller than I expected.",
    "It lacks modern features and feels outdated.",
    "The neighborhood does not seem safe.",
    "I don't like the layout of the property.",
    "There are too few parking spaces available.",
    "The property requires too many repairs.",
    "The backyard is too small.",
    "I’m not a fan of the interior design.",
    "The area is too noisy.",
    "It’s too far from public transport and schools."
]

ratings = [1, 2, 3, 4, 5]  # Ratings from 1 to 5
feature_preferences = ["Rooms", "Balcony", "Space", "Pool", "Gym", "Parking", "Location", "Price"]
property_tags = ["Spacious", "Budget-Friendly", "Good Locality", "Investment Potential", "Family-Friendly",
                 "Near Public Transport"]


# Generate fake data for multiple tables
def generate_users_table():
    return users


def generate_properties_table():
    return properties


def generate_interactions_table(num_entries):
    interactions = []
    for _ in range(num_entries):
        user = random.choice(users)
        property = random.choice(properties)

        timestamp = datetime.now() - timedelta(days=random.randint(1, 30))
        duration = random.randint(1, 120)  # Duration in minutes

        interactions.append({
            'user_id': user['user_id'],
            'property_id': property['property_id'],
            'timestamp': timestamp,
            'duration': duration
        })

    return interactions


def generate_feedback_table(num_entries):
    feedbacks = []
    for _ in range(num_entries):
        user = random.choice(users)
        property = random.choice(properties)

        feedback_id = f"F{random.randint(1000, 9999)}"
        inspection_date = datetime.now() - timedelta(days=random.randint(1, 30))
        feedback_date = inspection_date + timedelta(days=random.randint(0, 7))

        liking_text = random.choice(liking_reasons)
        disliking_text = random.choice(disliking_reasons)

        property_condition_rating = random.choice(ratings)
        agent_interaction_rating = random.choice(ratings)
        overall_experience_rating = random.choice(ratings)

        feedbacks.append({
            'feedback_id': feedback_id,
            'user_id': user['user_id'],
            'property_id': property['property_id'],
            'inspection_date': inspection_date,
            'feedback_date': feedback_date,
            'liking_text': liking_text,
            'disliking_text': disliking_text,
            'property_condition_rating': property_condition_rating,
            'agent_interaction_rating': agent_interaction_rating,
            'overall_experience_rating': overall_experience_rating
        })

    return feedbacks


def generate_property_tags_table(num_entries):
    property_tags_data = []
    for _ in range(num_entries):
        user = random.choice(users)
        property = random.choice(properties)

        selected_tags = random.sample(property_tags, random.randint(1, len(property_tags)))

        property_tags_data.append({
            'user_id': user['user_id'],
            'property_id': property['property_id'],
            'tags': ', '.join(selected_tags)
        })

    return property_tags_data


# Generate data
num_entries = 5000
users_table = generate_users_table()
properties_table = generate_properties_table()
interactions_table = generate_interactions_table(num_entries)
feedback_table = generate_feedback_table(num_entries)
property_tags_table = generate_property_tags_table(num_entries)


# Write each table to a separate CSV file
def write_csv(filename, data, fieldnames):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"{filename} generated successfully.")


write_csv('users_table.csv', users_table, users_table[0].keys())
write_csv('properties_table.csv', properties_table, properties_table[0].keys())
write_csv('interactions_table.csv', interactions_table, interactions_table[0].keys())
write_csv('feedback_table.csv', feedback_table, feedback_table[0].keys())
write_csv('property_tags_table.csv', property_tags_table, property_tags_table[0].keys())
