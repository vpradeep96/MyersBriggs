from django.shortcuts import render

from .forms import TextInputField, TwitterHandleField

from bs4 import BeautifulSoup
import urllib.request
import certifi

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
			# print("Text Field:", text_field_data)
			# print("Extraversion:", extraversion_data)
			# print("Intuition:", intuition_data)
			# print("Feeling:", feeling_data)
			# print("Perception:", perception_data)

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




		if twitterHandleField.is_valid():
			twitter_field_data = twitterHandleField.cleaned_data.get('twitter_handle')
			if twitter_field_data:
				twitter_search = True

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


