import requests

url = "https://openai80.p.rapidapi.com/chat/completions"

payload = {
	"model": "gpt-3.5-turbo",
	"messages": [
		{
			"role": "user",
			"content": "Addition of two numbers program"
		}
	]
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "d68c7a4ca0mshfe7db0559a72ad6p1f118fjsnb3beeaa77aac",
	"X-RapidAPI-Host": "openai80.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

choice = response.json()['choices']
list =  choice[0]
message = list['message']
print(message)