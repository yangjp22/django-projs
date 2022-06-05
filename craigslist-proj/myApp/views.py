from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from requests.compat import quote_plus
from lxml import etree
from . import models

BASE_URL = 'https://sfbay.craigslist.org/search/jjj?query={}'

# Create your views here.
def home(request):
	return render(request, 'base.html')


def search(request):

	search = request.POST.get('search')

	models.Search.objects.create(search = search)
	searchUrl = BASE_URL.format(quote_plus(search))

	response = requests.get(searchUrl)

	data = response.text

	obj = etree.HTML(data)

	infoReg = '//*[@id="sortable-results"]/ul/li/p'
	infos = obj.xpath(infoReg)
	infoDict = {'title': 'a/text()', 'link': 'a/@href', 'time': 'time/@datetime', 'location':'span[2]/span[@class="result-hood"]/text()'}
	finalList = []
	for info in infos[:80]:
		interDict = {}
		for key in infoDict:
			if info.xpath(infoDict[key]):
				interDict[key] = info.xpath(infoDict[key])[0].strip().replace('(', '').replace(')', '')
			else:
				interDict[key] = 'NA'
		finalList.append(interDict)


	stuffForFronted = {
		'search': search,
		'finalList': finalList,

	}
	return render(request, 'myApp/search.html', stuffForFronted)


def searchHome(request):
	return JsonResponse({'msg': 'Welcome', 'code': 200})


def craigslist(request):
	return JsonResponse({'msg': 'craigslist', 'code': 200})