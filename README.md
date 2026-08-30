# 🚀 DevOps Capstone Project

## End-to-End CI/CD Pipeline for a Python Student Management API

A cloud-native Student Management REST API built and deployed using an
end-to-end DevOps workflow.

This project demonstrates the complete journey from source code
management and automated testing to Docker containerization, image
publishing, server automation, and Kubernetes deployment on AWS.

---

## 📌 Project Overview

The application goes through the following pipeline:

```text
Developer
    |
    v
  GitHub
    |
    v
  Jenkins
    |
    +----> Install Dependencies
    |
    +----> Run Pytest
    |
    v
 Docker Build
    |
    v
 Docker Hub
    |
    v
 AWS EC2
    |
    v
   K3s
 Kubernetes
    |
    v
 Deployment
    |
    v
    Pod
    |
    v
  Service
    |
    v
 NodePort :30050
    |
    v
 Student API
```

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Flask | REST API framework |
| Pytest | Automated testing |
| Git | Version control |
| GitHub | Source code repository |
| Jenkins | CI/CD automation |
| Docker | Application containerization |
| Docker Hub | Container image registry |
| Ansible | Server configuration and automation |
| AWS EC2 | Cloud infrastructure |
| K3s | Lightweight Kubernetes distribution |
| Kubernetes | Container orchestration |
| kubectl | Kubernetes cluster management |
| Linux / Ubuntu | Server operating system |

---

# 🏗️ Architecture

```text
                         GitHub
                            |
                            v
                         Jenkins
                            |
                +-----------+-----------+
                |                       |
                v                       v
       Python Environment            Pytest
                |                       |
                +-----------+-----------+
                            |
                         SUCCESS
                            |
                            v
                       Docker Build
                            |
                            v
                        Docker Hub
                            |
                            v
                         AWS EC2
                            |
                            v
                      K3s Kubernetes
                            |
                      +-----+-----+
                      |           |
                      v           v
                 Deployment     Service
                      |           |
                      v           v
                     Pod       NodePort
                      |          :30050
                      +-----+-----+
                            |
                            v
                      Student API
```

---

# 🔄 CI/CD Pipeline

The Jenkins pipeline automates the application build and delivery
process.

### Pipeline Stages

### 1. Checkout

Jenkins retrieves the latest source code from GitHub.

### 2. Create Python Environment

A Python virtual environment is created for isolated dependency
management.

```bash
python3 -m venv venv
```

### 3. Install Dependencies

Dependencies are installed from:

```text
app/requirements.txt
```

### 4. Run Tests

Automated tests are executed using Pytest.

```bash
python -m pytest
```

If the tests fail, the Jenkins pipeline stops and does not proceed to
the Docker build.

### 5. Transfer Code to EC2

The application source code is securely transferred to the AWS EC2
server using SSH.

### 6. Docker Build

The application is packaged into a Docker image.

```bash
docker build -t student-api:1.1 .
```

### 7. Push Image to Docker Hub

The Docker image is tagged and pushed to Docker Hub.

```text
puneetbt11/student-api:1.1
```

---

# 🐳 Docker

Docker is used to package the Flask application and its dependencies
into a portable container.

### Build Image

```bash
docker build -t student-api:1.1 .
```

### Run Container

```bash
docker run -d -p 5000:5000 student-api:1.1
```

The application runs on:

```text
Container Port: 5000
```

---

# ☁️ AWS EC2

AWS EC2 provides the cloud infrastructure for the project.

EC2 is used as the compute environment for the DevOps workflow and
K3s Kubernetes deployment.

The project uses lightweight EC2 infrastructure to keep the capstone
suitable for a hands-on learning environment.

---

# ⚙️ Ansible

Ansible is used for server configuration and automation.

Ansible inventory defines the target EC2 server.

Example:

```ini
[webservers]
ec2-server ansible_host=<EC2-PUBLIC-IP> ansible_user=ubuntu
```

### Test Ansible Connectivity

```bash
ansible all -i inventory.ini -m ping
```

### Run an Ansible Playbook

```bash
ansible-playbook -i inventory.ini setup_ec2.yml
```

Ansible helps reduce manual server configuration and makes the setup
repeatable.

---

# ☸️ Kubernetes with K3s

K3s is used as the lightweight Kubernetes distribution for the project.

The K3s cluster is running on an AWS EC2 instance.

### Check Cluster

```bash
kubectl get nodes
```

Example:

```text
NAME              STATUS   ROLES
ip-xxx-xxx-xxx    Ready    control-plane
```

---

# 📦 Kubernetes Deployment

The Student API is deployed using a Kubernetes Deployment.

File:

```text
k8s/student-api-deployment.yml
```

The Deployment manages the application Pod.

Apply the Deployment:

```bash
kubectl apply -f student-api-deployment.yml
```

Check Pods:

```bash
kubectl get pods
```

---

# 🌐 Kubernetes Service

The application is exposed using a Kubernetes NodePort Service.

File:

```text
k8s/student-api-service.yml
```

Port configuration:

```text
Container Port : 5000
Service Port   : 5000
NodePort       : 30050
```

Apply the Service:

```bash
kubectl apply -f student-api-service.yml
```

Check the Service:

```bash
kubectl get service
```

---

# 🧪 API Endpoints

The Student API provides the following endpoints:

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Application information |
| GET | `/health` | Application health check |
| GET | `/students` | Returns student information |

---

# 🔍 Application Testing

The health endpoint can be tested using:

```bash
curl http://localhost:30050/health
```

Expected response:

```json
{
  "status": "UP"
}
```

The API can also be accessed externally through the EC2 public IP:

```bash
curl http://x.x.x.:30050/health
```

---

# 🔐 Security

Sensitive credentials are not stored directly in the Jenkinsfile.

Docker Hub credentials are managed using Jenkins Credentials.

SSH access to EC2 uses an SSH private key.


# 🔧 Troubleshooting

The project includes hands-on troubleshooting of application,
container, Kubernetes, and network connectivity issues.

Useful commands include:

### Kubernetes

```bash
kubectl get nodes
kubectl get pods
kubectl get services
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

### Docker

```bash
docker ps
docker images
docker logs <container>
```

### Linux / Networking

```bash
ip addr
ip route
ss -tulpn
curl <URL>
```

AWS Security Group configuration was also verified when external
NodePort connectivity was required.

---

# 🎯 Key Learning Outcomes

Through this project, I gained hands-on experience with:

- Linux administration
- Git and GitHub
- Jenkins CI/CD
- Automated testing with Pytest
- Docker containerization
- Docker Hub
- Ansible automation
- AWS EC2
- Kubernetes fundamentals
- K3s
- Kubernetes Deployments
- Kubernetes Services
- NodePort networking
- CI/CD troubleshooting
- Cloud-based application deployment

---

# 👨‍💻 Author

**Puneet Bhatnagar**

DevOps | AWS | Linux | Docker | Kubernetes | Jenkins | Ansible


