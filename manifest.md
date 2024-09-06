# Kubernetes Manifest Generator

This is a Python script to generate Kubernetes deployment and service YAML files. You can use this tool to quickly create manifest files for deploying applications in Kubernetes clusters, including handling different service types such as `ClusterIP`, `NodePort`, and `LoadBalancer`.

## Features

- Generate `Deployment` YAML with customizable:
  - Application name
  - Docker image
  - Number of replicas
  - Container port
- Generate `Service` YAML with customizable:
  - Service type (`ClusterIP`, `NodePort`, `LoadBalancer`)
  - Service port and target port
  - Automatic NodePort generation in the range of 30000-32767 for NodePort services

## Requirements

- Python 3.x
- PyYAML library (`pip install pyyaml`)

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/muzafferjoya/K8s-manifest-generator.git
cd K8s-manifest-generator
```

2. Install Dependencies
Install the required PyYAML package using pip:

```bash
pip install pyyaml
```

3. Run the Script
Run the script and follow the prompts to generate your Kubernetes manifest files.

```bash
python3 manifest_generator.py
```

You will be prompted to enter the following details:

Application Name: The name of your Kubernetes deployment and service.
Docker Image Name: The Docker image you want to deploy.
Replicas: The number of pod replicas.
Container Port: The container's internal port.
Service Port: The external port for the service.
Service Type: The type of Kubernetes service (ClusterIP, NodePort, or LoadBalancer).

Example
Here is an example of how the script runs:

Enter the application name: pets-api
Enter the Docker image name: pets-api:latest
Enter the number of replicas: 3
Enter the container port: 3000
Enter the service port: 80
Enter the service type (ClusterIP, NodePort, LoadBalancer): NodePort


This will generate two YAML files:

deployment.yaml
service.yaml

