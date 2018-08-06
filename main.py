from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Congratulations Nigel, you have deployed your first Azure webapp !  '

if __name__ == '__main__':
  app.run()
