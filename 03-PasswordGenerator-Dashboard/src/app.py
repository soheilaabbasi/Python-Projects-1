import streamlit as st
from password_generators import RandomPasswordGenerator, MemorablePasswordGenerator, PinGenerator
from nltk.corpus import words


#  * Title of the application
st.image('./images/banner.jpeg', width=400)
st.title(":zap: Password Generator")

option = st.radio("Select the type of password you want to generate:",
                    ("Random Password", "Memorable Password", "PIN Code"))

if option == 'PIN Code':
    length = st.slider("Select the length of the PIN code:", min_value=4, max_value=32, value=4)

    generator = PinGenerator(length)

elif option == 'Random Password':
    length = st.slider("Select the length of the password:", min_value=8, max_value=100, value=8)
    include_number = st.toggle("Include numbers", value=True)
    include_symbol = st.toggle("Include symbols", value=True)

    generator = RandomPasswordGenerator(length, include_number, include_symbol)

elif option == 'Memorable Password':
    num_of_words = st.slider("Select the number of words in the password:", 2, 10, 4)
    separator = st.text_input("Separator", value="-")
    capitalization = st.toggle("Capitalization")

    generator = MemorablePasswordGenerator(num_of_words, separator, capitalization, words.words())


password = generator.generate()
st.write(fr"Your password is: ``` {password} ``` ")
