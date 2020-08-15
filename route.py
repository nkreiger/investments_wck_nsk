# Flask file.
import jinja2
from flask import Flask, json, jsonify, render_template, request, make_response
from jinja2 import Environment, select_autoescape
from os.path import dirname
from _operator import itemgetter
from operator import itemgetter
import accessor
import json
import pandas as pd
import numpy as np

env = Environment(autoescape=select_autoescape(['html', 'xml']),
                  loader=jinja2.FileSystemLoader( dirname(__file__) + "/templates/" ))

app = Flask(__name__)

@app.route("/wrds-data-model/")
def index():
    return render_template( "home.html" )

@app.route("/wrds-data-model/get_libraries/")
def getLibraries():
    libraries = None

    libraries = accessor.getAllLibraries()
    
    print(libraries)
    
    return json.dumps(libraries)

@app.route("/wrds-data-model/get_tables/<library>")
def getTablesForLibrary(library):
    data = None

    data = accessor.getTables(library)

    print(data)
    
    return json.dumps(data)

@app.route("/wrds-data-model/get_table_data")
def getTableData():
    data = None
    tableList = []
    library = request.args.get('library', None)
    table = request.args.get('table', None)

    data = accessor.getTableData(library, table)

#    tableList.append(list(data))

 #   print("column headers: " + str(list(data)));

    tableList.append(data[data.columns[2:4]])

    return data.to_json()

@app.route("/wrds-data-model/get_table_data/<query>")
def getQueryResults(query):
    data = None

    data = accessor.executeQuery(query)

    print(data)

    return json.dumps(data)