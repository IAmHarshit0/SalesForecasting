import streamlit as st
import pandas as pd 
import pickle
import numpy as np
import matplotlib.pyplot as plt

st.title(f'Sales forecasting')

model = pickle.load(open('model.pkl', 'rb'))
encode = pickle.load(open('encode.pkl', 'rb'))

col1, col2 = st.columns(2, gap='medium')

with col1:
    wt = st.number_input("Weight Of The Item", value=6.30)
    vis = st.number_input("Item Visibility", value=0.12)
    item = st.selectbox(label="Item Type", options=['Food', 'Drinks', 'Non-Consumable'])
    location = st.selectbox(label="Outlet Location Type", options=['Tier 1', 'Tier 2', 'Tier 3'])
    identifier = st.selectbox(label="Outlet Identifier", options=['OUT049', 'OUT018', 'OUT010', 'OUT013', 'OUT027', 'OUT045', 'OUT017', 'OUT046', 'OUT035', 'OUT019'])


with col2:
    fat = st.selectbox(label="Item Fat Content", options=['Low Fat', 'Regular', 'Non-Edible'])
    mrp = st.number_input("Item MRP", value=95.64)
    size = st.selectbox(label="Outlet Size", options=['Small', 'Medium', 'High'])
    outlet = st.selectbox(label="Outlet Type", options=['Supermarket Type1', 'Supermarket Type2', 'Supermarket Type3', 'Grocery Store'])
    years = st.slider(label="Outlet Years", min_value=15, max_value=50, value=30)

user_input = {
    'New_Item_Type': item,
    'Outlet_Location_Type': location,
    'Item_Fat_Content': fat,
    'Outlet_Size': size,
    'Outlet_Type': outlet,
    'Outlet_Identifier': identifier
}

encoded_inputs = []

# Apply encoding using stored LabelEncoders
for col, val in user_input.items():
    le = encode[col]
    if val in le.classes_:
        encoded = le.transform([val])[0]
    else:
        st.error(f"'{val}' not found in encoder for '{col}'.")
        st.stop()
    encoded_inputs.append(encoded)

final_input = [
    wt,                                # Item_Weight
    encoded_inputs[0],                 # Item_Fat_Content
    vis,                               # Item_Visibility
    mrp,                               # Item_MRP
    encoded_inputs[1],                 # Outlet_Size
    encoded_inputs[2],                 # Outlet_Location_Type
    encoded_inputs[3],                 # Outlet_Type
    encoded_inputs[4],                 # New_Item_Type
    years,                             # Outlet_Years
    encoded_inputs[5]                  # Outlet (from Outlet_Identifier)
]


if st.button("Predict Sales"):
    pred = model.predict([final_input])[0]
    st.success(f"Predicted Sales: ₹{pred:.2f} Lakh")
