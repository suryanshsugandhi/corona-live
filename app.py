from flask import Flask, request
from data_builder import DataBuilder

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/trackerdata', methods=['POST'])
def tracker_data():
    d = DataBuilder()
    return d.tracker_data()

@app.route('/regiondata', methods=['POST'])
def region_data():
    d = DataBuilder()
    region = request.args.get('region')
    return d.region_data(region)

if __name__ == '__main__':
    app.run()