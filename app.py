import streamlit as st
from google import genai

# Page Configuration
st.set_page_config(page_title="AI Travel Concierge", page_icon="✈️", layout="centered")

st.title("✈️ Gen AI Academy: AI Travel Concierge")
st.write("Your autonomous, intelligent getaway and itinerary planner powered by Gemini.")

# User Inputs
destination = st.text_input("Where do you want to go?", placeholder="e.g., Bali, Jaisalmer, Paris")

col1, col2 = st.columns(2)
with col1:
    days = st.number_input("Number of Days:", min_value=1, max_value=14, value=3)
with col2:
    travel_style = st.selectbox("Travel Style:", ["Adventure & Exploring", "Cafes & Foodie", "Relaxation & Luxury", "Cultural & Historic"])

budget = st.select_slider("Budget Level:", options=["Budget-friendly", "Moderate", "Luxury"])
additional_notes = st.text_area("Any specific preferences? (e.g., 'Love local cafes', 'Traveling with family')")

# Build the prompt
prompt = f"""
You are an expert AI Travel Concierge. Design a highly detailed, personalized day-by-day itinerary for a trip to {destination}.
- Duration: {days} days
- Style: {travel_style}
- Budget: {budget}
- Additional Preferences: {additional_notes}

Provide the response in clean Markdown formatting with clear daily sections.
"""

# Generate Button
if st.button("Generate My Intelligent Itinerary ✨"):
    if not destination:
        st.warning("Please enter a destination to start planning.")
    else:
        with st.spinner("Our AI Concierge is mapping out your perfect trip..."):
            try:
                # Initialize the modern Google GenAI Client with your key
                client = genai.Client(api_key="AQ.Ab8RN6IpG6FdJBqRUywGeWwKwEeVsa3bzKK5nG76Mqmc4E3b5w")
                
                # Call the correct, modern Gemini 2.5 Flash model
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                )
                
                st.success("🎉 Your Personalized Itinerary is Ready!")
                st.markdown("---")
                st.markdown(response.text)
                st.markdown("---")
                
            except Exception as e:
                st.error(f"An error occurred: {e}")