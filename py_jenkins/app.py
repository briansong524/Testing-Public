# Simple Flask Script 

# Run a simple flask script through jenkins pipeline

import Flask

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def main():
    name = request.form.get('name')

    return 'Hello ' + str(name)

if __name__ == '__main__':
    app.run(debug=False, port=8000, host='0.0.0.0')