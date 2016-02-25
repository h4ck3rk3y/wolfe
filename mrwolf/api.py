import requests
import webbrowser
from tabulate import tabulate 
headers = {'Accept' : 'application/json'}


def stackoverflow(error,tag):

	tags = tag.split()
	if tags[0] == "sudo":
		res_tag = tags[1]
	else:
		res_tag = tags[0]


	url = 'https://api.stackexchange.com/2.2/search/advanced?order=desc&migrated=False&sort=activity&body=%s&tags=%s&accepted=True&closed=False&site=stackoverflow&key=BFKqtwHwltVKHrSIDKgf6Q((' % (error,res_tag)
	try:
		response = requests.get(url, headers = headers)

		if response.status_code == 200:	
			data = response.json()
			result_dict = []
			if len(data['items']) > 0:
				webbrowser.open_new_tab(data['items'][0]['link'])
				for i in range(1,min(6,len(data['items']))):
					res_dict = {}				
					res_dict['title'] = data['items'][i]['title']
					res_dict['link'] = data['items'][i]['link']
					result_dict.append(res_dict) 
				print tabulate([[i['title'][:50],i['link']] for i in result_dict], headers = ['Title','Link'],tablefmt="simple_grid")
					
			else:
				print "Substantial answers not found"
		else:
			print "Api Issues"
	except:
		print "Network Issues"


