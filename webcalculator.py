import streamlit as st
def calculate(num1, num2, operation):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
def main():
    st.title("Simple Calculator")
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number", value=0.0)
    with col2:
        num2 = st.number_input("Enter second number", value=0.0)
    col3, col4 = st.columns(2)
    with col3:
        add_button = st.button("Add")
        multiply_button = st.button("Multiply")
    with col4:
        subtract_button = st.button("Subtract")
        divide_button = st.button("Divide")    
    if add_button:
        result = calculate(num1, num2, "Add")
        st.success(f"Result: {result}")
    elif subtract_button:
        result = calculate(num1, num2, "Subtract")
        st.success(f"Result: {result}")
    elif multiply_button:
        result = calculate(num1, num2, "Multiply")
        st.success(f"Result: {result}")
    elif divide_button:
        result = calculate(num1, num2, "Divide")
        st.success(f"Result: {result}")
if __name__ == "__main__":
    main()