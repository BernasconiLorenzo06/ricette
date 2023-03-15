from flask import Flask,render_template
app = Flask(__name__)

import datetime

if ora == 12:
    ora = pranzo
else:
    ora == 19:
    ora = cena


@app.route('/', methods=['GET'])
def home():
    return render_template('tre.html')

@app.route('/pizza', methods=['GET'])
def pizza():
    return render_template('pizza.html')
    
@app.route('/sushi', methods=['GET'])
def sushi():
    return render_template('sushi.html')

@app.route('/pasta', methods=['GET'])
def pasta():
    return render_template('pasta.html')

@app.route('/hamburger', methods=['GET'])
def hamburger():
    return render_template('hamburger.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)