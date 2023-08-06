import json


def format_json(jsondata):
	data = json.loads(jsondata)
	output = f"Name: {data['name']}\nUUID: {data['id']}"
	return output


def rem_hyphen(instring):
	return str(instring).replace('-', '')

