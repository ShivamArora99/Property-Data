import streamlit as st
from data import properties

# Sample property data
import streamlit.components.v1 as components

GA_TRACKING_ID = 'G-CHZZSGD3GX'

GA_JS = f"""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_TRACKING_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', '{GA_TRACKING_ID}');
</script>
"""

# Inject the Google Analytics script in the head of the page
components.html(GA_JS, height=0)



st.title("Real Estate Data Collection App")

st.sidebar.header("Property Filters")
location = st.sidebar.selectbox("Location",["Sydney", "Melbourne", "Brisbane"])
price_range = st.sidebar.slider("Price Range", 100000, 1000000, (200000, 800000))


st.header("Property Listings")
st.write("Here, you'll see the properties based on selected filters.")


# Filter properties based on selected location and price range
filtered_properties = [p for p in properties if
                       p["location"] == location and price_range[0] <= p["price"] <= price_range[1]]

# Display filtered properties
for property in filtered_properties:
    if st.button("Save Property", key=property["id"]):
        st.write(f"Property '{property['name']}' saved.")
        # Custom Google Analytics event
        components.html(f"""
        <script>
        gtag('event', 'save_property', {{
            'event_category': 'User Actions',
            'event_label': '{property["name"]}',
        }});
        </script>
        """, height=0)



st.header("Feedback Form")
property_feedback = st.selectbox("Which property would you like to provide feedback on?", [p["name"] for p in properties])
feedback = st.text_area("What did you like or dislike about the property?")
agent_interaction = st.slider("Rate the agent interaction (1-5)", 1, 5)

if st.button("Submit Feedback"):
    st.write("Thank you for your feedback!")
    # Here, you would save the feedback to your database or a file

st.header("Inspection Registration")
inspection_property = st.selectbox("Select the property you want to inspect", [p["name"] for p in properties])
inspection_date = st.date_input("Select a date for the inspection")

if st.button("Register for Inspection"):
    st.write(f"Inspection registered for {inspection_property} on {inspection_date}.")
    # Save inspection registration data

