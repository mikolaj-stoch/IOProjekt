from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        # pobranie wszystkich zmiennych z input
        data = {"tab": [request.form[f'productName{i}'] for i in range(1, 6)]}

        # wykonanie funkcji
        return render_template("output.html", context=data)
    else:
        return render_template("input.html")


# @app.route("/output", methods=["POST", "GET"])
# def output(out):
#     return render_template("output.html", content=out)
#
#
# @app.route("/<nm1>")
# def user(nm1, nm2):
#     return render_template("output.html", content1=nm1, content2=nm2)


if __name__ == "__main__":
    app.run(debug=True)
