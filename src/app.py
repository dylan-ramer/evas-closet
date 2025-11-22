from flask import Flask
#Flask app constructor
app = Flask(__name__)

#Decorator to establish default route
@app.route('/')
def main():
    return "Hello, Welcome to Eva's Closet"

if __name__=='__main__':
    app.run(debug=True)