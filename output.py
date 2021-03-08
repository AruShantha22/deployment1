import streamlit as st
import numpy as np
import pandas as pd
from pickle import dump,load

clf1 = load(open('pickle10/svcliner.pkl', 'rb'))
def main():
    st.title('svm rbf predictions')
    col1=st.number_input('Enter col1 values')
    col2=st.number_input('Enter col2 values')
    if st.button('predict'):
        st.write(np.array(clf1.predict([[col1,col2]])))

if (__name__=='__main__'):
    main()
