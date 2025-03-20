import streamlit as st
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define a categorized FAQ dataset
faq_data = {
    "Account Management": {
        "How do I reset my password?": "Go to settings, select 'Change Password', and follow the instructions.",
        "How do I change my username?": "Navigate to 'Profile Settings' and select 'Edit Username'.",
        "How can I update my email address?": "Go to account settings and select 'Edit Email' to update it.",
        "How do I delete my account?": "Go to account settings and select 'Delete Account'. Follow the prompts to confirm.",
        "How do I secure my account?": "Use a strong password and enable two-factor authentication in settings."
    },
    "Orders & Payments": {
        "Where can I track my order?": "Visit the 'Order Status' page and enter your order number.",
        "How do I cancel my order?": "Go to 'My Orders', select the order, and click 'Cancel Order'.",
        "What should I do if my payment fails?": "Check your card details, ensure funds are available, and try again.",
        "How do I request a refund?": "Go to 'My Orders', select the order, and click 'Request Refund'.",
        "Do you support PayPal payments?": "Yes, we accept PayPal along with major credit/debit cards."
    },
    "App and Website Help": {
        "How do I download the app?": "Visit the App Store or Google Play Store and search for our app.",
        "What should I do if the app crashes?": "Try closing and reopening the app. If the issue persists, reinstall the app.",
        "How do I update the app?": "Visit the App Store or Google Play Store and click 'Update'.",
        "Can I use the app offline?": "Some features work offline, but an internet connection is required for full functionality."
    },
    "Support & Contact": {
        "How do I contact customer support?": "You can contact support via email at support@example.com or call 123-456-7890.",
        "Is customer support available 24/7?": "Yes, our support team is available 24/7.",
        "How do I report a bug?": "Visit 'Help & Support' and select 'Report a Bug'.",
        "Where can I find the terms and conditions?": "Check the 'Legal' section at the bottom of our homepage."
    },
    "Fun Facts": {
        "What is the weather today?": "Check your local weather app or website for the latest forecast.",
        "What’s the capital of France?": "The capital of France is Paris.",
        "Who invented the light bulb?": "Thomas Edison is credited with inventing the light bulb.",
        "How many continents are there?": "There are seven continents: Africa, Antarctica, Asia, Europe, North America, Australia, and South America.",
        "Describe Sobika?": "Sobika is a well-known dancer and AIML enthusiast."
    }
}

# Streamlit UI setup
st.title("🧠 Categorized FAQ Chatbot")
st.write("Ask me anything from the FAQ list!")

# Sidebar for category selection
category = st.sidebar.selectbox("Select a Category:", list(faq_data.keys()))

# Show questions under the selected category
st.subheader(f"Questions under {category}")
questions = list(faq_data[category].keys())
answers = list(faq_data[category].values())

# Display all possible questions for the selected category
st.write("Here are the available questions:")
for q in questions:
    st.write(f"👉 {q}")

# User input
user_question = st.text_input("Type your question here:").strip()

# Check user question
if user_question:
    # Fit the vectorizer to the questions of the selected category
    vectorizer = CountVectorizer().fit(questions)
    question_vectors = vectorizer.transform(questions)
    user_vec = vectorizer.transform([user_question])

    # Calculate similarity between user question and category questions
    similarities = cosine_similarity(user_vec, question_vectors)
    best_match_idx = np.argmax(similarities)
    best_match_score = similarities[0][best_match_idx]

    # Respond if the similarity is good enough
    if best_match_score > 0.3:
        st.write(f"**Answer:** {answers[best_match_idx]}")
    else:
        st.write("Sorry, I don't know the answer to that yet.")

# Add a footer
st.markdown("---")
st.write("💡 Tip: Select a category first, then type a question or pick one from the list!")
