from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        input_data = []
        for i in range(1, 6):
            temp_data = []
            temp_data.append(request.form[f'productName{i}'])
            temp_data.append(request.form[f'quantity{i}'])
            temp_data.append(request.form[f'minPrice{i}'])
            temp_data.append(request.form[f'maxPrice{i}'])
            temp_data.append(request.form[f'reputation{i}'])
            input_data.append(temp_data)
        # miejsce na wywolanie funkcji z argumentem input_data
        return render_template("output.html", context=input_data)
    else:
        return render_template("input.html")


if __name__ == "__main__":
    app.run(debug=True)
