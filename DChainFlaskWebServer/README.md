# DocuChainFlaskServer

- A simple flask server for predicting diseases based on the given input which can be deployed on GCP.
- It takes 132 chars long symptoms string and predicts the disease using custom machine learning model.

## Running locally

- Make sure you install the required modules.
- Run main.py
- Now you can request on localhost:5000/predict/symptomsString

You can take a look at sample.csv for understanding the features.

Example request:
http://127.0.0.1:5000/predict/111000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000


Output:
```json
{
  "final_prediction": "F",
  "naive_bayes_prediction": "Fungal infection",
  "rf_model_prediction": "Fungal infection",
  "svm_model_prediction": "Fungal infection",
  "specialist": "Dermatologist"
}
```


Model can predict the following 41 diseases:
| Disease | Disease | Disease |
| --- | --- | --- |
|Fungal infection|Allergy|GERD|
|Chronic cholestasis|Drug Reaction|Peptic ulcer diseae|
|AIDS|Diabetes|Bronchial Asthma|
|Hypertension|Migraine|Cervical spondylosis|
|Paralysis (brain hemorrhage)|Jaundice|Malaria|
|Chicken pox|Dengue|Typhoid|
|hepatitis A|Hepatitis B|Hepatitis C|
|Hepatitis D|Hepatitis E|Alcoholic hepatitis|
|Tuberculosis|Common Cold|Pneumonia|
|Dimorphic hemmorhoids(piles)|Heart attack|Varicose veins|
|Hypothyroidism|Hyperthyroidism|Hypoglycemia|
|Osteoarthristis|Arthritis|(vertigo) Paroymsal  Positional Vertigo|
|Acne|Urinary tract infection|Psoriasis|
|Impetigo|NaN|NaN|


Do hit the ⭐ button if this helped you!!
