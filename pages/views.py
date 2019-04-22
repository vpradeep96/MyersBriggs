from django.shortcuts import render

from .forms import TextInputField, TwitterHandleField

from bs4 import BeautifulSoup
import urllib.request
import certifi
import pymongo
import sklearn

import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

from sklearn import linear_model

from sklearn.feature_extraction.text import CountVectorizer

import pickle
from sklearn.externals import joblib


client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.pymongo
inty = db.introversion
postos = db.posts

# Create your views here.
def home_view(request, *args, **kwargs):	# *args, **kwargs
	textInputField = TextInputField(request.POST or None)
	twitterHandleField = TwitterHandleField(request.POST or None)

	# extraversionField = ExtraversionField(request.POST or None)
	# intuitionField = IntuitionField(request.POST or None)
	# feelingField = FeelingField(request.POST or None)
	# perceptionField = PerceptionField(request.POST or None)
	# myersBriggsTypesField = MyersBriggsTypesField(request.POST or None)

	twitter_search = False

	if request.method == "POST":
		if textInputField.is_valid():
			username_data = textInputField.cleaned_data.get('username')
			text_field_data = textInputField.cleaned_data.get('text_field')
			extraversion_data = textInputField.cleaned_data.get('extraversion_field')
			intuition_data = textInputField.cleaned_data.get('intuition_field')
			feeling_data = textInputField.cleaned_data.get('feeling_field')
			perception_data = textInputField.cleaned_data.get('perception_field')
			

			obj = {
				'username': username_data,
				'T/F': feeling_data[0],
				'N/S': intuition_data[0],
				'P/J': perception_data[0],
				'E/I': extraversion_data[0],
			}
			found = postos.find_one({'username': username_data})
			if (found is None):
				obj['posts'] = [text_field_data]
				obj['variance'] = 0
				obj['stdDev'] = 0
				obj['average'] = len(text_field_data.split(' '))
				obj['avgWordLength'] = (len(text_field_data)-obj['average'])/obj['average']
				postos.insert_one(obj)
			else:
				found['posts'].append(text_field_data)
				
				vectorizer = joblib.load('vectorizer1.pkl')
				
				
				#the four models 
				
				json_file = open('model.json', 'r')
				loaded_model_json = json_file.read()
				json_file.close()
				model1 = model_from_json(loaded_model_json)
				model2 = model_from_json(loaded_model_json)
				model3 = model_from_json(loaded_model_json)
				model4 = model_from_json(loaded_model_json)
				# load weights into new model
				model1.load_weights("modely1.h5")
				model2.load_weights("modely2.h5")
				model3.load_weights("modely3.h5")
				model4.load_weights("modely4.h5")
				
				model1.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
				model2.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
				model3.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
				model4.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
				
				
				#Encoders & Decoders
				
				enc1 = joblib.load('enc1.pkl')
				enc2 = joblib.load('enc2.pkl')
				enc3 = joblib.load('enc3.pkl')
				enc4 = joblib.load('enc4.pkl')
				
				#
				
				
				
				obj['posts'] = found['posts']
				hello = len(text_field_data.split(' '))
				totalPosts = len(found['posts'])
				obj['average'] = (found['average']*totalPosts+hello)/totalPosts+1
				obj['stdDev'] = (found['stdDev'] + (hello-obj['average']) * (hello-obj['average'])) /(totalPosts+1)
				avgWordLength = (len(text_field_data)-obj['average'])/obj['average']
				obj['avgWordLength'] = (avgWordLength + found['avgWordLength']*totalPosts)/totalPosts
				obj['variance'] = obj['stdDev'] * obj['stdDev']
				postos.replace_one({'username': username_data}, obj)
			
			if text_field_data:
				twitter_search = False
				context = {
					"username_data":username_data,
					"text_field_data":text_field_data,
					"extraversion_data":extraversion_data,
					"intuition_data":intuition_data,
					"feeling_data":feeling_data,
					"perception_data":perception_data,
				}
				return render(request, "results.html", context)
			else:
				pass

		"""
		Currently the user can type in values into the boxes and 
		"""


	context = {
		"textInputField":textInputField,
		"twitterHandleField":twitterHandleField,
		# "myersBriggsTypesField":myersBriggsTypesField,
		# "extraversionField":extraversionField,
		# "intuitionField":intuitionField,
		# "feelingField":feelingField,
		# "perceptionField":perceptionField,

		"twitter_search":twitter_search,

	}
	return render(request, "home_view.html", context)


