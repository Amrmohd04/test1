import streamlit as st

# Function to diagnose skin diseases based on symptoms
def diagnose_skin_disease(symptoms):
    # Replace this with your disease prediction logic
    # In a real-world scenario, you'd use a machine learning model
    # to predict the disease based on the symptoms provided.
    # For simplicity, this example just returns a static result.
    if 'rash' in symptoms:
        return "You might have a skin rash."
    else:
        return "No specific diagnosis could be made."

# Streamlit app
def main():
    st.title("Skin Disease Diagnosis App")
    st.write("Enter your symptoms to get a preliminary diagnosis.")

    # Get user input
    symptoms = st.text_input("Enter your symptoms (comma-separated):")

    if st.button("Diagnose"):
        if symptoms:
            symptom_list = [sym.strip() for sym in symptoms.split(',')]
            diagnosis = diagnose_skin_disease(symptom_list)
            st.write("Diagnosis:", diagnosis)
        else:
            st.write("Please enter your symptoms.")

if __name__ == "__main__":
    main()

import streamlit as st
from skindiseases import skindiseases

# Function to diagnose skin diseases based on symptoms
def diagnose_skin_disease(symptoms):
    possible_diseases = []

    for disease in skin_diseases:
        matching_symptoms = [symptom for symptom in symptoms if symptom in disease["symptoms"]]
        if len(matching_symptoms) > 0:
            possible_diseases.append(disease["name"])

    if possible_diseases:
        return f"You might have: {', '.join(possible_diseases)}"
    else:
        return "No specific diagnosis could be made."

# Streamlit app
def main():
    st.title("Skin Disease Diagnosis App")
    st.write("Enter your symptoms to get a preliminary diagnosis.")

    # Get user input
    symptoms = st.text_input("Enter your symptoms (comma-separated):")

    if st.button("Diagnose"):
        if symptoms:
            symptom_list = [sym.strip() for sym in symptoms.split(',')]
            diagnosis = diagnose_skin_disease(symptom_list)
            st.write("Diagnosis:", diagnosis)
        else:
            st.write("Please enter your symptoms.")

if __name__ == "__main__":
    main()
