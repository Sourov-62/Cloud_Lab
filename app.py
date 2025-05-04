from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = []
    if request.method == "POST":
        try:
            n = int(request.form["number"])
            result = [2 * i for i in range(n)]
        except ValueError:
            result = ["Invalid input."]
    return render_template_string("""
        <h2>Generate Even Numbers</h2>
        <form method="post">
            Enter a number: <input name="number">
            <button type="submit">Submit</button>
        </form>
        {% if result %}
            <p>Result: {{ result }}</p>
        {% endif %}
    """, result=result)

if __name__ == "__main__":
    app.run(debug=True)
