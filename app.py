# -*- coding: utf-8 -*-
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import requests
from parse import *
from mitie import *
from bs4 import BeautifulSoup
import json
from mitie import *
import nltk
import sys, os

# import mitie lib
parent = os.path.dirname(os.path.realpath(__file__))
print parent
sys.path.append('/home/jayden/Documents/Hackathon/McHacks2017/MITIE/mitielib')

# setup app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('query_form.html')

@app.route("/jobs_form")
def jobs_form():
    return render_template('query_form_jobs.html')

@app.route("/train", methods=['POST'])
def train():
    input_data = request.form.get('input_data');
    entities = request.form.get('entities')
    outputVar = request.form.get('outputVar')
    return render_template('model_train.html', input_data=input_data, entities=entities, outputVar=outputVar)

@app.route("/train_vue", methods=['POST'])
def train_vue():
    input_data = request.form.get('input_data');
    entities = request.form.get('entities')
    outputVar = request.form.get('outputVar')
    return render_template('model_train_vue.html', input_data=input_data, entities=entities, outputVar=outputVar)

@app.route("/parse_job", methods=['GET'])
def parse_job_get():
    return render_template('query_form_job_description.html')

@app.route("/parse_job", methods=['post'])
def parse_job_post():
    data = request.form.get('input_data')
    ner = named_entity_extractor("mitie_training/25_dev.dat")
    tokens = custom_tokenize(data)
    entities = ner.extract_entities(tokens)
    return_data = []

    for e in entities:
        r = e[0]
        tag = e[1]
        entity_text = " ".join(tokens[i] for i in r)
        if len(entity_text) > 1:
            entity_text = entity_text.replace(' ', '');
            return_data.append(entity_text)

    return_data = list(set(return_data))
    output_data = ""

    for entity in return_data:
        output_data += '<span class=\"token\">' + entity + '</span>';

    return render_template('job_desc.html', input_data=data, output_data=output_data)

@app.route("/jobs_json")
def jobs_json():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr);
    user_agent = request.headers.get('User-Agent');
    indeed_api_params = {
        'publisher': 9978236252243350,
        'v': 2,
        'callback': 'hello',
        'q': 'Developer',
        'l': 'Toronto, ON',
        'st': 'jobsite',
        'co': 'ca',
        'limit': '100',
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

    token_array = []

    for job in results:
        r = requests.get(job['url']).text
        soup = BeautifulSoup(r, "html.parser")
        job_descriptions = soup.find_all(id="job_summary")
        for job_desc in job_descriptions:
            job['full_description'] = job_desc.get_text()
            job['description_tokenized'] = custom_tokenize(job_desc.get_text()) 
            token_array.append(job['description_tokenized'])

    response = app.response_class(
        response=json.dumps(token_array),
        status=200,
        mimetype='application/json'
    ) 

    return response

@app.route("/train_jobs")
def train_jobs():
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
            job['description_tokenized'] = custom_tokenize(job_desc.get_text()) 

    return render_template('model_train_jobs.html', 
                           results=results,
                           results_json=json.dumps(results),
                           dataset_name=(query + " - " + city));

def custom_tokenize(s):
    s = s.replace(';', ' , ')
    s = s.replace('/', ' , ')
    s = mitie.tokenize(s)
    return s

if __name__ == "__main__":
    app.run()
