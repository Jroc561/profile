from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def base():
    return render_template('base.html')

#app.run(host='0.0.0.0', port=5000)
if __name__ == '__main__':
    app.run()