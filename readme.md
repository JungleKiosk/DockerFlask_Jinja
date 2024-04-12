# Docker Python Flask PostgreSQL
This project is an example of how to use Docker to create and distribute a Python web application based on Flask.

# 1st step - Setting Project
## Project Files
commit: initial commit
```
d776e8a2ca1ab3ba5c81a26c6c352720491f5020
```
First, the directory must be created:

back_end|
        |-Dockerfile
        |-main.py
        |-requirements.txt
docker-compose.yml
readme.md

> [!TIP]
> you can call the main folders your own but usually use 'back_end' , 'front_end'....

1. docker-compose.yml
The docker-compose.yml file is used to define the services that will constitute the Docker environment for our project. In this file, the configurations of the Docker services are specified, such as the images to be used, environment variables, exposed ports and other network configurations.

2. Dockerfile
The Dockerfile contains instructions for creating the Docker image that will host the Flask application. Within this file, dependencies, the execution environment and the operations required to configure and start the application are defined.

3. main.py
The main.py file contains the main source code of the Flask application. Here we define the application's routes, business logic and all the functions needed to handle incoming HTTP requests and generate the corresponding responses.

4. requirements.txt
The requirements.txt file lists all the Python dependencies needed to run the Flask application. This file is used by pip to automatically install all dependencies when the Docker image is built.

## docker-file.yml
The file docker-compose.yml is used to define and manage the Docker services within the project. In this case, the file contains two services:

> **Web service:** This service defines a ****container** for the Flask web application. It uses the Dockerfile located in the back_end directory to create the **Docker image**.<br>
It mounts the back_end directory as a **volume** inside the **container** to allow access to the application's source code. It exposes port 5000 of the **container** to allow access to the web application.<br>
It also defines some environment variables that the Flask application will use for configuration, such as DEBUG, PORT and the credentials for the PostgreSQL database.

> **db service:** This service uses the default Docker image of PostgreSQL. It exposes port 5432 to allow access to the database. It sets environment variables to configure the database, such as the **user**, **password** and **database name**.

> [!NOTE]
> The web service depends on the db service, which means that Docker Compose will first start the db service before starting the web service.

## Dockerfile
The Dockerfile is used to create the Docker image for the Flask application. <br>
It uses the base image python:3.7 (depends on the installed Python version) as the starting point and sets the working directory (WORKDIR) to /app. <br>
It sets environment variables to configure the Flask application, then copies all files from the current directory (where the Dockerfile is located) to the working directory inside the container. <br>
Finally, it runs the pip install command to install the dependencies listed in the requirements.txt file and sets the default command (CMD) to start the application using python main.py.

## requirements.txt
The requirements.txt file lists all the Python dependencies required for the Flask application.

In summary, the docker-compose.yml file coordinates the orchestration of Docker services, while the Dockerfile is used to create the Docker image for the Flask application, which includes the source code (main.py) and dependencies (requirements.txt). Once the services are started with Docker Compose, the Flask application will be accessible at http://localhost:5000.



