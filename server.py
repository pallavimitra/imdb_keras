from flask import Flask, jsonify, make_response, request
import traceback 
import predict

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def run():
    try:
        print("Request Recieved")
        data = request.get_json(force=True)
        print({'data recived' : data})
        input_params = data['input']
        print({'input recived' : input_params})
        result =  predict.predict(input_params)
        print('prediction')
        print(result)
        #return jsonify({'prediction': result})
        #return "Hello World!!"
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)})

'''@app.route('/score', methods=['POST'])
def score():
    features = request.json['X']
    return make_response(jsonify({'score': features}))'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
