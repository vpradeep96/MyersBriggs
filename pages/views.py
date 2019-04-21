from django.shortcuts import render

from .forms import TextInputField, TwitterHandleField

from bs4 import BeautifulSoup
import urllib.request
import certifi

# Create your views here.
def home_view(request, *args, **kwargs):	# *args, **kwargs

	textInputField = TextInputField(request.POST or None)
	twitterHandleField = TwitterHandleField(request.POST or None)

	twitter_search = False

	if request.method == "POST":
		if textInputField.is_valid():
			text_field_data = textInputField.cleaned_data.get('text_field')
			if text_field_data:
				twitter_search = False
		if twitterHandleField.is_valid():
			twitter_field_data = twitterHandleField.cleaned_data.get('twitter_handle')
			if twitter_field_data:
				twitter_search = True




	context = {
		"textInputField":textInputField,
		"twitterHandleField":twitterHandleField,
		"twitter_search":twitter_search,
	}
	return render(request, "home_view.html", context)