from flask import Flask, render_template

import redis
import json

app = Flask(__name__)

redis_config = json.load(open("redis.json", "r"))

r = redis.Redis(
    host=redis_config["host"],
    port=redis_config["port"],
    db=redis_config["db"],
    password=redis_config["auth"],
    decode_responses=True
)

@app.route("/")
def index():
    return render_template("index.html", index=True)

@app.route("/thanks")
def thanks():
	return render_template("thanks.html")

@app.route("/api/v1/servers")
def get_servers():
    servers = 0
    for shard_key in r.keys("shard-*:servers"):
        servers += int(r.get(shard_key))

    return str(servers)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)
