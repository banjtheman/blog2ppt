import requests


print("Testing api")
testing_url = "https://ixdgqj6lrhyzndf3cu2ase6pfy0adgxb.lambda-url.us-east-1.on.aws/"
data = {"blog_url":"https://dev.to/banjtheman/dc-fire-and-ems-data-visualizer-4a6l"}
req = requests.post(testing_url,json=data)
print(req.json())
print("Done and done")