# Real Estate Price Predictor 🏠

A sleek, professional, and interactive web application built with Dash to predict real estate prices based on user inputs and uploaded Excel data. The app leverages a trained Random Forest regression model for accurate price prediction in both USD and INR.

## Table of Contents
- [About](#about)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Model](#model)
- [File Upload](#file-upload)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About
This application allows users to upload an Excel file containing real estate data and then input parameters such as location, property size, and number of rooms to predict the price. The app uses a Random Forest regression model trained to estimate property prices based on features such as size, rooms, and location.

## Features
- **Excel File Upload**: Users can upload an Excel file (.xlsx) with property data.
- **Dynamic Input Form**: Select location and enter property size and rooms.
- **Price Prediction**: Predicts real estate prices in both USD and INR (currency conversion included).
- **User-Friendly UI**: Clean, modern design with Google Fonts and responsive layout.
- **Error Handling**: Validates user inputs and file upload status.

## Demo
_Add a GIF or screenshot here to showcase your app interface._

## Installation
### Clone the repository:
```bash
git clone https://github.com/yourusername/real-estate-price-predictor.git
cd real-estate-price-predictor
```
Features include:
Property size (sqft)

Number of rooms

Location (One-hot encoded: Downtown, Suburb, Uptown)

Currency conversion from USD to INR uses a static rate (1 USD = 83.5 INR).
File Upload
Supported format: .xlsx (Excel file)

Upon successful upload, the app enables the input form to enter details for price prediction.

Handles file reading errors gracefully.

Technologies Used
Python 3.8+

Dash - For web app framework

Pandas - Data processing

NumPy - Numerical operations

Scikit-learn - Machine Learning model loading

Joblib - Model serialization

Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
Developed by Darshan M N


