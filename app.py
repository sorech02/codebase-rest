from flask import Flask, jsonify, abort, make_response, url_for

app = Flask(__name__)

cvxs = [
    {
        'id': 143,
        'label': 'Adenovirus types 4 and 7',
        'description': 'Adenovirus, type 4 and type 7, live, oral Notes: This vaccine is administered as 2 tablets.',
        'status': 'Valid',
    },
    {
        'id': 54,
        'label': 'adenovirus, type 4',
        'description': 'adenovirus vaccine, type 4, live, oral',
        'status': 'Valid',
    },
]


@app.route('/codeset/cvx')
def get_all_cvx():
    return jsonify({'cvxs': [build_instance_uri(cvx) for cvx in cvxs]})

@app.route('/codeset/cvx/<int:cvx_id>', methods=['GET'])
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

