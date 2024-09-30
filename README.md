FastAPI Authentication Service

This is a FastAPI application that implements basic authentication, now deployed using Kubernetes and PostgreSQL.
Features

    Basic Authentication using HTTP Basic Auth
    User management with CRUD operations
    Book reservation system
    Kubernetes-based deployment for scalability and management

Getting Started

These instructions will help you set up and run the application in a Kubernetes environment.
Prerequisites

    Kubernetes and a working cluster (e.g., Minikube)
    Helm for Kubernetes package management
    Docker (to build images)

Setup

    Clone the repository:

    bash

git clone <your-repo-url>
cd <your-repo-directory>

Deploy the FastAPI Application:

Use Helm to deploy the application. Make sure your Docker images are built and available in a registry accessible by your Kubernetes cluster:

bash

    helm install fastapi-auth-service ./helm-chart-directory

Usage

API Endpoints:

    POST /users/ - Create a new user.
    POST /books/ - Add a new book.
    GET /booking/ - Retrieve booking information.

Authentication:

    The application uses HTTP Basic Authentication.
    Use the credentials specified in the .env (auth-secrets) to authenticate API requests.

Configuration

Kubernetes Configuration:

    Deployment and Service YAML files are used to manage the FastAPI application and PostgreSQL database.
    Helm Charts package the necessary Kubernetes resources for deployment.

Environment Variables (Managed via Kubernetes Secrets):

    USERNAME - The username for HTTP Basic Authentication.
    PASSWORD - The password for HTTP Basic Authentication.
