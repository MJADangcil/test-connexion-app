import connexion

app = connexion.FlaskApp(__name__, specification_dir='openapi/')
app.add_api('my_api.yaml')
app.run(port=8080)