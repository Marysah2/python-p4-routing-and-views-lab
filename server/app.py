from flask import Flask

app = Flask(__name__)

# "/" route
@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


# "/print/<parameter>" route
@app.route("/print/<parameter>")
def print_parameter(parameter):
    print(parameter)          # print to console
    return parameter          # display in browser


# "/count/<parameter>" route
@app.route("/count/<int:parameter>")
def count(parameter):
    output = ""
    for i in range(parameter):
        output += f"{i}\n"
    return output


# "/math/<parameters>" route
@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        return str(num1 + num2)
    elif operation == "-":
        return str(num1 - num2)
    elif operation == "*":
        return str(num1 * num2)
    elif operation == "div":
        return str(num1 / num2)
    elif operation == "%":
        return str(num1 % num2)
    else:
        return "Invalid operation"


if __name__ == "__main__":
    app.run(debug=True)
