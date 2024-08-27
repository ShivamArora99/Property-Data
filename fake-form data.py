import  pandas  as pd
from faker import Faker
import random

fake = Faker('en_AU')
suburbs = [
    {'name': 'Bondi', 'lat': -33.8915, 'lon': 151.2767},
    {'name': 'Manly', 'lat': -33.7963, 'lon': 151.2875},
    {'name': 'Parramatta', 'lat': -33.8140, 'lon': 151.0031},
    {'name': 'Surry Hills', 'lat': -33.8836, 'lon': 151.2115},
    {'name': 'Newtown', 'lat': -33.8971, 'lon': 151.1796},
    {'name': 'Chatswood', 'lat': -33.7969, 'lon': 151.1832},
    {'name': 'Liverpool', 'lat': -33.9175, 'lon': 150.9244},
    {'name': 'Cronulla', 'lat': -34.0527, 'lon': 151.1523},
    {'name': 'Mosman', 'lat': -33.8295, 'lon': 151.2443},
    {'name': 'Penrith', 'lat': -33.7510, 'lon': 150.6949}
]

property_comments = [
    "The backyard is spacious and perfect for entertaining guests.",
    "I love the modern kitchen layout and the high-end appliances.",
    "The neighborhood is quiet and family-friendly, which is a big plus.",
    "The open-plan living space makes the home feel very spacious.",
    "The balcony offers stunning views of the surrounding area.",
    "The property is in a great location, close to shops and public transport.",
    "The bedrooms are well-sized and have plenty of natural light.",
    "The price seems reasonable for the area and the amenities offered."
]

def gen_fake_inspection_data(num_records):
    data = []
    for _ in range(num_records):
        suburb = random.choice(suburbs)
        record = {
            'Property ID': random.randint(1, 20),
            'Name': fake.name(),
            'Company': fake.company(),
            'Email Address': fake.email(),
            'Phone Number': fake.phone_number(),
            'Zip Code': fake.postcode(),
            'Address': fake.street_address(),
            'City': 'Sydney',
            'State': 'NSW',
            'Suburb': suburb['name'],
            'Latitude': suburb['lat'],
            'Longitude': suburb['lon'],
            "Did you find what you were looking for": random.choice(['Yes', 'No']),
            'Overall Condition of the Property': random.choice(['Excellent', 'Good', 'Fair', 'Poor', 'Very Poor']),
            'Interaction with the agent': random.randint(1, 5),
            'Satisfaction with the inspection process': random.choice(['Very Satisfied', 'Satisfied', 'Neutral', 'Unsatisfied', 'Very Unsatisfied']),
            'Likelihood to Buy or Rent': random.randint(1, 5),
            'What did you like most?': ', '.join(random.sample(
                ['Bedrooms', 'Bathrooms', 'Kitchen', 'Living Space', 'Garage', 'Balcony', 'Neighborhood', 'Price'],
                k=random.randint(1, 3))),
            'How well did the property meet your needs?': random.randint(1, 5),
            'View Similar Properties': random.choice(['Yes', 'No']),
            'Additional Comments': random.choice(property_comments)
        }

        data.append(record)
    return pd.DataFrame(data)

if __name__ == '__main__':
    fake_survey_data = gen_fake_inspection_data(300)
    fake_survey_data.to_csv('fake_survey_data.csv')
    print("Data generation complete.")


def clean_data(df):
    # Load the data

    # Mapping categorical columns to numerical values
    condition_mapping = {
        'Excellent': 5,
        'Good': 4,
        'Fair': 3,
        'Poor': 2,
        'Very Poor': 1
    }
    satisfaction_mapping = {
        'Very Satisfied': 5,
        'Satisfied': 4,
        'Neutral': 3,
        'Unsatisfied': 2,
        'Very Unsatisfied': 1
    }
    yes_no_mapping = {
        'Yes': 1,
        'No': 0
    }

    # Apply mappings
    df['Overall Condition of the Property'] = df['Overall Condition of the Property'].map(condition_mapping)
    df['Satisfaction with the inspection process'] = df['Satisfaction with the inspection process'].map(satisfaction_mapping)
    df['Did you find what you were looking for'] = df['Did you find what you were looking for'].map(yes_no_mapping)
    df['View Similar Properties'] = df['View Similar Properties'].map(yes_no_mapping)

    # Convert 'Interaction with the agent' and 'Likelihood to Buy or Rent' to integer if they are not already
    df['Interaction with the agent'] = df['Interaction with the agent'].astype(int)
    df['Likelihood to Buy or Rent'] = df['Likelihood to Buy or Rent'].astype(int)
    df['How well did the property meet your needs?'] = df['How well did the property meet your needs?'].astype(int)

    # Save cleaned data
    df.to_csv('cleaned_fake.csv', index=False)




if __name__ == '__main__':
    fake_survey_data = gen_fake_inspection_data(300)
    fake_survey_data.to_csv('fake_survey_data.csv')
    clean_data(fake_survey_data)
    print("all good")