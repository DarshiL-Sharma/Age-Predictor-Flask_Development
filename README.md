# Age-Predictor-Flask_Development
An age prediction web app where users enter a name and the server retrieves an estimated age using an external API. The project focuses on backend fundamentals, API integration, and building interactive web applications.
# Age Predictor Web App

A Flask-based web application that estimates a person's age using their name. The application integrates with the Agify API, which analyzes datasets of names and ages to return a predicted average age. This project demonstrates backend development, API integration, routing, and frontend interaction.

---

# Overview
This project allows users to input a name and receive an estimated age. The backend server communicates with an external API that processes statistical data and returns a predicted age. The result is then displayed on a dynamic webpage.

The purpose of this project is to demonstrate how web servers interact with APIs and how data flows between the frontend and backend of a web application.

---

# How the Age Prediction Works

1. A user enters a name into the input field.
2. JavaScript captures the form submission.
3. The browser redirects the request to the route `/name/<name>`.
4. The Flask backend receives the request.
5. The server sends a GET request to the Agify API.
6. The API processes the name using its dataset.
7. A JSON response containing the predicted age is returned.
8. Flask renders the result using a template.

Example request to the API:

https://api.agify.io?name=emma

Example response:

{
  "name": "emma",
  "age": 28,
  "count": 15000
}

The returned age represents the average predicted age for people with that name based on available data.

---

# Technologies Used

Backend
- Python
- Flask
- Requests library

Frontend
- HTML
- CSS
- JavaScript

External Service
- Agify API

Concepts Demonstrated
- REST API integration
- JSON data handling
- Dynamic routing
- Template rendering
- Client-server communication

---

# Project Structure

project/
│
├── app.py
│
├── templates/
│   ├── home.html
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md

---

# Installation and Setup

1. Clone the repository

git clone https://github.com/yourusername/age-predictor.git

2. Navigate into the project directory

cd age-predictor

3. Install required dependencies

pip install flask requests

4. Run the application

python app.py

5. Open the application in your browser

http://localhost:5002

---

# Application Flow

User Input → JavaScript Form Handler → Flask Route → API Request → JSON Response → Render Template → Display Result

---

# Features

- Predicts age using a name
- Clean user interface
- Dynamic routing
- API data integration
- Lightweight backend server
- Simple and interactive frontend

---

# Learning Outcomes

Through this project you can learn:

- How Flask web servers work
- How to connect applications with third-party APIs
- Handling HTTP requests and responses
- Rendering dynamic templates
- Structuring a small full-stack project

---

# Possible Future Improvements

- Add gender prediction
- Add nationality prediction
- Add error handling
- Deploy the application to the cloud

---

# API Reference

Agify API  
https://agify.io

Agify predicts age using aggregated statistical data from names across different regions and datasets.
Agify provides free access of API for education and Learning .

---

# License

This project is open-source and intended for educational and learning purposes.
