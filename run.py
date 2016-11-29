from flask import Flask, render_template

import redis
import os

app = Flask(__name__)

r = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    db=int(os.getenv("REDIS_DB")),
    password=os.getenv("REDIS_PASSWORD"),
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
    app.run(host="0.0.0.0", port=8080, debug=False)
