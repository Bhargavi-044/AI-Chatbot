from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Simple rules for disease detection (expandable)
DISEASE_RULES = [
    {
        'disease': 'Common Cold',
        'symptoms': {'cough', 'sneezing', 'runny nose', 'sore throat'},
        'advice': 'Rest, stay hydrated, and consider over-the-counter cold remedies.'
    },
    {
        'disease': 'Flu',
        'symptoms': {'fever', 'chills', 'body ache', 'fatigue', 'cough'},
        'advice': 'Rest, drink fluids, and consult a doctor if symptoms are severe.'
    },
    {
        'disease': 'Migraine',
        'symptoms': {'headache', 'nausea', 'sensitivity to light', 'sensitivity to sound'},
        'advice': 'Rest in a dark, quiet room and consider prescribed medication.'
    },
    {
        'disease': 'COVID-19',
        'symptoms': {'fever', 'cough', 'loss of taste', 'loss of smell', 'shortness of breath'},
        'advice': 'Isolate, get tested, and consult a healthcare provider.'
    },
    {
        'disease': 'Allergic Rhinitis',
        'symptoms': {'sneezing', 'runny nose', 'itchy eyes', 'nasal congestion'},
        'advice': 'Avoid allergens, use antihistamines, and consult a doctor if needed.'
    },
    {
        'disease': 'Asthma',
        'symptoms': {'wheezing', 'shortness of breath', 'chest tightness', 'cough'},
        'advice': 'Use prescribed inhalers and avoid triggers.'
    },
    {
        'disease': 'Pneumonia',
        'symptoms': {'fever', 'cough', 'chest pain', 'shortness of breath', 'fatigue'},
        'advice': 'Seek medical attention for antibiotics and supportive care.'
    },
    {
        'disease': 'Gastroenteritis',
        'symptoms': {'diarrhea', 'vomiting', 'abdominal pain', 'nausea', 'fever'},
        'advice': 'Stay hydrated and consult a doctor if symptoms persist.'
    },
    {
        'disease': 'Diabetes',
        'symptoms': {'increased thirst', 'frequent urination', 'fatigue', 'blurred vision'},
        'advice': 'Monitor blood sugar, follow prescribed medication, and consult your doctor.'
    },
    {
        'disease': 'Hypertension',
        'symptoms': {'headache', 'dizziness', 'blurred vision', 'nosebleeds'},
        'advice': 'Monitor blood pressure, reduce salt intake, and take prescribed medication.'
    },
    {
        'disease': 'Tuberculosis',
        'symptoms': {'persistent cough', 'weight loss', 'night sweats', 'fever'},
        'advice': 'Consult a doctor for diagnosis and treatment.'
    },
    {
        'disease': 'Chickenpox',
        'symptoms': {'itchy rash', 'fever', 'fatigue', 'loss of appetite'},
        'advice': 'Rest, avoid scratching, and consult a doctor if needed.'
    },
    {
        'disease': 'Measles',
        'symptoms': {'fever', 'rash', 'cough', 'runny nose', 'red eyes'},
        'advice': 'Rest, stay hydrated, and consult a doctor.'
    },
    {
        'disease': 'Malaria',
        'symptoms': {'fever', 'chills', 'sweating', 'headache', 'nausea'},
        'advice': 'Seek immediate medical attention for antimalarial treatment.'
    },
    {
        'disease': 'Dengue',
        'symptoms': {'fever', 'severe headache', 'pain behind eyes', 'joint pain', 'rash'},
        'advice': 'Rest, drink fluids, and consult a doctor.'
    },
    {
        'disease': 'Typhoid',
        'symptoms': {'fever', 'abdominal pain', 'headache', 'loss of appetite', 'diarrhea'},
        'advice': 'Consult a doctor for antibiotics and supportive care.'
    },
    {
        'disease': 'Urinary Tract Infection',
        'symptoms': {'burning urination', 'frequent urination', 'pelvic pain', 'cloudy urine'},
        'advice': 'Drink plenty of water and consult a doctor for antibiotics.'
    },
    {
        'disease': 'Sinusitis',
        'symptoms': {'facial pain', 'nasal congestion', 'headache', 'runny nose'},
        'advice': 'Use decongestants and consult a doctor if symptoms persist.'
    },
    {
        'disease': 'Bronchitis',
        'symptoms': {'cough', 'mucus', 'fatigue', 'shortness of breath', 'chest discomfort'},
        'advice': 'Rest, drink fluids, and consult a doctor if needed.'
    },
    {
        'disease': 'Appendicitis',
        'symptoms': {'abdominal pain', 'loss of appetite', 'nausea', 'vomiting', 'fever'},
        'advice': 'Seek immediate medical attention.'
    },
    {
        'disease': 'Anemia',
        'symptoms': {'fatigue', 'pale skin', 'shortness of breath', 'dizziness'},
        'advice': 'Eat iron-rich foods and consult a doctor for supplements.'
    },
    {
        'disease': 'Depression',
        'symptoms': {'persistent sadness', 'loss of interest', 'fatigue', 'sleep disturbances'},
        'advice': 'Seek support from mental health professionals.'
    },
    {
        'disease': 'Anxiety Disorder',
        'symptoms': {'excessive worry', 'restlessness', 'fatigue', 'difficulty concentrating'},
        'advice': 'Practice relaxation techniques and consult a mental health professional.'
    },
    {
        'disease': 'Otitis Media',
        'symptoms': {'ear pain', 'fever', 'hearing loss', 'irritability'},
        'advice': 'Consult a doctor for diagnosis and treatment.'
    },
    {
        'disease': 'Conjunctivitis',
        'symptoms': {'red eyes', 'itchy eyes', 'watery eyes', 'discharge'},
        'advice': 'Maintain eye hygiene and consult a doctor if needed.'
    },
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    symptoms = set(s.strip().lower() for s in data.get('symptoms', []))
    medicines = [m.strip().lower() for m in data.get('medicines', [])]

    detected = None
    for rule in DISEASE_RULES:
        if symptoms & rule['symptoms']:
            detected = rule
            break

    if detected:
        response = {
            'disease': detected['disease'],
            'advice': detected['advice'],
            'message': f"Based on your symptoms, you may have {detected['disease']}. {detected['advice']}"
        }
    else:
        response = {
            'disease': 'Unknown',
            'advice': 'Please consult a healthcare professional for an accurate diagnosis.',
            'message': 'Sorry, I could not determine your condition. Please consult a doctor.'
        }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True) 