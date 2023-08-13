import streamlit as st

# Function to diagnose skin diseases based on symptoms
def diagnose_skin_disease(symptoms):
    # Replace this with your disease prediction logic
    # In a real-world scenario, you'd use a machine learning model
    # to predict the disease based on the symptoms provided.
    # For simplicity, this example just returns a static result.
    if 'rash' in symptoms:
        return "You might have a skin rash."
    if 'eczema' in symptoms:
        return "You might have eczema."
    if 'psoriasis' in symptoms:
        return "You might have psoriasis."
    if 'acne' in symptoms:
        return "You might have acne."
    if 'dermatitis' in symptoms:
        return "You might have dermatitis."
    if 'vitiligo' in symptoms:
        return "You might have vitiligo."
    if 'rosacea' in symptoms:
        return "You might have rosacea."
    if 'hives' in symptoms:
        return "You might have hives."
    if 'melanoma' in symptoms:
        return "You might have melanoma."
    if 'lichen planus' in symptoms:
        return "You might have lichen planus."
    if 'pityriasis rosea' in symptoms:
        return "You might have pityriasis rosea."
    if 'pimples on face' in symptoms:
        return "You might have Acne."
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
