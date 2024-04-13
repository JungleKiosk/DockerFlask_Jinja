# 🌊🐋🌊 Docker 🌳Flask🐍 PostgreSQL 🌴🐘🌴

# ⛩️render_template Jinja⛩️ from scratch 

# 1st step - Setting Project
## Project Files
First, the directory must be created:
```
back_end|
        |-Dockerfile
        |-main.py
        |-requirements.txt
docker-compose.yml
readme.md
```

> [!TIP]
> you can call the main folders your own but usually use 'back_end' , 'front_end'....

1. docker-compose.yml <br>
The docker-compose.yml file is used to define the services that will constitute the Docker environment for our project. In this file, the configurations of the Docker services are specified, such as the images to be used, environment variables, exposed ports and other network configurations.

2. Dockerfile<br>
The Dockerfile contains instructions for creating the Docker image that will host the [Flask](https://flask.palletsprojects.com/en/3.0.x/).
 application. Within this file, dependencies, the execution environment and the operations required to configure and start the application are defined.

3. main.py<br>
The main.py file contains the main source code of the Flask application. Here we define the application's routes, business logic and all the functions needed to handle incoming HTTP requests and generate the corresponding responses.

4. requirements.txt<br>
The requirements.txt file lists all the Python dependencies needed to run the Flask application. This file is used by pip to automatically install all dependencies when the Docker image is built.

## docker-file.yml
The file docker-compose.yml is used to define and manage the Docker services within the project. In this case, the file contains two services:

- **Web service:** This service defines a **container** for the Flask web application. It uses the Dockerfile located in the back_end directory to create the **Docker image**.<br>
It mounts the back_end directory as a **volume** inside the **container** to allow access to the application's source code. It exposes port 5000 of the **container** to allow access to the web application.<br>
It also defines some environment variables that the Flask application will use for configuration, such as DEBUG, PORT and the credentials for the PostgreSQL database.

- **db service:** This service uses the default Docker image of PostgreSQL. It exposes port 5432 to allow access to the database. It sets environment variables to configure the database, such as the **user**, **password** and **database name**.

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

commits: <br>
initial commit
```
d776e8a2ca1ab3ba5c81a26c6c352720491f5020
```
setting Docker Python Flask
```
ac04ed4f0cd8956f12deb9a01bc13a86c243fb4f
```

# 2nd step - Flask routes & Template imports
After setting up the basic Flask application, the next step was to create a route and render it using the [render_template](https://flask.palletsprojects.com/en/2.3.x/tutorial/templates/) function.

The Flask application was set up with a **simple route defined for the root URL ('/')**. When accessing this route, the application returns a plain text response of "Hello!".

main.py
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return ('Hello!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```
Browser
![hello_img](/back_end/assets/img/readme/hello_1st_route.png)

commit: setting Docker Python Flask
```
ac04ed4f0cd8956f12deb9a01bc13a86c243fb4f
```

Flask's `render_template` function allows HTML templates to be rendered within the Flask application.

main.py
```
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home/home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

base.html
```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>{% block title %} {% endblock %}</title>
    <link rel="stylesheet" type="text/css" href="/assets/css/style.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<style>
    body{
        background-color: black;
        color: rgb(255, 255, 255);
    }
</style>

<body>
    <div class="content">
        {% block content %}
        {% endblock %}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
</body>

</html>
```

home.html

```
{% extends "base.html" %}

{% block title %}
Home
{% endblock %}


{% block content %}

<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-6 text-center">
            <h1>Hello Jinja! ⛩️</h1>
        </div>
    </div>
</div>


{% endblock %}
```
Browser
![hello_img](/back_end/assets/img/readme/hello_jinja.png)

commit: template folder: {% extends "base.html" %}
```
b63566182f7b77f42a982e4614267fdd0f7fe44e
```
Now, instead of `return`ing a simple textual response, the main route ('/') has been modified to render an HTML template called home.html located in the home directory. <br>
When a user accesses the main route, the browser will display the contents of the HTML `return`ed by the template. This allows objects in the DOM (Document Object Model) to be displayed within the browser.

**But... What is that base.html file? 🌳🦥🌳**

### **Using Jinja Blocks {% block %} ⛩️**
In the base.html template, the concept of Jinja {% block %} blocks is used. These blocks allow you to define portions of content within a template that can be overwritten or extended by other templates that extend the base template.

**Why is it convenient to use?**
1. **Code Organisation**: Using Jinja blocks, it is possible to organise HTML code into reusable forms. The basic template base.html defines the basic structure of the web page, while other templates, such as home.html, extend the basic template and overwrite or extend the defined blocks.

2. **Code Reuse:** Jinja blocks avoid duplication of HTML code. For example, the header and footer are defined in the base template and can be reused in all other templates without having to re-implement them.

3. **Customising Templates:** Jinja blocks make it easy to customise templates without having to modify the base template.<br>
For example, in the template home.html, the `{% block title %}` has been overwritten to define a specific title for the Home page, while the `{% block content %}` has been extended to add the specific content of the Home page.

> [!NOTE]
> The use of Jinja blocks makes it possible to keep the code clean, organised and easily modifiable, thus improving the maintainability and flexibility of the project.

basic template Jinja ⛩️🥷
```
{% extends "base.html" %}

{% block title %}
Page Title
{% endblock %}


{% block content %}

HTML code

{% endblock %}
```

> [!IMPORTANT]
> Flask is closely related to [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/), since Jinja2 is the default template engine used by Flask to render dynamic HTML templates. This is how they are related:

>[!NOTE]
> **render_template:** This is a function provided by Flask that facilitates the rendering of HTML templates. When you call render_template in your Flask code and pass it the name of the template to render, Flask uses Jinja2 to interpret that template and generate an HTML response that is sent back to the client. <br> **Jinja2:** This is a template engine for Python that provides a syntax for creating dynamic HTML templates. Jinja2 allows variables, expressions, loops and conditions to be inserted into HTML templates, making it possible to generate customised, dynamic web pages.

Basically, when you use render_template in Flask, you are actually using Jinja2 to generate the HTML content of the template. Jinja2 interprets the template, replacing variables and expressions with the values provided, and Flask returns the result to the client as a complete HTML page.
