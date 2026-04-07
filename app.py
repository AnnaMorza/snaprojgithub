from flask import Flask
import os
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Docker App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
                background-color: #f0f0f0;
            }
            h1 {
                color: #333;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                max-width: 600px;
                margin: 0 auto;
            }
            .time {
                color: #666;
                font-size: 14px;
                margin-top: 20px;
            }
            .badge {
                background-color: #4CAF50;
                color: white;
                padding: 5px 10px;
                border-radius: 5px;
                display: inline-block;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello from Anna Morozova</h1>
            <div class="badge">✅ CI/CD works</div>
            <div class="time">Time: ''' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '''</div>
        </div>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)