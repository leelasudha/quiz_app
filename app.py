from flask import Flask, request, jsonify, render_template
import os
import requests
import random
app = Flask(__name__)

#def index():
#    return "<h1>Welcome to our server !!</h1>"


url = 'https://opentdb.com/api.php?amount=10'
r = requests.get(url)
api_response = r.json()
questions = []
options =[]
correct_answer = []
@app.route('/', methods= ["GET","POST"])
def index():
	if request.method == "POST":
		
		name = request.form.get("option")
		print(name)
		data = api_response['results']
		for i in data:
			if i['correct_answer'] not in i['incorrect_answers']:
				i['incorrect_answers'].append(i['correct_answer'])
			random.shuffle(i['incorrect_answers'])
			if len(questions) < 11:
				questions.append(i['question'])
				options.append(i['incorrect_answers'])
				correct_answer.append(i['correct_answer'])
		context =  zip(questions,options, correct_answer, )
		return render_template( 'index.html', context = context, name = name)
	context =  zip(questions,options, correct_answer)
	
	return render_template( 'index.html', context = context)
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=8888)  
