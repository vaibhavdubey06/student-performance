# 🎓 Student Exam Performance Predictor## End to End Machine Learning Project



[![CI Pipeline](https://github.com/vaibhavdubey06/student-performance/actions/workflows/ci.yml/badge.svg)](https://github.com/vaibhavdubey06/student-performance/actions/workflows/ci.yml)# 🎓 Student Exam Performance Indicator

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)

[![Flask](https://img.shields.io/badge/flask-3.0-green.svg)](https://flask.palletsprojects.com/)🚀 **Live Demo:** https://mlproject-a8sw.onrender.com  

[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)An end-to-end **Machine Learning web application** that predicts a student’s **mathematics exam score** based on demographic information and academic performance.  

The project demonstrates the complete ML lifecycle — from data preprocessing and model training to deployment on the cloud.

🚀 **Live Demo:** [https://mlproject-a8sw.onrender.com](https://mlproject-a8sw.onrender.com)

---

An **end-to-end Machine Learning web application** that predicts a student's **mathematics exam score** based on demographic information and academic performance. This project demonstrates the complete ML lifecycle — from exploratory data analysis and model training to CI/CD pipelines and cloud deployment.

## 📌 Project Overview

---

The **Student Exam Performance Indicator** estimates a student’s expected math score using the following features:

## 📑 Table of Contents

- Gender  

- [Project Overview](#-project-overview)- Race/Ethnicity  

- [Features](#-features)- Parental Level of Education  

- [Tech Stack](#-tech-stack)- Lunch Type  

- [Project Structure](#-project-structure)- Test Preparation Course  

- [Machine Learning Pipeline](#-machine-learning-pipeline)- Reading Score  

- [Model Performance](#-model-performance)- Writing Score  

- [Getting Started](#-getting-started)

- [Docker Deployment](#-docker-deployment)The trained model is deployed using **Flask** and hosted on **Render**, enabling real-time predictions through a simple and user-friendly web interface.

- [CI/CD Pipeline](#-cicd-pipeline)

- [API Usage](#-api-usage)---

- [Testing](#-testing)

- [Deployment](#-deployment)## 🧠 Machine Learning Workflow



---1. **Data Ingestion**

   - Load raw dataset and split into training and testing data

## 📌 Project Overview

2. **Data Transformation**

The **Student Exam Performance Predictor** estimates a student's expected math score using the following features:   - Handle categorical and numerical features

   - Feature encoding and scaling

| Feature | Type | Description |   - Save preprocessor as an artifact

|---------|------|-------------|

| Gender | Categorical | Male/Female |3. **Model Training**

| Race/Ethnicity | Categorical | Group A-E |   - Trained and evaluated multiple regression models:

| Parental Level of Education | Categorical | Education level of parents |     - Linear Regression

| Lunch | Categorical | Standard/Free-Reduced |     - Decision Tree Regressor

| Test Preparation Course | Categorical | Completed/None |     - Random Forest Regressor

| Reading Score | Numerical | Score in reading (0-100) |     - Gradient Boosting Regressor

| Writing Score | Numerical | Score in writing (0-100) |     - AdaBoost Regressor

     - XGBoost Regressor

---     - CatBoost Regressor

   - Selected the best-performing model using **R² Score**

## ✨ Features

4. **Model Persistence**

### Core ML Features   - Saved trained model and preprocessor using pickle

- 📊 **Real-time predictions** via web interface

- 🧠 **Multiple model comparison** (Linear Regression, Ridge, Random Forest, Gradient Boosting, XGBoost)5. **Prediction Pipeline**

- 📈 **Hyperparameter tuning** with GridSearchCV   - Accepts user input

- 🔍 **Error analysis** with residual plots and slice-based metrics   - Applies preprocessing

- 🎯 **Model explainability** with permutation importance and partial dependence plots   - Generates predicted exam score

- 📉 **Bootstrap confidence intervals** for robust evaluation

6. **Deployment**

### Production Features   - Flask-based web application

- 🐳 **Docker containerization** for portable deployment   - Deployed on **Render Cloud**

- ⚡ **GitHub Actions CI/CD** with automated linting and testing

- 🧪 **Comprehensive test suite** (15+ unit tests)---

- 🔒 **Input validation** and error handling

- 📝 **Structured logging** for debugging## 🖥️ Application Features

- ☁️ **Cloud deployment** on Render

- 📊 Real-time exam score prediction  

---- 🧩 Interactive web form for user input  

- ⚙️ End-to-end ML pipeline integration  

## 🛠️ Tech Stack- ☁️ Cloud deployment with public access  



| Category | Technologies |---

|----------|--------------|

| **Language** | Python 3.11 |## 🛠️ Tech Stack

| **ML/Data** | Scikit-learn, XGBoost, Pandas, NumPy, Matplotlib, Seaborn |

| **Web Framework** | Flask, Gunicorn |- **Language:** Python  

| **Testing** | Pytest |- **Machine Learning:** Scikit-learn, CatBoost, XGBoost  

| **Linting** | Ruff |- **Data Processing:** Pandas, NumPy  

| **Containerization** | Docker, Docker Compose |- **Web Framework:** Flask  

| **CI/CD** | GitHub Actions |- **Deployment Platform:** Render  

| **Deployment** | Render |- **Version Control:** Git & GitHub  

| **Version Control** | Git, GitHub |

---

---

## 🚀 Deploy (Render)

## 📁 Project Structure

This repo is already structured for Render deployment.

```

mlproject/### Option A (recommended): Render Blueprint

├── app.py                    # Flask application entry point

├── Dockerfile                # Multi-stage production Docker build1. Push this project to GitHub.

├── docker-compose.yml        # Container orchestration2. In Render: **New → Blueprint**.

├── requirements.txt          # Python dependencies3. Select your repo.

├── pyproject.toml            # Ruff & pytest configuration4. Render will use `mlproject/render.yaml` to:

├── render.yaml               # Render deployment config   - install dependencies

├── setup.py                  # Package setup   - start the server with `gunicorn app:app`

│

├── artifacts/                # Trained models & data### Option B: Manual Web Service

│   ├── model.pkl             # Serialized ML model

│   ├── preprocessor.pkl      # Data preprocessorIf you don’t use the blueprint, configure these values:

│   ├── train.csv             # Training data

│   └── test.csv              # Test data- **Root Directory:** `mlproject`

│- **Build Command:** `pip install -r requirements.txt`

├── notebook/                 # Jupyter notebooks- **Start Command:** `gunicorn app:app`

│   ├── EDA STUDENT PERFORMANCE.ipynb

│   └── MODEL TRAINING.ipynb  # Comprehensive training notebookRender injects the `PORT` environment variable automatically; the app is coded to respect that.

│

├── src/                      # Source code### ✅ Deployment checklist

│   ├── components/           # ML pipeline components

│   │   ├── data_ingestion.py- Ensure `mlproject/artifacts/model.pkl` and `mlproject/artifacts/preprocessor.pkl` are committed to the repo (Render needs them at runtime).

│   │   ├── data_transformation.py- `requirements.txt` includes `-e .` so the `src` package is installed and imports like `from src...` work in production.

│   │   └── model_trainer.py

│   ├── pipeline/             # Prediction pipeline---

│   │   └── predict_pipeline.py

│   ├── exception.py          # Custom exceptions## 🧪 Run locally (production-like)

│   ├── logger.py             # Logging configuration

│   └── utils.py              # Utility functionsIf you want to run like production (gunicorn), use:

│

├── templates/                # HTML templates```powershell

│   ├── home.htmlcd "c:\Users\dubey\OneDrive\Desktop\Student-performance\mlproject"

│   └── index.htmlC:/Users/dubey/OneDrive/Desktop/Student-performance/.venv/Scripts/python.exe -m gunicorn app:app

│```

├── tests/                    # Unit tests

│   ├── test_app.py           # Flask endpoint tests

│   └── test_predict_pipeline.py  # Pipeline tests
│
└── logs/                     # Application logs
```

---

## 🧠 Machine Learning Pipeline

### 1. Data Ingestion
- Load raw dataset from CSV
- Split into training (80%) and testing (20%) sets
- Save artifacts for reproducibility

### 2. Data Transformation
```
Numerical Features → Median Imputer → Standard Scaler
Categorical Features → Mode Imputer → One-Hot Encoder
```

### 3. Model Training & Selection
Models evaluated with 5-fold cross-validation:
- Linear Regression ✅ (Best performer)
- Ridge Regression
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

### 4. Model Evaluation
- **Metrics:** RMSE, MAE, R² Score
- **Bootstrap confidence intervals** for uncertainty quantification
- **Slice-based analysis** for fairness evaluation
- **Robustness checks** with noisy inputs

### 5. Model Explainability
- Permutation feature importance
- Partial dependence plots
- Residual analysis

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| **Validation RMSE** | 4.96 |
| **Holdout R²** | 0.86 |
| **Baseline (Dummy) RMSE** | 14.77 |
| **Improvement over Baseline** | 66% |

### Feature Importance (Top 3)
1. **Writing Score** - Most predictive feature
2. **Reading Score** - Strong correlation with math
3. **Lunch Type** - Indicator of socioeconomic factors

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- pip or conda
- Docker (optional)

### Local Installation

```bash
# Clone the repository
git clone https://github.com/vaibhavdubey06/student-performance.git
cd student-performance/mlproject

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## 🐳 Docker Deployment

### Using Docker

```bash
# Build the image
cd mlproject
docker build -t student-performance-predictor .

# Run the container
docker run -p 8080:8080 student-performance-predictor
```

### Using Docker Compose

```bash
cd mlproject
docker-compose up --build
```

Visit `http://localhost:8080` to access the application.

### Docker Features
- **Multi-stage build** for optimized image size
- **Non-root user** for security
- **Health checks** for reliability
- **Gunicorn** production server (2 workers, 4 threads)

---

## ⚡ CI/CD Pipeline

This project uses **GitHub Actions** for continuous integration:

```yaml
On Push/PR to main:
├── 🔍 Lint (Ruff)
│   └── Code style & import checks
├── 🧪 Test (Pytest)
│   └── 15+ unit tests
└── 🏗️ Build Check
    └── Dependency verification
```

### Pipeline Status
All checks must pass before merging:
- ✅ Code formatting (Ruff)
- ✅ Import sorting
- ✅ Unit tests (15 tests)
- ✅ Build verification

---

## 📡 API Usage

### Web Interface
Navigate to the home page and fill in the student information form.

### Programmatic Access

```python
import requests

# Prediction endpoint
url = "https://mlproject-a8sw.onrender.com/predictdata"

data = {
    "gender": "male",
    "ethnicity": "group B",
    "parental_level_of_education": "bachelor's degree",
    "lunch": "standard",
    "test_preparation_course": "completed",
    "reading_score": 72,
    "writing_score": 74
}

response = requests.post(url, data=data)
print(response.text)  # Predicted math score
```

---

## 🧪 Testing

### Run All Tests

```bash
cd mlproject
pytest -v
```

### Test Coverage

| Test File | Tests | Coverage |
|-----------|-------|----------|
| `test_predict_pipeline.py` | 9 tests | CustomData, PredictPipeline |
| `test_app.py` | 6 tests | Flask endpoints, error handling |

### Sample Test Run

```
==================== test session starts ====================
collected 15 items

tests/test_app.py ......                                [ 40%]
tests/test_predict_pipeline.py .........                [100%]

==================== 15 passed in 3.87s =====================
```

---

## ☁️ Deployment

### Render (Current)

The app is deployed on Render using the blueprint configuration:

1. Push to GitHub
2. Render auto-deploys from `render.yaml`
3. Live at: https://mlproject-a8sw.onrender.com

### Deployment Checklist

- [x] `artifacts/model.pkl` committed
- [x] `artifacts/preprocessor.pkl` committed
- [x] `requirements.txt` includes all dependencies
- [x] `render.yaml` configured
- [x] Environment variables set

---

## 📈 Future Improvements

- [ ] Add Swagger/OpenAPI documentation
- [ ] Implement model monitoring & drift detection
- [ ] Add Pydantic input validation
- [ ] Set up MLflow for experiment tracking
- [ ] Add A/B testing capability
- [ ] Implement feature store

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Vaibhav Dubey**

- GitHub: [@vaibhavdubey06](https://github.com/vaibhavdubey06)

---

<p align="center">
  ⭐ Star this repository if you found it helpful!
</p>
