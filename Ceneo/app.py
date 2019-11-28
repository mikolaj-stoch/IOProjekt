from flask import Flask, render_template, request
import temporary
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method == "POST":
        data = {'input': []}
        for i in range(5):
            if request.form[f'productName{i}']:
                data['input'].append({
                    'name': request.form[f'productName{i}'],
                    'quantity': request.form[f'quantity{i}'],
                    'minimum_price': request.form[f'minPrice{i}'],
                    'maximum_price': request.form[f'maxPrice{i}'],
                    'reputation': request.form[f'reputation{i}']
                })
        with open('input_data.txt', 'w') as file:
            json.dump(data, file)
        output_data = temporary.search()  # TEMPORARY FUNCTION ! ! !
        return render_template("output.html", context=output_data)
    else:
        return render_template("search.html")


if __name__ == "__main__":
    app.run(debug=True)
