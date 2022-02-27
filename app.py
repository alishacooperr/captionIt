from flask import Flask, render_template, request, flash
from pandas import DataFrame
import pandas as pd
import random

app = Flask(__name__)
app.secret_key = "cats101"

@app.route("/caption")
def index():
		flash("What is a word that describes your image?")
		return render_template("index.html")

@app.route("/enter", methods=["POST", "GET"])
def enter():

	words_Arr = ["party","drinks","alcohol","books","university","school","coffee","food","water","ocean","sand","sunny","sun","picnic","summer","spring","winter","autumn","cold","snow","breakfast","brunch","lunch","dinner","love","romance","sex","kiss","bed","valentine","relationship","ootd","top","bottom","clothing","company","sponsor","fit","motivated","sports","workout","lift","depression","emo","moody","dark","black"]
	user_input = str(request.form['words_input'])
	user_Arr = user_input.split()

	if len(user_Arr) == 0:
		flash("We can't give you a caption if we don't know what your picture looks like! Please enter a word <3")
	elif len(user_Arr) > 1:
		flash("Hey lovely! Please enter one word only to describe your picture xoxo")
	
	else:
		if user_input.lower() in words_Arr:
			df = pd.read_csv("captions.csv")
			listofrows = df.values.tolist()
			for row in listofrows:
				if row[0] == user_input.lower():

					stop = 0
					for i in row:
						if i == "none":
							stop = row.index(i)
							break


					targetCaption = row[random.randint(1,stop-1)]
					flash(targetCaption)
					break

		else:
			flash("Soz that word isn't in our system :( Please enter another word so that we can find your perfect caption!")

	return render_template("index.html")