#!/usr/bin/env python

import json
import requests

from flask import Flask, request, render_template

app = Flask(__name__)


# get the latest commits of repository - inputs: repository owner login, repository name
def get_latest_commit(repo_owner, repo_name):
    search_results = requests.get("https://api.github.com/repos/" + repo_owner + "/" + repo_name + "/commits")
    json_data = json.loads(search_results.content)
    return json_data


# get top five sorted search results
def get_sorted_search_results(search_term):
    search_results = requests.get("https://api.github.com/search/repositories?q=" + search_term)
    json_data = json.loads(search_results.content)
    # sort the search results
    sorted_list = sorted(json_data["items"], key=lambda k: k.get("created_at", 0), reverse=True)
    top_five = []
    # get latest commits for the top 5 repositories in the results
    for i in range(len(sorted_list)):
        if i == 5:
            break
        top_five.append(sorted_list[i])
        top_five[i]["commit_details"] = get_latest_commit(sorted_list[i]["owner"]["login"], sorted_list[i]["name"])
    return top_five


# Home page of the application
@app.route("/")
def main():
    return render_template('index.html')


# navigator route
@app.route("/navigator")
def navigator():
    search_term = request.args.get("search_term")
    if search_term is None:
        return render_template('search.html')  # send back the correct usage page
    sorted_search_results = get_sorted_search_results(search_term)
    return render_template('template.html', sorted_list=sorted_search_results, search_term=search_term)


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('404 Not Found')
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', error)
    return render_template('500.html'), 500


@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error('Unhandled Exception: %s', e)
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run()  # Default: http://127.0.0.1:5000/
