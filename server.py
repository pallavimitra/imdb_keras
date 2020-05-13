from flask import Flask, jsonify, make_response, request
import traceback 
import predict

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def run():
    try:
        data = request.get_json(force=True)
        #input_params = data['input']
        #result =  predict.predict(input_params)
        #return jsonify({'prediction': result})
        return jsonify({'data': data})
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)})

'''@app.route('/score', methods=['POST'])
def score():
    features = request.json['X']
    return make_response(jsonify({'score': features}))'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
