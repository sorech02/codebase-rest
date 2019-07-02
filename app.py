import ast

from flask import Flask, jsonify, abort, make_response, url_for

app = Flask(__name__)

with open('cvx.txt', 'r') as f:
    cvxs = ast.literal_eval(f.read())

@app.route('/codeset/cvx')
def get_all_cvx():
    return jsonify({'cvxs': [build_instance_uri(cvx) for cvx in cvxs]})

@app.route('/codeset/cvx/<cvx_id>', methods=['GET'])
def get_cvx(cvx_id):
    cvx = [cvx for cvx in cvxs if cvx['id'] == cvx_id]
    if len(cvx) == 0:
        abort(404)
    return jsonify({'cvx': cvx[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def build_instance_uri(instance):
    new_instance = {}
    for field in instance:
        if field == 'id':
            new_instance['uri'] = url_for('get_cvx', cvx_id=instance['id'], _external=True)
        else:
            new_instance[field] = instance[field]
    return new_instance

