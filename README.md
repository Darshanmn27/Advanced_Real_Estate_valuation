
# Real Estate Price Predictor 🏠

A sleek, professional, and interactive web application built with **Dash** to predict real estate prices based on user inputs and uploaded Excel data. The app leverages a trained Random Forest regression model for accurate price prediction in both **USD** and **INR**.

---

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

---

## About

This application allows users to upload an Excel file containing real estate data and then input parameters such as location, property size, and number of rooms to predict the price. The app uses a **Random Forest regression model** trained to estimate property prices based on features such as size, rooms, and location.

---

## Features

- 📤 **Excel File Upload**: Users can upload an Excel file (.xlsx) with property data.
- 🧾 **Dynamic Input Form**: Select location and enter property size and rooms.
- 💰 **Price Prediction**: Predicts real estate prices in both USD and INR (currency conversion included).
- 🎨 **User-Friendly UI**: Clean, modern design with Google Fonts and responsive layout.
- ✅ **Error Handling**: Validates user inputs and file upload status.

---

## Demo

_Add a GIF or screenshot here to showcase your app interface._

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Darshanmn27/real-estate-price-predictor.git
cd real-estate-price-predictor
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate       # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Run the app locally:

```bash
python app.py
```

Then open your browser and navigate to: `http://127.0.0.1:8050/`

---

## Model

The app uses a pre-trained **Random Forest Regressor** model saved as `models/Random_Forest.pkl`.

### Features used in the model:
- 📏 Property Size (sqft)
- 🛏️ Number of Rooms
- 📍 Location (One-hot encoded: Downtown, Suburb, Uptown)

💱 Currency conversion from **USD to INR** uses a static rate:

```text
1 USD = 83.5 INR
```

---

## File Upload

- Supported format: `.xlsx` (Excel file)
- Upon successful upload, the app enables the input form for price prediction
- Handles file reading errors gracefully and provides helpful messages

---

## Technologies Used

- 🐍 Python 3.8+
- 💠 Dash - For building interactive web apps
- 🧮 Pandas - For data manipulation and preprocessing
- 🔢 NumPy - For numerical computations
- 🧠 Scikit-learn - For loading the machine learning model
- 🧳 Joblib - For model serialization

---

## Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to open an issue or a pull request.  

---

## License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more details.

---

## Contact

👨‍💻 Developed by **Darshan M N**

- GitHub: [https://github.com/Darshanmn27](https://github.com/Darshanmn27)
- LinkedIn: [https://www.linkedin.com/in/darshan-m-n-7546b632b/](https://www.linkedin.com/in/darshan-m-n-7546b632b/)
- Email: darshanmn2327@gmail.com

---

*Thank you for visiting this project! If you liked it, don't forget to ⭐ the repo.*
