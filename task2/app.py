from flask import Flask, request, render_template

app = Flask(__name__)

def multiply_matrices(a, b):
    if len(a[0]) != len(b):
        return "Matrix multiplication not possible"

    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]

    return result

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        try:
            matrix_a = eval(request.form["matrix_a"])
            matrix_b = eval(request.form["matrix_b"])
            result = multiply_matrices(matrix_a, matrix_b)
        except Exception as e:
            error = f"Error: {e}"
    return render_template("index.html", result=result, error=error)
