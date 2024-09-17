import streamlit as st
import random

# Character list for generating passwords
char_list = [
    "A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H",
    "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o",
    "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W",
    "w", "X", "x", "Y", "y", "Z", "z", "0", "1", "2", "3", "4", "5", "6", "7",
    "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+",
    "=", "{", "}", "[", "]", "|", "\\", ":", ";", "\"", "'", "<", ">", ",",
    ".", "?", "/", "`", "~"
]

# Title of the app
st.title("Welcome to Password Generator")

# Slider to choose password length
length = st.slider("Select password length:",
                   min_value=8,
                   max_value=48,
                   value=15)
# Button to generate the password
if st.button("Generate Password"):
    # Generate password using random.choices to allow repetition of characters
    password_ = random.choices(char_list, k=length)
    _password_ = "".join(password_)

    # Display the generated password
    st.success(f"Your password is: {_password_}")
    st.write(f"Your password is: {_password_}")
else:
    # If the button is not clicked, display this info message
    st.info("Please click the button to generate a password.")
