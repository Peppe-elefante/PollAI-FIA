from flask import Flask, request, jsonify
import pandas as pd
import py_eureka_client.eureka_client as eureka_client
import socket

# Get the correct IP address to register with Eureka
hostname = socket.gethostbyname(socket.gethostname())

rest_port = 8050
eureka_client.init(eureka_server="http://localhost:8761/eureka",
                   app_name="uova-service",
                   instance_port=rest_port,
                   instance_ip = hostname)

app = Flask(__name__)

@app.route("/predizione", methods=['POST'])
def hello():
    data = request.json
    df = pd.DataFrame(data)
    print(df.head())
    response_value = 30
    return jsonify({"prediction": response_value})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = rest_port)