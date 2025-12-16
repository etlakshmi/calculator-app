import streamlit as st
from main import add, subtract, multiply, divide
st.title("Simple Calculator")
Number1=st.number_input("Enter the first number:",value=0.0)
Number2=st.number_input("Enter the second number:",value=0.0)
operation=st.selectbox("Select Operation:",("Addition(+)","Subtraction(-)","Multiplication(*)","Division(/)"))
if st.button("Calculate"):
    if operation=="Addition(+)":
        result=add(Number1,Number2)
    elif operation=="Subtraction(-)":
        result=subtract(Number1,Number2)
    elif operation=="Multiplication(*)":
        result=multiply(Number1,Number2)
    elif operation=="Division(/)":
        result=divide(Number1,Number2)
    st.success(f"Result: {result}")
