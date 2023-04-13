import pickle
import numpy as np
from statistics import mode
from flask import Flask, jsonify

app = Flask(__name__)

# load the trained model
with open('final_rf_model.pkl', 'rb') as f:
    final_rf_model = pickle.load(f)

with open('final_nb_model.pkl', 'rb') as f:
    final_nb_model = pickle.load(f)

with open('final_svm_model.pkl', 'rb') as f:
    final_svm_model = pickle.load(f)

# load the symptom index dictionary and predictions classes
with open('data_dict.pkl', 'rb') as f:
    data_dict = pickle.load(f)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/predict/<string:s>')
def predict(s):
    input_data = []
    for char in s:
        input_data.append(int(char))
    
    # reshape the input data and convert it into suitable format for model predictions
    input_data = np.array(input_data).reshape(1,-1)
    
    rf_prediction = data_dict["predictions_classes"][final_rf_model.predict(input_data)[0]]
    nb_prediction = data_dict["predictions_classes"][final_nb_model.predict(input_data)[0]]
    svm_prediction = data_dict["predictions_classes"][final_svm_model.predict(input_data)[0]]

    final_prediction = mode([rf_prediction, nb_prediction, svm_prediction])[0][0]
    
    
    specialist_dict = {
    'Fungal infection': 'Dermatologist',
    'Allergy': 'Immunologist',
    'GERD': 'Gastroenterologist',
    'Chronic cholestasis': 'Hepatologist',
    'Drug Reaction': 'Internal Medicine Specialist',
    'Peptic ulcer disease': 'Gastroenterologist',
    'AIDS': 'Infectious Disease Specialist',
    'Diabetes': 'Endocrinologist',
    'Bronchial Asthma': 'Pulmonologist',
    'Hypertension': 'Cardiologist',
    'Migraine': 'Neurologist',
    'Cervical spondylosis': 'Orthopedic Surgeon',
    'Paralysis (brain hemorrhage)': 'Neurologist',
    'Jaundice': 'Gastroenterologist',
    'Malaria': 'Infectious Disease Specialist',
    'Chicken pox': 'Dermatologist',
    'Dengue': 'Infectious Disease Specialist',
    'Typhoid': 'Internal Medicine Specialist',
    'hepatitis A': 'Hepatologist',
    'Hepatitis B': 'Hepatologist',
    'Hepatitis C': 'Hepatologist',
    'Hepatitis D': 'Hepatologist',
    'Hepatitis E': 'Hepatologist',
    'Alcoholic hepatitis': 'Hepatologist',
    'Tuberculosis': 'Pulmonologist',
    'Common Cold': 'General Practitioner',
    'Pneumonia': 'Pulmonologist',
    'Dimorphic hemorrhoids(piles)': 'General Surgeon',
    'Heart attack': 'Cardiologist',
    'Varicose veins': 'Vascular Surgeon',
    'Hypothyroidism': 'Endocrinologist',
    'Hyperthyroidism': 'Endocrinologist',
    'Hypoglycemia': 'Endocrinologist',
    'Osteoarthritis': 'Orthopedic Surgeon',
    'Arthritis': 'Orthopedic Surgeon',
    '(vertigo) Paroymsal Positional Vertigo': 'Otolaryngologist',
    'Acne': 'Dermatologist',
    'Psoriasis': 'Dermatologist',
    'Impetigo': 'Dermatologist',
    'Urinary tract infection': 'Urologist'
}

    specialist_rf = specialist_dict.get(rf_prediction, "Can't specify a specialist.")
    specialist_nb = specialist_dict.get(nb_prediction, "Can't specify a specialist.")
    specialist_svm = specialist_dict.get(svm_prediction, "Can't specify a specialist.")

    if(specialist_rf == specialist_nb and specialist_nb == specialist_svm):
        specialist = specialist_rf
    elif(specialist_rf == specialist_nb):
        specialist = specialist_rf
    elif(specialist_nb == specialist_svm):
        specialist = specialist_nb
    elif(specialist_rf == specialist_svm):
        specialist = specialist_svm
    else:
        specialist = "Can't specify a speacialist."
    
    predictions = {
        "rf_model_prediction": rf_prediction,
        "naive_bayes_prediction": nb_prediction,
        "svm_model_prediction": svm_prediction,
        "final_prediction":final_prediction,
        "specialist": specialist
    }

    return jsonify(predictions)

if __name__ == "__main__":
    app.run(debug=True)