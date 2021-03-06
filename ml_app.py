import streamlit as st
from sklearn.linear_model import LogisticRegression
from pickle import dump, load


classifier = load(open('pickle1/logit1_model.pkl', 'rb'))


def prediction(tenure, StreamingTV, StreamingMovies, MonthlyCharges,TotalCharges, MultipleLines_Yes, InternetService_Fiberoptic,InternetService_No, Contract_Oneyear, Contract_Twoyear):
    if tenure=='Yes':
        tenure = 1
    else:
        tenure= 0
    if StreamingTV =='Yes':
        StreamingTV=1
    else:
        StreamingTV=0
    if StreamingMovies=='Yes':
        StreamingMovies=1
    else:
        StreamingMovies=0
    if MonthlyCharges=='Yes':
        MonthlyCharges=1
    else:
        MonthlyCharges=0
    if TotalCharges=='Yes':
        TotalCharges=1
    else:
        TotalCharges=0
    if MultipleLines_Yes=='Yes':
        MultipleLines_Yes=1
    else:
        MultipleLines_Yes=0
    if InternetService_Fiberoptic=='Yes':
        InternetService_Fiberoptic=1
    else:
        InternetService_Fiberoptic=0
    if InternetService_No =='Yes':
        InternetService_No=1
    else:
        InternetService_No=0
    if Contract_Oneyear=='Yes':
        Contract_Oneyear=1
    else:
        Contract_Oneyear=0

    if Contract_Twoyear=='Yes':
        Contract_Twoyear=1
    else:
        Contract_Twoyear=0

    prediction=classifier.predict([[tenure, StreamingTV, StreamingMovies, MonthlyCharges,TotalCharges, MultipleLines_Yes, InternetService_Fiberoptic,InternetService_No, Contract_Oneyear, Contract_Twoyear]])
    if prediction==1:
        pred='Continue'
    else:
        pred='Not Continue'
    return pred

def main():
    st.header('LogisticRegression Model predictions')

    tenure=st.number_input('Enter the total number of months the customer has been with the company')
    StreamingTV=st.selectbox('whether the customer has StreamingTV or not',('Yes','No'))
    StreamingMovies=st.selectbox('whether the customer has StreamingMovies or not',('Yes','No'))
    MonthlyCharges=st.number_input('Enter the Monthly amount Charged to the customer')
    TotalCharges=st.number_input(' Enter the Total amount charged to the customer')
    MultipleLines_Yes=st.selectbox('whether the customer has multiple lines or not',('Yes','No'))
    InternetService_Fiberoptic=st.selectbox('InternetService',('Yes','No'))
    InternetService_No=st.selectbox('InternetService is no',('Yes'))
    Contract_Oneyear=st.selectbox('select if Term of the customer contract for one year',('Yes','No'))
    Contract_Twoyear=st.selectbox('select if Term of the customer contract for two years',('Yes','No'))


    if st.button('predict'):
        churn_predict=prediction(tenure, StreamingTV, StreamingMovies, MonthlyCharges,TotalCharges, MultipleLines_Yes, InternetService_Fiberoptic,InternetService_No, Contract_Oneyear, Contract_Twoyear)
        st.info('Having subscribtion {}'.format(churn_predict))
if __name__=='__main__':
    main()
