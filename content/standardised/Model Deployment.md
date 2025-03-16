---
tags:
  - deleted
  - model_architecture
aliases:
  - Deployment
---
Deploying a machine learning model involves moving it from a development environment to a production environment where it can make predictions on new data.

## Steps for Model Deployment

Model Exporting
   - Use tools like `joblib` or `pickle` to serialize the model.
     ```python
     import joblib
     joblib.dump(model, 'linear_regression_model.pkl')
     ```

Deployment Options
   - Application Integration: Embed the model into an application for real-time predictions.
   - [[API]] Deployment: Use frameworks like [[Flask]] or [[FastAPI]] to create an API endpoint for the model.
   - Automated Workflows: Integrate the model into automated data processing pipelines.
## Tools and Platforms

- [[Sklearn Pipeline]]: Streamline the deployment process by integrating [[Preprocessing]] and model steps.
- [[Gradio]]: Create user-friendly interfaces for model interaction.
- [[Streamlit.io]]

## Considerations

- [[Scalability]]: Ensure the deployment solution can handle the expected load.
- [[Model Observability]]: Implement monitoring to track model performance and detect issues.

# Deploying using [[PyCaret]]

**AWS:**  When deploying model on AWS S3, environment variables must be configured using the command-line interface. To configure AWS environment variables, type `aws configure` in terminal. The following information is required which can be generated using the Identity and Access Management (IAM) portal of your amazon console account:

- AWS Access Key ID
- AWS Secret Key Access
- Default Region Name (can be seen under Global settings on your AWS console)
- Default output format (must be left blank)

**GCP:** To deploy a model on Google Cloud Platform ('gcp'), the project must be created using the command-line or GCP console. Once the project is created, you must create a service account and download the service account key as a JSON file to set environment variables in your local environment. Learn more about it: https://cloud.google.com/docs/authentication/production

**Azure:** To deploy a model on Microsoft Azure ('azure'), environment variables for the connection string must be set in your local environment. Go to settings of storage account on Azure portal to access the connection string required.
AZURE_STORAGE_CONNECTION_STRING (required as environment variable)
Learn more about it: https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python?toc=%2Fpython%2Fazure%2FTOC.json