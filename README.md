# vulnerable-flask-app
A simple Python web application built based on Flask. This app might not be able to run, it is used for security analysis lab experiment in CSC471 Software Security.

## Vulnerable Dependencies
In the file 'requirements.txt', you can find the list of dependencies of this software. When setting up the development environment, you can use the command `pip -r requirements.txt` to install all the dependencies.

Here are some python packages (dependencies) with publicly-known security vulnerabilities:
- **Flask 2.3.1**: This version of Flask has the direct vulnerability "Information Exposure", details can be found here: [Snyk Vulnerability Database: Flask](https://security.snyk.io/package/pip/flask) and [flask@2.3.1 vulnerabilities](https://security.snyk.io/package/pip/flask/2.3.1)
- **Jinja2 2.11.3**: Jinja2 is a template engine written in pure Python. This version of Jinja2 has many vulnerabilities including XSS, Template Injection, and Improper Neutralization. Details can be found here: [jinja2@2.11.3 vulnerabilities](https://security.snyk.io/package/pip/jinja2/2.11.3)
- **pyyaml 3.13**: pyyaml is a YAML parser and emitter for Python. This version of pyyaml is vulnerable to Arbitrary Code Execution due to using the insecure `yaml.load()` function. Details can be found here: [pyyaml@3.13 vulnerabilities](https://security.snyk.io/package/pip/pyyaml/3.13)