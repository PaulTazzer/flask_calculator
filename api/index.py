from flask import Flask, render_template, request

app = Flask(__name__, template_folder="../templates")

@app.route("/", methods=["GET", "POST"])
def calculator():
    num1 = num2 = operator = result = None  # Initialize variables
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operator = request.form["operator"]

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2 if num2 != 0 else "Error: Div by 0"

        except Exception as e:
            result = f"Invalid input: {e}"

    return render_template("index.html", num1=num1, num2=num2, operator=operator, result=result)

if __name__ == "__main__":
    app.run(debug=True)
