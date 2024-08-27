properties = [
    {"id": 1, "name": "Cozy Apartment in Sydney", "price": 450000, "location": "Sydney"},
    {"id": 2, "name": "Spacious Villa in Melbourne", "price": 850000, "location": "Melbourne"},
    {"id": 3, "name": "Modern Condo in Brisbane", "price": 550000, "location": "Brisbane"},
]

import requests

GA_TRACKING_ID = 'G-CHZZSGD3GX'  # Replace with your tracking ID
client_id = '555'  # A random client ID

payload = {
    'v': '1',
    'tid': GA_TRACKING_ID,
    'cid': client_id,
    't': 'pageview',
    'dp': '/test-page',  # A test page path
    'dt': 'Test Page Title',  # A test page title
    'dh': 'https://mgvdwuclndfrartabyv5tf.streamlit.app/'
}

response = requests.post('https://www.google-analytics.com/collect', data=payload)
print(f'Status Code: {response.status_code}')
