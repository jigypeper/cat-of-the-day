from flask import Flask, render_template
import random
import requests
import shutil

app = Flask(__name__)

@app.route("/cats")
def get_cat():
    urls = 'https://api.thecatapi.com/v1/images/search'
    cat_breeds = str(random.choice(['bengal', 'siamese', 'persian', 'ragdoll']))
    querystring = {"mime_types":"png","limit":"1","breed":cat_breeds}
    header = {"Content-Type": "application/json",'x-api-key':'<API KEY HERE>'}
    response = requests.get(urls, headers= header, params=querystring)
    img_url = response.json()[0]['url']
    res = requests.get(img_url, stream= True)

    if res.status_code == 200:
        with open(f'static/{"cat-of-the-day"}.png', 'wb') as handler:
            shutil.copyfileobj(res.raw, handler)
    
    return render_template("cats.html")
