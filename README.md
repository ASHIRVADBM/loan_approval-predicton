📘 Loan Approval Prediction System

A complete Machine Learning project that predicts whether a loan application will be Approved or Rejected, based on applicant financial details.
Built using Python, Scikit-Learn, Streamlit, and Pandas.

🚀 Features

🔍 Data preprocessing & feature engineering

🤖 Logistic Regression model for prediction

📊 Visualizations using Matplotlib & Seaborn

🔮 Real-time prediction with a Streamlit web app

💾 Saved model & scaler (model.pkl + scaler.pkl)

📦 Virtual environment support

🧪 Train/test split & confusion matrix

📁 Project Structure
loan_approval_prediction/
│── app.py                 # Streamlit frontend
│── model.pkl              # Trained ML model
│── scaler.pkl             # StandardScaler used for preprocessing
│── requirements.txt        # Python dependencies
│── .gitignore
│── README.md
│── loan_env/ (ignored)    # Virtual environment

🛠️ Technologies Used

Python 3.12

Streamlit

Pandas

NumPy

Scikit-Learn

Matplotlib

Seaborn

⚙️ Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/yourusername/loan-approval-prediction.git
cd loan-approval-prediction

2️⃣ Create a Virtual Environment
py -3.12 -m venv loan_env


Activate:

Windows:
loan_env\Scripts\activate

Mac/Linux:
source loan_env/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Streamlit Application
streamlit run app.py


Access the app in your browser:

👉 http://localhost:8501

🧠 How the Model Works

The model uses features such as:

Number of dependents

Education level

Employment status

Annual income

Loan amount

Loan term

CIBIL score

Total assets

It uses a trained Logistic Regression model to classify:

1 → Loan Approved

0 → Loan Rejected

The inputs are scaled using a saved StandardScaler (scaler.pkl) to ensure proper prediction.

🖼️ Streamlit App Preview

The app provides:

✔ Input fields for all applicant details
✔ Real-time prediction
✔ Clean UI
✔ Easy to use

📊 Model Evaluation

The project includes:

Confusion Matrix

Accuracy Score

Data visualizations such as:

Loan status distribution

Education vs Loan Status

Self-employed vs Loan Status

🧾 Requirements
streamlit==1.32.0
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.4.2
matplotlib==3.8.4
seaborn==0.13.2
joblib==1.3.2
python-dateutil==2.9.0
pytz==2024.1

🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss what you'd like to improve.

📜 License

This project is licensed under the MIT License.

💡 Future Enhancements

Implement FastAPI backend

Deploy Streamlit app to Streamlit Cloud

Add database connection (MongoDB / SQL)

Add additional ML algorithms (XGBoost, Random Forest)

Improve UI/UX

⭐ Show Your Support

If you like this project, please star the repository ⭐ on GitHub!

If you'd like, I can also generate:

🔹 A professional project logo
🔹 A GitHub Actions CI workflow
🔹 A proper setup.bat installer
🔹 Deployment instructions
