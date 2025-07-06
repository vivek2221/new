import os 
import google.generativeai as genai
import gradio as gr
import streamlit as st
import speech_recognition as sr
import pywhatkit
import pandas as pd
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Wedding Invitation", layout="centered")


    st.markdown("## 💍 Wedding Invitation App")
    st.write("🎙️ Click the button below and speak the guest's name.")
    name_list = ['vivek', 'bhavya']
    phone_list = ['7806046570', '9602398321']
    prefix = "+91"
    invitation_text = "pls come to our wedding"
    if st.button("🎤 Start Listening"):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            st.info("Listening... Please speak now.")
            audio = r.listen(source)
    
        try:
            spoken_text = r.recognize_google(audio).lower()
            st.success(f"✅ You said: **{spoken_text}**")

        
            for i, guest_name in enumerate(name_list):
                if guest_name in spoken_text:
                    phone = phone_list[i]
                    full_msg = guest_name + invitation_text
                    full_number = prefix + phone

                    st.markdown(f"**📲 Sending invitation to {guest_name} at {full_number}**")
                    st.markdown(f"**✉️ Message:** {full_msg}")

                    pywhatkit.sendwhatmsg_instantly(full_number, full_msg)
                    break
                else:
                    st.warning("⚠️ Name not recognized. Please try again.")

        except sr.UnknownValueError:
            st.error("😕 Sorry, I couldn’t understand your voice.")
        except sr.RequestError as e:
            st.error(f"🛑 Could not complete the request: {e}")