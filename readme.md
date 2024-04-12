# Docker Python Flask
This project is an example of how to use Docker to create and distribute a Python web application based on Flask.

# 1st step - Setting Project
## Project Files
```
commit: initial commit
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



