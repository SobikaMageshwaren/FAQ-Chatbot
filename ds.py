import pandas as pd

# Full FAQ dataset from your code
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

# Convert the dataset into a list of rows
data_rows = [[category, question, answer] 
             for category, questions in faq_data.items() 
             for question, answer in questions.items()]

# Create a DataFrame
df = pd.DataFrame(data_rows, columns=["Category", "Question", "Answer"])

# Save to CSV
csv_filename = "full_faq_data.csv"
df.to_csv(csv_filename, index=False)

print(f"✅ CSV file '{csv_filename}' saved successfully!")
