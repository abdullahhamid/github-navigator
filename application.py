#!/usr/bin/env python

import json
import requests
import logging

from flask import Flask, request, render_template

app = Flask(__name__)

#Add index template here
@app.route("/")
def main():
    return "Welcome to GitHub Navigator!"


@app.route("/navigator")
def navigator():
    search_term = request.args.get("search_term")
    if search_term is None:
        return "please use search_term=arrow"
    search_results = get_search_results(search_term)
    sorted_list = get_sorted_list(search_results)
    #app.logger.info(search_results)
    return render_template('template.html', created_at=sorted_list)

#also add for 404
#@app.errorhandler(500)
#def internal_server_error(error):
#    app.logger.error('Server Error: %s', (error))
#    return render_template('500.htm'), 500


#@app.errorhandler(Exception)
#def unhandled_exception(e):
#    app.logger.error('Unhandled Exception: %s', (e))
#    return render_template('500.htm'), 500


def get_sorted_list(results):
    sorted_list = sorted(results["items"], key=lambda k: k.get("created_at", 0), reverse=True)
    for entry in sorted_list:
        app.logger.info(entry["created_at"])
    return "hello"


def get_search_results(search_term):
    search_results = requests.get("https://api.github.com/search/repositories?q=" + search_term)
    json_data = json.loads(search_results.content)
    #str = json_data["items"][0]["created_at"]
    return json_data


if __name__ == "__main__":
    app.run(debug=True)  # Port changed to 9876 instead of default 5000
