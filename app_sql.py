import streamlit as st
import sqlite3
import re
import base64

def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    
    page_bg = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center center;
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

def create_database():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Employees (
                        ID INTEGER PRIMARY KEY,
                        Name TEXT,
                        Department TEXT,
                        Salary INTEGER,
                        Hire_Date TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Departments (
                        ID INTEGER PRIMARY KEY,
                        Name TEXT,
                        Manager TEXT)''')
    
    cursor.execute("DELETE FROM Employees")
    cursor.execute("DELETE FROM Departments")
    
    employees_data = [
        (1, "Alice", "Sales", 50000, "2021-01-15"),
        (2, "Bob", "Engineering", 70000, "2020-06-10"),
        (3, "Charlie", "Marketing", 60000, "2022-03-20")
    ]
    
    departments_data = [
        (1, "Sales", "Alice"),
        (2, "Engineering", "Bob"),
        (3, "Marketing", "Charlie")
    ]
    
    cursor.executemany("INSERT INTO Employees VALUES (?, ?, ?, ?, ?)", employees_data)
    cursor.executemany("INSERT INTO Departments VALUES (?, ?, ?)", departments_data)
    
    conn.commit()
    conn.close()

def get_response(query):
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    
    query = query.lower()
    
    try:
        if "show me all employees in the" in query:
            department = re.search(r"in the (.+?) department", query)
            if department:
                dept_name = department.group(1).capitalize()
                cursor.execute("SELECT Name FROM Employees WHERE Department = ?", (dept_name,))
                result = cursor.fetchall()
                response = [row[0] for row in result] or ["No employees found."]
            else:
                response = ["Invalid department format."]
        
        elif "who is the manager of the" in query:
            department = re.search(r"of the (.+?) department", query)
            if department:
                dept_name = department.group(1).capitalize()
                cursor.execute("SELECT Manager FROM Departments WHERE Name = ?", (dept_name,))
                result = cursor.fetchone()
                response = [result[0]] if result else ["No manager found."]
            else:
                response = ["Invalid department format."]
        
        elif "list all employees hired after" in query:
            date_match = re.search(r"after (\d{4}-\d{2}-\d{2})", query)
            if date_match:
                hire_date = date_match.group(1)
                cursor.execute("SELECT Name FROM Employees WHERE Hire_Date > ?", (hire_date,))
                result = cursor.fetchall()
                response = [row[0] for row in result] or ["No employees found."]
            else:
                response = ["Invalid date format. Use YYYY-MM-DD."]
        
        elif "total salary expense for the" in query:
            department = re.search(r"for the (.+?) department", query)
            if department:
                dept_name = department.group(1).capitalize()
                cursor.execute("SELECT SUM(Salary) FROM Employees WHERE Department = ?", (dept_name,))
                result = cursor.fetchone()
                response = [f"Total salary expense: ${result[0]:,}"] if result[0] else ["No salary data found."]
            else:
                response = ["Invalid department format."]
        
        else:
            response = ["Sorry, I don't understand that query."]
    
    except Exception as e:
        response = [f"Error: {str(e)}"]
    
    conn.close()
    return response

# Streamlit UI
st.set_page_config(page_title="Employee Chat Assistant", page_icon="💬")
st.markdown("<h1 style='text-align: center; color: black;'>Employee Chat Assistant</h1>", unsafe_allow_html=True)
set_background("chatbot.png")

st.markdown("<h3 style='color: black;'>Ask a question about employees and departments.</h3>", unsafe_allow_html=True)

create_database()

user_query = st.text_input("Enter your query:", placeholder="Type your question here...")
if st.button("Ask 💬"): 
    if user_query:
        response = get_response(user_query)
        st.success("Response:")
        for res in response:
            st.markdown(f"<p style='color: black;'>{res}</p>", unsafe_allow_html=True)  # Change response color to black
    else:
        st.warning("Please enter a query.")
