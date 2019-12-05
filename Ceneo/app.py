from flask import Flask, render_template, request
import json
import os
import sqlite3
import itertools
import sys
import optimalizer
import time
import tmp_dir_manager
import tmp      # TEMPORARY


app = Flask(__name__)


@app.route("/")     # Home page (127.0.0.1:5000)
def home():
    return render_template("home.html")


@app.route("/search", methods=["POST", "GET"])      # Search page (127.0.0.1:5000/search)
def search():
    if request.method == "POST":
        data = {'products': []}     # Dictionary for input data
        for i in range(5):
            if request.form[f'productName{i}']:
                data['products'].append({
                    'name': request.form[f'productName{i}'],    # Get the value of the form field named "productName{i}"
                    'quantity': request.form[f'quantity{i}'],   # "productName{i}" means "productName1" for i=1 etc
                    'minimum_price': request.form[f'minPrice{i}'],
                    'maximum_price': request.form[f'maxPrice{i}'],
                    'reputation': request.form[f'reputation{i}']
                })
        tmp_dir_manager.create('./tmp')             # Create tmp directory
        with open('./tmp/input_data.txt', 'w') as file:
            json.dump(data, file)                   # Save input data to json file
        tmp.search()    # TEMPORARY

        os.system(".\\Crawler\\ONE_BAT_TO_RULE_THEM_ALL.bat")
        time.sleep( 12 )
        optimalizer.main()


        with open('.\\tmp\\output_data.txt') as json_file:
            output_data = json.load(json_file)      # Load output data from json file
        tmp_dir_manager.delete('./tmp')             # Delete tmp directory
        return render_template("results.html", context=output_data)
    else:
        return render_template("search.html")


@app.route("/authors")      # Authors page (127.0.0.1:5000/authors)
def authors():
    return render_template("authors.html")


if __name__ == "__main__":
    app.run(debug=True)
