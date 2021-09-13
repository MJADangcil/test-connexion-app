# test-connexion-app
 A private repo for learning connexion.

## Technology Stack
- [Python](https://www.python.org/) v3.9.6
- [pip](https://pip.pypa.io/en/stable/) v21.1.3
- [connexion[swagger-ui]](https://connexion.readthedocs.io/en/latest/quickstart.html) v2.9.0
  - [Flask](https://flask.palletsprojects.com/en/2.0.x/) v1.1.4
  - [Swagger | OpenAPI](https://swagger.io/solutions/getting-started-with-oas/) v2.0

## Instructions
If you don't have a Python virtual environment, [create a one](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments). Otherwise, *skip* to next step.

`python3 -m venv {{YOUR_VIRTUAL_ENVIRONMENT}}`

<br>Activate your Python virtual environment. 
- macOS and Linux: `source {{YOUR_VIRTUAL_ENVIRONMENT}}/bin/activate`
- Windows: `{{YOUR_VIRTUAL_ENVIRONMENT}}\Scripts\activate.bat`

NOTE: If you ever need to exit your virtual environment run `deactivate` from the virtual environment terminal.

<br>Install the package bundle `connexion[swagger-ui]`. This bundle contains `Flask` and `Swagger | Open API`

- macOS: `python3 -m pip install "connexion[swagger-ui]"`
- Windows: `python3 -m pip install connexion[swagger-ui]`

<br>Set the Flask application to be the module `app.py`.
- Bash: `export FLASK_APP=app.py`
- CMD: `set FLASK_APP=app.py`
- Powershell: `$env:FLASK_APP = "app.py"`

<br>Optionally, set the Flask application's environment to be development if you need additional development features.
- Bash: `export FLASK_ENV=development`
- CMD: `set FLASK_ENV=development`
- Powershell: `$env:FLASK_ENV = "development"`

<br>Run the Flask application and open corresponding address.

`flask run`


<br>Opening the corresponding address to your application *should* result in a page like this. 

![Flask application](/readme_images/flask_app.png 'Flask application default address')

<br>To view the API specification via Swagger | Open API user interface, append a `/ui/` to the end of the address. For example...

`http://127.0.0.1:5000/ui/`

![Swagger | OpenAPI UI](/readme_images/swagger_openapi.png 'Swagger | OpenAPI application UI')

## Contributors
[Michael Josh A. Dangcil](https://github.com/MichaelJoshDangcil)