import argparse
from jinja2 import Template

# Jinja2 template for Kubernetes Deployment
k8s_deployment_template = '''\
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ app_name }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ app_name }}
  template:
    metadata:
      labels:
        app: {{ app_name }}
    spec:
      containers:
      - name: {{ app_name }}
        image: {{ image_name }}:{{ image_tag }}
        ports:
        - containerPort: {{ container_port }}
        env:
        - name: PORT
          value: "{{ container_port }}"
'''

# Jinja2 template for Kubernetes Service (NodePort)
k8s_service_template = '''\
apiVersion: v1
kind: Service
metadata:
  name: {{ app_name }}-service
spec:
  type: NodePort
  ports:
  - port: {{ service_port }}
    targetPort: {{ container_port }}
    nodePort: {{ node_port }}
  selector:
    app: {{ app_name }}
'''

def generate_k8s_deployment(app_name, image_name, image_tag, container_port):
    template = Template(k8s_deployment_template)
    k8s_deployment_content = template.render(
        app_name=app_name,
        image_name=image_name,
        image_tag=image_tag,
        container_port=container_port
    )
    return k8s_deployment_content

def generate_k8s_service(app_name, service_port, container_port, node_port):
    template = Template(k8s_service_template)
    k8s_service_content = template.render(
        app_name=app_name,
        service_port=service_port,
        container_port=container_port,
        node_port=node_port
    )
    return k8s_service_content

def main():
    parser = argparse.ArgumentParser(description="Generate Kubernetes manifest files for a project.")
    parser.add_argument("app_name", help="Name of the application")
    parser.add_argument("image_name", help="Docker image name")
    parser.add_argument("image_tag", help="Docker image tag")
    parser.add_argument("service_port", help="Port on which the service will be exposed", type=int)
    parser.add_argument("container_port", help="Container port to be exposed", type=int)
    parser.add_argument("node_port", help="Node port for accessing the service externally", type=int)

    args = parser.parse_args()

    k8s_deployment_content = generate_k8s_deployment(
        args.app_name,
        args.image_name,
        args.image_tag,
        args.container_port
    )
    k8s_service_content = generate_k8s_service(
        args.app_name,
        args.service_port,
        args.container_port,
        args.node_port
    )

    # Write Deployment manifest
    with open('deployment.yaml', 'w') as deployment_file:
        deployment_file.write(k8s_deployment_content)
    
    # Write Service manifest
    with open('service.yaml', 'w') as service_file:
        service_file.write(k8s_service_content)
    
    print("Kubernetes manifests generated successfully.")

if __name__ == '__main__':
    main()
