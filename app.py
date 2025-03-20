from flask import Flask, request
from jinja2 import Environment, PackageLoader, select_autoescape
import yaml

app = Flask(__name__)

env = Environment(
    loader=PackageLoader("yourapp"),
    autoescape=select_autoescape()
)


@app.route('/load_yaml', methods=['POST'])
def load_yaml():
    yaml_data = request.data
    try:
        data = yaml.load(yaml_data, Loader=yaml.FullLoader)  # This is vulnerable to certain attacks
        return {"message": "YAML loaded", "data": data}, 200
    except Exception as e:
        return {"message": f"Error loading YAML: {str(e)}"}, 400

if __name__ == '__main__':
    app.run(debug=True)
