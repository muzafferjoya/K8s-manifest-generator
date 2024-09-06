import yaml
import random

def generate_deployment(name, image, replicas, container_port):
    deployment = {
        'apiVersion': 'apps/v1',
        'kind': 'Deployment',
        'metadata': {'name': name},
        'spec': {
            'replicas': replicas,
            'selector': {'matchLabels': {'app': name}},
            'template': {
                'metadata': {'labels': {'app': name}},
                'spec': {
                    'containers': [{
                        'name': name,
                        'image': image,
                        'ports': [{'containerPort': container_port}]
                    }]
                }
            }
        }
    }
    return yaml.dump(deployment)

def generate_service(name, port, target_port, service_type):
    service = {
        'apiVersion': 'v1',
        'kind': 'Service',
        'metadata': {'name': name},
        'spec': {
            'selector': {'app': name},
            'ports': [{
                'protocol': 'TCP',  # Explicit protocol
                'port': port,
                'targetPort': target_port
            }],
            'type': service_type
        }
    }

    if service_type == "NodePort":
        # NodePort should be within the range 30000-32767
        node_port = random.randint(30000, 32767)
        service['spec']['ports'][0]['nodePort'] = node_port  # Add nodePort to the service

    return yaml.dump(service)

# User Inputs
app_name = input("Enter the application name: ")
image = input("Enter the Docker image name: ")
replicas = int(input("Enter the number of replicas: "))
container_port = int(input("Enter the container port: "))
service_port = int(input("Enter the service port: "))
service_type = input("Enter the service type (ClusterIP, NodePort, LoadBalancer): ")

# Generate YAMLs
deployment_yaml = generate_deployment(app_name, image, replicas, container_port)
service_yaml = generate_service(app_name, service_port, container_port, service_type)

# Save the YAMLs to files
with open("deployment.yaml", "w") as deployment_file:
    deployment_file.write(deployment_yaml)

with open("service.yaml", "w") as service_file:
    service_file.write(service_yaml)

print("Deployment YAML saved to deployment.yaml")
print("Service YAML saved to service.yaml")
