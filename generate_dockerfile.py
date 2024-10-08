import argparse
from jinja2 import Template

# Jinja2 template for Dockerfile
dockerfile_template_node = '''\
# Base image
FROM node:{{ version }}

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all files
COPY . .

# Expose the specified port
EXPOSE {{ expose_port }}

# Command to run the application
CMD ["node", "{{ start_script }}"]
'''

dockerfile_template_python = '''\
# Base image
FROM python:{{ version }}

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt

# Copy all files
COPY . .

# Expose the specified port
EXPOSE {{ expose_port }}

# Command to run the application
CMD ["python", "{{ start_script }}"]
'''

dockerfile_template_java_maven = '''\
# Stage 1: Build with Maven
FROM maven:{{ maven_version }}-jdk-{{ java_version }}-slim AS build
LABEL Muzaffar Khan "muzafferjoya@gmail.com"
RUN mkdir -p /workspace
WORKDIR /workspace
COPY pom.xml /workspace
COPY src /workspace/src
RUN mvn -B -f pom.xml clean package -DskipTests

# Stage 2: Run with OpenJDK
FROM openjdk:{{ java_version }}-jdk-slim
COPY --from=build /workspace/target/*.jar /app/app.jar
EXPOSE {{ expose_port }}
ENTRYPOINT ["java","-jar","/app/app.jar"]
'''

def generate_dockerfile(language, version, expose_port, start_script='app.js', maven_version='3.6.3', java_version='8'):
    if language == 'node':
        template = Template(dockerfile_template_node)
        dockerfile_content = template.render(
            version=version,
            expose_port=expose_port,
            start_script=start_script
        )
    elif language == 'python':
        template = Template(dockerfile_template_python)
        dockerfile_content = template.render(
            version=version,
            expose_port=expose_port,
            start_script=start_script
        )
    elif language == 'java':
        template = Template(dockerfile_template_java_maven)
        dockerfile_content = template.render(
            maven_version=maven_version,
            java_version=java_version,
            expose_port=expose_port
        )
    else:
        raise ValueError("Unsupported language")
    
    return dockerfile_content

def main():
    parser = argparse.ArgumentParser(description="Generate Dockerfile for a project.")
    parser.add_argument("language", help="Programming language for the Dockerfile (node, python, java)")
    parser.add_argument("version", help="Version of the base image or Java version for Java projects")
    parser.add_argument("expose_port", help="Port to be exposed", type=int)
    parser.add_argument("--start_script", help="Script to start the application (for Node.js and Python)", default="app.js")
    parser.add_argument("--maven_version", help="Maven version (default: 3.6.3)", default="3.6.3")
    parser.add_argument("--java_version", help="Java version (default: 8)", default="8")

    args = parser.parse_args()

    dockerfile_content = generate_dockerfile(
        args.language,
        args.version,
        args.expose_port,
        args.start_script,
        args.maven_version,
        args.java_version
    )

    # Write Dockerfile
    with open('Dockerfile', 'w') as dockerfile:
        dockerfile.write(dockerfile_content)
    
    print("Dockerfile generated successfully.")

if __name__ == '__main__':
    main()
