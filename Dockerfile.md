# Dockerfile Generator

This script dynamically generates `Dockerfile` based on the programming language, version, and additional parameters. It supports Node.js, Python, and Java (Maven).

## Features

- Generate `Dockerfile` for:
  - **Node.js**
  - **Python**
  - **Java (Maven build)**

## Prerequisites

Before running the script, ensure you have the following installed:

- **Python 3.x**
- **Jinja2 library** for templating

Install Jinja2 with pip:

```bash
pip install jinja2
```

## Usage
## Command Format

```bash
python script_name.py <language> <version> <expose_port> [--start_script <script_name>] [--jar_file <jar_file>]
```

## Example Commands

Node.js
To generate a Dockerfile for a Node.js application:

```bash
python script_name.py node 16 3000 --start_script app.js
```

This generates a Dockerfile for a Node.js project using Node.js version 16 and exposing port 3000. The start script is app.js.

**Python**

To generate a Dockerfile for a Python application:

```bash
python script_name.py python 3.9 5000 --start_script app.py
```

This generates a Dockerfile for a Python project using Python version 3.9 and exposing port 5000. The start script is app.py.

**Java (Maven)** 
To generate a Dockerfile for a Java project with Maven:

```bash
python script_name.py java 8 8080 --maven_version 3.6.3 --java_version 8
```

This generates a Dockerfile for a Maven-built Java application, using OpenJDK 8, exposing port 8081, and specifying myapp.jar as the JAR file.



### Output Files

**Dockerfile:** A file that describes how to build the Docker image for your project.
For Node.js and Python: Copies dependencies, installs them, and starts the application.
For Java: Builds the application using Maven, then copies the JAR file and runs it.
