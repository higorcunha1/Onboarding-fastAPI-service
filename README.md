# FastAPI Authentication Service

This is a FastAPI application that implements basic authentication using Docker and PostgreSQL.

## Features

- Basic Authentication using HTTP Basic Auth
- User management with CRUD operations
- Book reservation system
- Dockerized for easy deployment

## Getting Started

These instructions will help you set up and run the application on your local machine.

### Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop) and [Docker Compose](https://docs.docker.com/compose/install/)
- [Python](https://www.python.org/) (Optional: only if you want to run the app outside of Docker)

### Setup

1. **Clone the repository:**

   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>

2. **Create a .env file:**

    Create a file named .env in the root directory of the project with the following content:
    ```
    USERNAME=your_username
    PASSWORD=your_password

3. **Build and run the application:**
    
    Use Docker Compose to build and run the application:
     ```bash
    docker-compose up --build

### Usage

API Endpoints:
    POST /users/ - Create a new user.
    POST /books/ - Add a new book.
    GET /booking/ - Retrieve booking information.

Authentication:
    The application uses HTTP Basic Authentication.
    Use the credentials specified in the .env file to authenticate API requests.

Configuration

Docker Configuration:
    docker-compose.yml - Defines the Docker services for the application and PostgreSQL.
    Dockerfile - Defines how to build the Docker image for the application.

Environment Variables:
    USERNAME - The username for HTTP Basic Authentication.
    PASSWORD - The password for HTTP Basic Authentication.
