from flask import Flask, render_template
from flask import request
from flask import Response
import errors
import helper
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  error = errors.error('param')
  response = Response(response=error, status=200, headers=None, mimetype='text/javascript', content_type=None, direct_passthrough=False)
  return response
 
@app.route('/class')
def classes():
	some_class = helper.MITClass()
	message = some_class.get_class_info("6.01")
	response = Response(response=message, status=200, headers=None, mimetype='text/javascript', content_type=None, direct_passthrough=False)	
	return response

if __name__ == '__main__':
  app.run(debug=True)