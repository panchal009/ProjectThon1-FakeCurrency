 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)

# loading the trained model
pickle_scaler = open('scaler.pkl', 'rb') 
scaler = pickle.load(pickle_scaler)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(var, skew, curt, entr):   
  
    x_test = scaler.transform([[var, skew, curt, entr]])
    # Making predictions 
    prediction = classifier.predict(x_test)
     
    if prediction == 0:
        pred = 'Not Fake'
    else:
        pred = 'Fake'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">PragyanAI Fake Currency Detection Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
    # 'var', 'skew', 'curt', 'entr
    # following lines create boxes in which user can enter data required to make prediction 
    var = st.number_input(label="Enter Variance value",step=1,format=“%.2f”)
    skew = st.number_input(label="Enter skew value",step=1,format=“%.2f”)
    curt = st.number_input(label="Enter curt value",step=1,format=“%.2f”)
    entr = st.number_input(label="Enter entr value",step=1,format=“%.2f”)
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(var, skew, curt, entr) 
        st.success('The Currency is {}'.format(result))
        print(LoanAmount)
     
if __name__=='__main__': 
    main()
