from django.shortcuts import render

from .forms import TextInputField, TwitterHandleField, ExtraversionField, IntuitionField, FeelingField, PerceptionField

from bs4 import BeautifulSoup
import urllib.request
import certifi

# Create your views here.
def home_view(request, *args, **kwargs):	# *args, **kwargs

	textInputField = TextInputField(request.POST or None)
	twitterHandleField = TwitterHandleField(request.POST or None)

	extraversionField = ExtraversionField(request.POST or None)
	intuitionField = IntuitionField(request.POST or None)
	feelingField = FeelingField(request.POST or None)
	perceptionField = PerceptionField(request.POST or None)

	twitter_search = False

	if request.method == "POST":
		if textInputField.is_valid():
			text_field_data = textInputField.cleaned_data.get('text_field')
			if text_field_data:
				twitter_search = False
		if extraversionField.is_valid():
			extraversion_data = extraversionField.cleaned_data.get('extraversion_field')
		if intuitionField.is_valid():
			intuition_data = intuitionField.cleaned_data.get('intuition_field')
		if feelingField.is_valid():
			feeling_data = feelingField.cleaned_data.get('feeling_field')
		if perceptionField.is_valid():
			perception_data = perceptionField.cleaned_data.get('perception_field')
			print(perception_data)


		if twitterHandleField.is_valid():
			twitter_field_data = twitterHandleField.cleaned_data.get('twitter_handle')
			if twitter_field_data:
				twitter_search = True





	context = {
		"textInputField":textInputField,
		"twitterHandleField":twitterHandleField,
		"extraversionField":extraversionField,
		"intuitionField":intuitionField,
		"feelingField":feelingField,
		"perceptionField":perceptionField,


		"twitter_search":twitter_search,

	}
	return render(request, "home_view.html", context)