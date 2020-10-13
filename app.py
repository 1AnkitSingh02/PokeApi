from flask import Flask,jsonify,request
import csv
import json

app = Flask(__name__)

@app.route('/pokemon/all',methods=['GET'])
def pokemon():
    with open('./poke.json','r') as jsonfile:
        file_data = json.loads(jsonfile.read())
        return file_data
        # res= request.get_json(json.dumps(file_data))
        

@app.route('/')
def home():
    return '''<h1>All Pokemon Data</h1>
<p>Pokemon Data with some Specs</p>'''

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/pokemon', methods=['GET'])
def poke_filter():
    name = str(request.args['name']).lower()

    # name = query_parameters.get('Name')
    with open('./poke.json','r') as jsonfile:
        file_data = json.loads(jsonfile.read())
        return jsonify(file_data[name])
 
if __name__=='__main__':
    app.run(debug=True)