import streamlit as st
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

st.title("Streamlit Logging App, with button")

placeholder = st.empty()

# Input box for logging interval
interval = st.text_input("Enter logging interval (seconds):", "5")

def log_message(logging_interval):
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"Log message at {current_time}"
        
        # Log to Streamlit
        placeholder.text(message)
        
        # Log to standard output
        logging.info(message)
        
        time.sleep(logging_interval)

if st.button('Start Logging'):
    try:
        logging_interval = int(interval)
        if logging_interval <= 0:
            st.error("Logging interval must be a positive integer.")
        else:
            log_message(logging_interval)
    except ValueError:
        st.error("Please enter a valid integer for the logging interval.")
