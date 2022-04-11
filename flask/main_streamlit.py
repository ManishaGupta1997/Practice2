from flask import Flask, request
import streamlit as st


def hello():

    try :
        st.title("Learning Streamlit")  #page title
        stu_name = st.text_input("StudentName") #input func like python
        numb = st.text_input("RollNo")
        #return "Oops something went wrong", 400
        
        result = f"Student name is {stu_name} and roll no is {numb}"  #gives reults
        if st.button("Print output"):  
            st.success(result)  #press button
    except Exception as e :
        return f" Error occuredd with message : {e}"

if __name__=="__main__":  #done done name
    hello()
