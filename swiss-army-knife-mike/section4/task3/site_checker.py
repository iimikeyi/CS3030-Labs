import requests

urls = [
	"https://www.google.com",
	"https://www.github.com",
	"https://www.this-site-does-not-exist-fake.com",
]

for url in urls:
	try:
		response = requests.get(url, timeout=5)
		if response.status_code == 200:
			print(f"UP {url}")
		else:
			print(f"DOWN {url} (status: {response.status_code})")
	except requests.exceptions.RequestException:
		print(f"DOWN {url} (unreachable)")
