# -*- coding: utf-8 -*-
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import requests
from parse import *
from bs4 import BeautifulSoup
import json
import nltk
import sys, os
from tokenize import *

# setup app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('query_form.html')

@app.route("/train", methods=['POST'])
def train():
    input_data = request.form.get('input_data');
    entities = request.form.get('entities')
    outputVar = request.form.get('outputVar')
    return render_template('model_train.html', input_data=input_data, entities=entities, outputVar=outputVar)

# commented out to remove from front end. Will use this route to explain training with custom JSON from API
#@app.route("/train_from_api")
def train_api():
    query = request.args.get('query')
    city = request.args.get('city')
    numEntries = request.args.get('numEntries')
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr);
    user_agent = request.headers.get('User-Agent');

    indeed_api_params = {
        'publisher': 9978236252243350,
        'v': 2,
        'callback': 'hello',
        'q': query,
        'l': city,
        'st': 'jobsite',
        'co': 'CA',
        'limit': numEntries,
        'format': 'json',
        'userip': ip,
        'useragent': user_agent,
    }
    indeed_api_headers = {
        'User-Agent': user_agent 
    }
    indeed_api_response = requests.get('http://api.indeed.com/ads/apisearch', 
                                       params=indeed_api_params, 
                                       headers=indeed_api_headers).text
    indeed_api_response = parse('hello({})', indeed_api_response).fixed[0]
    indeed_api_response = json.loads(indeed_api_response)
    results = indeed_api_response['results']

    for job in results:
        r = requests.get(job['url']).text
        soup = BeautifulSoup(r, "html.parser")
        job_descriptions = soup.find_all(id="job_summary")
        for job_desc in job_descriptions:
            job['full_description'] = job_desc.get_text()
            job['description_tokenized'] = tokenize(job_desc.get_text()) 

    return render_template('model_train_jobs.html', 
                           results=results,
                           results_json=json.dumps(results),
                           dataset_name=(query + " - " + city));


if __name__ == "__main__":
    app.run()
