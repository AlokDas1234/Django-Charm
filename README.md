# Django Charm

Welcome to **Django Charm**! This is a handy package that can save your time so you can focus on building what truly matters in your Django project.

## Features
- Users no longer need to install Django. 
- No need to manually create and configure a Django project and app separately.
- Automatically handles the `urls.py` and `settings.py` setup.
- Instantly creates `index.html` with a starter template — ready to go.

---

## django-charm

This package allows you to create a Django project and app by executing a single command (including generating `views.py`, `urls.py`, and a basic `index.html` template).

## Table of Contents
- [Installation](#installation)
- [Features](#features)
- [Examples](#examples)
- [License](#license)


## Installation

```bash
pip install django-charm
```





# Examples:

  #####  Create the Whole Project:
To create a new Django project and app:<br>
<br>
A.ctivate your virtual environment.<br>

3.Use the --createproject flag to specify the project name.<br>

4.Use -a to specify the app name.



```bash

django-charm --createproject myproject -a myapp

```
  #####  To create only a new app inside an existing project:

1.Make sure your Django project already exists.<br>
2.Use the --createapp flag to specify the new app name.<br>
3.Use -p to specify the parent project name (where manage.py is located).

```bash

django-charm  --createapp myapp -p parentpackage

```
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

