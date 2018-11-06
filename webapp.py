import requests

def fetch_details(id):
	response = requests.get("http://localhost:3000/duration", data = {"id":id})
	return response
