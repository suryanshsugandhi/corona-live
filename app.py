from flask import Flask, request
from data_builder import DataBuilder

app = Flask(__name__)

# ROUTES FOR DATA
@app.route('/trackerdata', methods=['POST'])
def tracker_data():
    return d.tracker_data()

@app.route('/regiondata', methods=['POST'])
def region_data():
    region = request.args.get('region')
    return d.region_data(region)

@app.route('/totaldata', methods=['POST'])
def total_data():
    return d.total_data()

# ROUTES FOR NEWS
@app.route('/news', methods=['POST'])
def method_name():
    pass

if __name__ == '__main__':
    d = DataBuilder()
    app.run()