#!/usr/bin/env python

import json
import requests
import logging

from flask import Flask, request, render_template

app = Flask(__name__)

#Add index template here
@app.route("/")
def main():
    return render_template('index.html')


@app.route("/navigator")
def navigator():
    search_term = request.args.get("search_term")
    if search_term is None:
        return "please use search_term=arrow"
    search_results = get_search_results(search_term)
    sorted_list = get_sorted_list(search_results)
    app.logger.info(sorted_list)
    return render_template('template.html', sorted_list=sorted_list, search_term=search_term)


@app.errorhandler(404)
def internal_server_error(error):
    app.logger.error('404 Not Found')
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', (error))
    return render_template('500.html'), 500


@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error('Unhandled Exception: %s', (e))
    return render_template('500.html'), 500


# get top five sorted search results
def get_sorted_list(results):
    sorted_list = sorted(results["items"], key=lambda k: k.get("created_at", 0), reverse=True)
    top_five = []
    for i in range(5):
        top_five.append(sorted_list[i])
    return top_five


def get_search_results(search_term):
    search_results = requests.get("https://api.github.com/search/repositories?q=" + search_term)
    json_data = json.loads(search_results.content)
    return json_data


if __name__ == "__main__":
    app.run(debug=True)  # Port changed to 9876 instead of default 5000
