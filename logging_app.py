import streamlit as st
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

st.title("Streamlit Logging App")

placeholder = st.empty()

def log_message():
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"Log message at {current_time}"
        
        # Log to Streamlit
        placeholder.text(message)
        
        # Log to standard output
        logging.info(message)
        
        time.sleep(5)

if st.button('Start Logging'):
    log_message()
