from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    # Menampilkan pesan sederhana
    return 'Hello World from Docker!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

