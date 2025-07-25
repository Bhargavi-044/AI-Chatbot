AI Healthcare Chatbot

## Project Description

This project is a simple AI-powered healthcare chatbot designed to assist users in identifying possible diseases based on their symptoms and medicines.
The chatbot provides basic healthcare advice and encourages users to consult a medical professional for a definitive diagnosis.

### Key Features
- User Input: Users can enter their symptoms and any medicines they are taking.
- Disease Detection: The chatbot uses a rule-based system to match symptoms to a list of 20+ common diseases.
- Healthcare Advice: For each detected disease, the chatbot provides general advice and next steps.
- Web Interface: Users interact with the chatbot through a clean, easy-to-use web page.
- Expandable: The disease database and advice can be easily extended or replaced with more advanced AI/ML models in the future.

### How It Works
1. User Interaction: The user enters symptoms (and optionally medicines) into the chat interface.
2. Processing: The backend (built with Flask) processes the input, compares symptoms to a predefined set of disease rules, and determines the most likely disease(s).
3. Response: The chatbot responds with the detected disease and provides healthcare advice.
4. Recommendation: If the symptoms do not match any known disease, the chatbot advises the user to consult a healthcare professional.

### Technologies Used
- Backend: Python, Flask, Flask-CORS
- Frontend: HTML, CSS, JavaScript
- Logic: Rule-based symptom-to-disease mapping

### Usage
1. Start the Flask server (`python app.py`).
2. Open your browser and go to [http://localhost:5000](http://localhost:5000).
3. Enter your symptoms and medicines to chat with the bot.

### Disclaimer
This chatbot is for educational and informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment.
Always consult a qualified healthcare provider with any questions regarding a medical condition.

