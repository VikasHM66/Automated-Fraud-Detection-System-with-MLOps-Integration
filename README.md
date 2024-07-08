# Automated Fraud Detection System with MLOps

## Contents

- ### Project Description:
This project demonstrates a comprehensive machine learning operations (MLOps) pipeline for detecting fraudulent credit card transactions. The system is designed to ensure reproducibility, scalability, and seamless deployment using a combination of Mlflow, Flask, Docker, Kubernetes, and GitLab CI/CD.
## Libraries and Tools Used

<p align="left">
  <a href="https://www.python.org/" target="_blank">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python" width="40" height="40"/>
  </a>
  <a href="https://flask.palletsprojects.com/" target="_blank">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/flask/flask-original.svg" alt="Flask" width="40" height="40"/>
  </a>
  <a href="https://www.docker.com/" target="_blank">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original.svg" alt="Docker" width="40" height="40"/>
  </a>
  <a href="https://kubernetes.io/" target="_blank">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/kubernetes/kubernetes-plain.svg" alt="Kubernetes" width="40" height="40"/>
  </a>
  <a href="https://mlflow.org/" target="_blank">
    <img src="https://github.com/mlflow/mlflow/blob/master/docs/source/images/favicon.ico" alt="MLflow" width="40" height="40"/>
  </a>
  <a href="https://gitlab.com/" target="_blank">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/gitlab/gitlab-original.svg" alt="GitLab" width="40" height="40"/>
  </a>
  <a href="https://jupyter.org/" target="_blank">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/jupyter/jupyter-original.svg" alt="Jupyter" width="40" height="40"/>
  </a>
  <a href="https://scikit-learn.org/" target="_blank">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/scikit-learn/scikit-learn-original.svg" alt="Scikit-Learn" width="40" height="40"/>
  </a>
  <a href="https://pandas.pydata.org/" target="_blank">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" alt="Pandas" width="40" height="40"/>
  </a>
  <a href="https://numpy.org/" target="_blank">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg" alt="NumPy" width="40" height="40"/>
  </a>
</p>


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
