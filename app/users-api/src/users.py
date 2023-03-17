import os
import requests

from flask import Flask

app = Flask(__name__)

db_api_url = "http://a7d8063cee700472c9353bb557bbff40-301760262.us-east-2.elb.amazonaws.com/"         
@app.route('/users')
def users():
    user_from_db = requests.get(f"{db_api_url}/users")
    print(user_from_db)
    return user_from_db.json()



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
