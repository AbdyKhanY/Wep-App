# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 12:16:52 2024

@author: USER
"""

import numpy as np
import pickle
import streamlit as st
import os
import requests

# Function to download files from GitHub
def download_file(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            f.write(response.content)
        st.write(f"Downloaded {filename} successfully")
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to download {filename} from {url}: {e}")

# URLs of the model files on GitHub
parkinsons_model_url = "https://github.com/AbdyKhanY/Mohaa/blob/4672d5b9b4cf79de5111edd89cab79590c5719b5/parkinsons_model.pkl"

# Download model files if they do not exist
if not os.path.exists('parkinsons_model.pkl'):
    st.write("Downloading model file...")
    download_file(parkinsons_model_url, 'parkinsons_model.pkl')

# Load the model
try:
    with open('parkinsons_model.pkl', 'rb') as file:
        parkinsons_model = pickle.load(file)
    st.write("Model loaded successfully")
except Exception as e:
    st.error(f"Error loading model file: {e}")

# Function for prediction
def parkinsons_disease_prediction(input_data):
    try:
        input_data_as_numpy_array = np.asarray(input_data, dtype=float)
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
        prediction = parkinsons_model.predict(input_data_reshaped)
        return 'The Person has Parkinson\'s Disease' if prediction[0] == 1 else 'The Person does not have Parkinson\'s Disease'
    except Exception as e:
        st.error(f"Error during model prediction: {e}")
        return None

def main():
    st.title('Parkinson\'s Disease Prediction Web App')

    # Getting input data from user
    input_data = []
    input_data.append(st.text_input('MDVP_Fo(Hz)'))
    input_data.append(st.text_input('MDVP_Fhi(Hz)'))
    input_data.append(st.text_input('MDVP_Flo(Hz)'))
    input_data.append(st.text_input('MDVP_Jitter(%)'))
    input_data.append(st.text_input('MDVP_Jitter(Abs)'))
    input_data.append(st.text_input('MDVP_RAP'))
    input_data.append(st.text_input('MDVP_PPQ'))
    input_data.append(st.text_input('Jitter_DDP'))
    input_data.append(st.text_input('MDVP_Shimmer'))
    input_data.append(st.text_input('MDVP_Shimmer(dB)'))
    input_data.append(st.text_input('Shimmer_APQ3'))
    input_data.append(st.text_input('Shimmer_APQ5'))
    input_data.append(st.text_input('MDVP_APQ'))
    input_data.append(st.text_input('Shimmer_DDA'))
    input_data.append(st.text_input('NHR'))
    input_data.append(st.text_input('HNR'))
    input_data.append(st.text_input('RPDE'))
    input_data.append(st.text_input('DFA'))
    input_data.append(st.text_input('spread1'))
    input_data.append(st.text_input('spread2'))
    input_data.append(st.text_input('D2'))
    input_data.append(st.text_input('PPE'))

    # Creating a button for prediction
    if st.button('Parkinsons Disease Test Result'):
        diagnosis = parkinsons_disease_prediction(input_data)
        if diagnosis:
            st.success(diagnosis)
        else:
            st.error("Please enter valid numeric values.")

if __name__ == '__main__':
    main()
