import numpy as np 
import pandas as pd 
import streamlit as st
import pickle

with open ("model.pkl","rb") as file:
    model=pickle.load(file)

with open ("scaler.pkl","rb") as file:
    scaler=pickle.load(file)

with open ("pca.pkl","rb") as file:
    pca=pickle.load(file)

def precition(input_data):
    scaled_data=sc.transform(input_data)
    pca_data=pca.transform(scaled_data)
    pred=model.predict(pca_data)[0]
    if pred==0:
        return "developed"
    elif pred == 1:
        return "developing"
    else: 
        return "under_delveloped"

def main():
    st.title("HELP INTERNATIONAL FOUNDATION")
    st.subheader("This application helps to classify the country on the basis of it's soci-economic and health factors")
    chld_mor=st.text_input("Enter child mortality rate")
    exports=st.text_input("Enter Export Per Capita")
    health=st.text_input("Enter Health Per Capita")
    imports=st.text_input("Enter Import Per Capita ")
    infl=st.text_input("Enter Inflation Rate")
    lf_exp=st.text_input("Enter Life Expentacy")
    tol_fer=st.text_input("Enter Total Fertility rate")
    gdp=st.text_input("Enter GDP Per Population")
    income=st.text_input("Enter Net Income Per Person")

    inp_list=[[chld_mor,exports,health,imports,income,infl,lf_exp,tol_fer,gdp]]

    if st.button("Predict"):
        response=prediction(inp_list)
        st.sucess(response)

if __name__=="__main__":
    main()



    

        
