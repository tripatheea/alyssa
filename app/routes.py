from flask import Flask, render_template
from flask import request
from flask import Response
import errors
from helper import *
import json
import requests


app = Flask(__name__)      
 
@app.route('/')
def home():
  error = errors.error('param')
  response = Response(response=error, status=200, headers=None, mimetype='text/javascript', content_type=None, direct_passthrough=False)
  return response
 
@app.route('/class', methods = ['GET'])
def classes():
	which_class = request.args.getlist('class')[0]
	what_info = request.args.getlist('type')[0]

	some_class = MITClass()
	message = some_class.get_class_info(which_class, what_info)
	message = json.dumps(message)
	response = Response(response=message, status=200, headers=None, mimetype='text/javascript', content_type=None, direct_passthrough=False)	
	
	return response

@app.route('/quizzes', methods = ['GET'])
def quizzes():
   exam = MITExam()
   return exam.all_exams()

@app.route('/WAYF', methods = ['GET', 'POST'])
def WAYF():
   r = requests.post(constants.url['stellar'], data=request.args)
   return r.content

if __name__ == '__main__':
  app.run(debug=True)