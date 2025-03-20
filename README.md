🧠 Streamlit Categorized FAQ Chatbot
📌 Overview
This is a Streamlit-based Categorized FAQ Chatbot that helps users get quick answers to frequently asked questions. Users can select a category, view available questions, and type their own question to get a relevant answer.

🚀 Features
Category Selection: Choose from predefined categories (e.g., Account Management, Orders & Payments, App Help, Support, Fun Facts).
Dynamic Question Display: View all questions within the selected category.
User Input Handling: Enter a custom question for better flexibility.
Cosine Similarity Matching: Matches user questions with existing FAQs using CountVectorizer.
Smart Response: Returns the most similar answer if similarity exceeds 0.3; otherwise, it provides a fallback response.

🛠️ Setup & Installation
Clone the repository.
Install the necessary packages:
Run the chatbot: python -m streamlit run botapp.py

🔧 How to Use
Select a category from the sidebar.
Explore the displayed questions under the selected category.
Type your question in the input box.
The bot will return the most relevant answer or notify you if no good match is found.

🔥 Example Categories & Questions
✅ Account Management

"How do I reset my password?"
"How do I secure my account?"

💸 Orders & Payments

"How do I cancel my order?"
"What should I do if my payment fails?"

📱 App and Website Help

"How do I download the app?"
"Can I use the app offline?"

🤝 Support & Contact

"How do I contact customer support?"
"Is customer support available 24/7?"

🎉 Fun Facts

"Who invented the light bulb?"
"Describe Sobika?"

🌟 Future Improvements

Semantic search using BERT or Sentence Transformers.
Feedback collection to improve answers.
Support for multiple languages.
