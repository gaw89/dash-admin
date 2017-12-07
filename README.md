# Dash-Admin

### Intro
#### Dash-Admin is an extension for [Dash](https://github.com/plotly/dash) to help start new Dash projects.

Dash-Admin is modelled after the ```django-admin``` command in the popular Python web framework [Django](https://github.com/django/django).  The goal of dash-admin is to provide a simple, easy-to-use CLI tool for staring projects in Dash.  

### Documentation

Getting a working Dash application is as simple as:

```dash-admin startproject myproject```

This will give you a working Dash application, complete with user authentication, user management (both online and through the CLI), and a main page with an interactive Plotly chart.  To start the application ```cd``` to the 'myproject' folder which was just created and enter:

```python run.py```

then visit [localhost:8050/myproject/app1](http://localhost:8050/myproject/app1).

You can log in with username ```admin``` and password ```admin```.

### Installation

Dash-Admin can be installed via ```pip install dash-admin --process-dependency-links``` or by cloning this repo and running ```python setup.py install```.
