# 🌊 OceanShield — DevOps Monitoring Platform

A containerized FastAPI application demonstrating a complete DevOps workflow using **Docker, Kubernetes, Terraform, GitHub Actions, Prometheus, and Grafana**.

---

## 📌 Overview

OceanShield is a DevOps-focused monitoring platform built to demonstrate how a web application can be developed, containerized, deployed, monitored, and continuously tested using modern DevOps tools.

The project implements the following workflow:

**FastAPI → GitHub → GitHub Actions → Docker → Kubernetes → Prometheus → Grafana**

Terraform is used to provision Kubernetes infrastructure.

---

## 🎯 Objectives

* Develop a lightweight REST API using FastAPI
* Containerize the application using Docker
* Deploy the application using Kubernetes
* Run multiple application replicas for availability
* Use Terraform for infrastructure provisioning
* Implement Continuous Integration using GitHub Actions
* Expose application metrics using Prometheus instrumentation
* Collect and monitor metrics using Prometheus
* Visualize monitoring data using Grafana

---

## 🛠️ Technology Stack

| Technology           | Purpose                      |
| -------------------- | ---------------------------- |
| **Python / FastAPI** | Backend REST API             |
| **Docker**           | Application containerization |
| **Kubernetes**       | Container orchestration      |
| **Terraform**        | Infrastructure provisioning  |
| **GitHub Actions**   | Continuous Integration       |
| **Prometheus**       | Metrics collection           |
| **Grafana**          | Metrics visualization        |
| **Git / GitHub**     | Version control              |

---

## 🏗️ Architecture

```text
                    ┌─────────────────┐
                    │     GitHub      │
                    │   Source Code   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ GitHub Actions  │
                    │       CI        │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │      Docker     │
                    │ Container Image │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Kubernetes    │
                    │   Deployment    │
                    │   2 Replicas    │
                    └────────┬────────┘
                             │
                    ┌────────┴────────┐
                    ▼                 ▼
              ┌───────────┐     ┌───────────┐
              │   Pod 1   │     │   Pod 2   │
              │ FastAPI   │     │ FastAPI   │
              └─────┬─────┘     └─────┬─────┘
                    │                 │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    Prometheus   │
                    │ Metrics Scraping│
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     Grafana     │
                    │   Dashboard     │
                    └─────────────────┘

             Terraform
                  │
                  ▼
          Kubernetes Infrastructure
```

---

## 🚀 Application Endpoints

The FastAPI application provides the following endpoints:

### `/`

Returns the application's running status.

### `/health`

Health-check endpoint used to verify that the application is healthy.

### `/telemetry`

Returns basic service telemetry information.

### `/metrics`

Exposes Prometheus-compatible application metrics.

---

## 🐳 Docker

The application is packaged into a Docker image using the project's `Dockerfile`.

### Build the image

```bash
docker build -t oceanshield-api:latest .
```

### Run the container

```bash
docker run -d -p 8000:8000 --name oceanshield-api oceanshield-api:latest
```

The application can then be accessed at:

```text
http://localhost:8000
```

---

## ☸️ Kubernetes

The application is deployed to Kubernetes using:

* `k8s/deployment.yaml`
* `k8s/service.yaml`

The Deployment runs **2 replicas** of the FastAPI application.

### Apply the Deployment

```bash
kubectl apply -f k8s/deployment.yaml
```

### Apply the Service

```bash
kubectl apply -f k8s/service.yaml
```

### Check Pods

```bash
kubectl get pods
```

### Check Service

```bash
kubectl get service
```

### Access the application

For local testing, the Kubernetes Service can be accessed through port forwarding:

```bash
kubectl port-forward service/oceanshield-service 8080:8000
```

Then open:

```text
http://localhost:8080
```

---

## 🏗️ Terraform

Terraform is used to provision the Kubernetes namespace for the project.

Terraform configuration is located in:

```text
terraform/main.tf
```

### Initialize Terraform

```bash
cd terraform
terraform init
```

### Preview changes

```bash
terraform plan
```

### Apply infrastructure

```bash
terraform apply
```

The project creates the:

```text
oceanshield
```

Kubernetes namespace.

---

## 🔄 Continuous Integration

GitHub Actions is used to automatically validate changes pushed to the `main` branch.

The workflow:

1. Checks out the repository
2. Sets up Python 3.12
3. Installs project dependencies
4. Builds the Docker image
5. Runs the Docker container
6. Performs an application health check
7. Stops the test container

Workflow file:

```text
.github/workflows/ci.yml
```

The health check verifies:

```text
GET /health
```

---

## 📊 Monitoring

The FastAPI application is instrumented using:

```text
prometheus-fastapi-instrumentator
```

Prometheus collects metrics exposed by the `/metrics` endpoint.

Prometheus configuration:

```text
monitoring/prometheus/prometheus.yml
```

The monitoring setup includes application metrics such as:

* HTTP request metrics
* Request-related metrics
* Python garbage-collection metrics

---

## 📈 Grafana Dashboard

Grafana is connected to Prometheus as its data source.

The project dashboard is called:

**OceanShield Monitoring**

Current dashboard panels include:

* HTTP Requests
* HTTP Request Count
* Python GC Activity

This provides a visual representation of application activity and runtime metrics.

---

## 🧪 Testing

The project was tested at multiple stages:

### API Testing

FastAPI endpoints were tested locally, including:

```text
/
 /health
/telemetry
/metrics
```

### Docker Testing

The Docker image was built and executed locally.

The `/metrics` endpoint was verified from the running container.

### Kubernetes Testing

The Kubernetes deployment was verified using:

```bash
kubectl get pods
```

Two application replicas were deployed successfully.

The Kubernetes Service was tested using port forwarding.

### Prometheus Testing

Prometheus successfully scraped metrics from the application.

### Grafana Testing

Grafana successfully queried the Prometheus API and displayed application metrics.

### CI Testing

GitHub Actions successfully:

* Installed dependencies
* Built the Docker image
* Started the container
* Passed the `/health` check

---

## 📁 Project Structure

```text
OceanShield-DevOps/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── monitoring/
│   └── prometheus/
│       └── prometheus.yml
│
├── terraform/
│   ├── main.tf
│   └── .terraform.lock.hcl
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

---


## 🔮 Future Scope

Possible future improvements include:

* Kubernetes-native Prometheus service discovery
* Automated deployment after successful CI
* Persistent Grafana dashboards
* Alerting for application failures
* Container resource monitoring
* Production cloud deployment
* HTTPS and secure API access

---


