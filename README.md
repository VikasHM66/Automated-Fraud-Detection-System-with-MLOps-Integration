# Automated Fraud Detection System with MLOps

## Contents

- ### Project Description:
This project demonstrates a comprehensive machine learning operations (MLOps) pipeline for detecting fraudulent credit card transactions. The system is designed to ensure reproducibility, scalability, and seamless deployment using a combination of Mlflow, Flask, Docker, Kubernetes, and GitLab CI/CD.

- ### Introduction:
The goal of this project is to develop an automated fraud detection system for credit card transactions. This project covers the full machine learning lifecycle, from data preprocessing and model training to deployment and monitoring.

- ### Features:
 - MLOps Pipeline: Utilizes Mlflow for experiment tracking, model training, and deployment.
 - Web Application: A Flask-based web app for serving predictions with a user-friendly interface.
 - Containerization: Uses Docker to containerize the application.
 - Orchestration: Deploys using Kubernetes with Minikube for scalability.
 - CI/CD: Implements GitLab CI/CD for automated build, test, and deployment processes.

- ### Architecture:
 - Data Preprocessing: Cleans and preprocesses data for model training.
 - Model Training: Trains and evaluates machine learning models using Mlflow.
 - Model Deployment: Deploys the trained model as a Flask web service.
 - Containerization: Packages the application in Docker containers.
 - Orchestration: Manages containers using Kubernetes.
 - CI/CD Pipeline: Automates the workflow using GitLab CI/CD.
