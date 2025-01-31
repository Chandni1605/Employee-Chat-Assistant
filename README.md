# Employee-Chat-Assistant
### Project Title: Employee Chat Assistant

### Description:

#### The Employee Chat Assistant is an interactive web application built using Streamlit and SQLite that allows users to query information about employees and departments within a company. This assistant responds to a variety of queries related to employee details, department managers, and salary expenses. The system is designed to offer a user-friendly interface, allowing users to interact with the database seamlessly through simple natural language queries.

#### Technologies Used:

#### Streamlit: A Python library used to build the interactive front-end of the chatbot.
#### SQLite: A lightweight, serverless relational database used to store information about employees and departments.
#### Python: The core programming language that powers the backend logic and query processing.
#### Regular Expressions (regex): Used to extract specific data from user queries.
#### Base64: Used to encode an image for use as the background of the app interface.

### Key Features:

#### Background Image: The application allows the addition of a custom background image, making the UI visually appealing.
#### Employee Data: The app has a built-in SQLite database that stores information about employees, including their name, department, salary, and hire date.
#### Department Data: The database also stores information about departments, including the department's name and manager.
#### Natural Language Processing: Users can ask questions in natural language (e.g., "Who is the manager of the Sales department?" or "List all employees hired after 2021-01-01"), and the app will process the query and return the relevant data.
#### Dynamic Query Handling: The app can respond to multiple types of queries, including:
#### Employees in a specific department
#### The manager of a department
#### Employees hired after a certain date
#### The total salary expense for a department
#### Real-time Interactivity: The app allows users to enter their query through a text input field, and responses are dynamically displayed after each query.

### Database Structure:

### Employees Table:
#### ID: Unique identifier for each employee.
#### Name: The name of the employee.
#### Department: The department where the employee works.
#### Salary: The salary of the employee.
#### Hire_Date: The date when the employee was hired.
### Departments Table:
#### ID: Unique identifier for each department.
#### Name: The name of the department.
#### Manager: The name of the manager of the department.

### User Interaction:

The user opens the Streamlit app and is presented with a clean, visually appealing interface.
The user is prompted to type a query about employees and departments.
Upon clicking the "Ask" button, the query is processed and the relevant information is retrieved from the database.
The assistant displays the answer to the user, with each response rendered in black text for clarity.
Deployment:

#### The application can be deployed using Streamlit Sharing, Heroku, or other cloud platforms, providing a publicly accessible URL for users to interact with the chatbot.

### Future Improvements:

#### Natural Language Understanding: Enhancing the app's ability to handle more complex queries and natural language variations.
Expanded Database: Adding more fields to the employee and department records, such as employee job titles, contact details, or project assignments.
User Authentication: Adding user login functionality to restrict access to certain features or data.
This chatbot serves as a great starting point for integrating natural language processing into business applications, offering a simple yet effective way to interact with company data.
