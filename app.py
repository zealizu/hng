from flask import Flask, Response, jsonify
from flask_cors import CORS
import requests
from datetime import datetime, timezone
import json

app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def home():
    return "Welcome to HNG"

@app.route("/me", methods=["GET"])
def handle_fetch():
    url = "https://catfact.ninja/fact"
    
    try:
        response = requests.get(url=url , timeout=5)
        response.raise_for_status()
        data = response.json()["fact"]
        time = (datetime.now(timezone.utc)).isoformat()
        result={
            "status": "success",
            "user": {
                "email": "zealizu@gmail.com",
                "name": "Izuchukwu Chidubem Zeal",
                "stack": "Flask"
            },
            "timestamp": time,
            "fact": data
            }
        json_string = json.dumps(result, indent=2)
        return Response(json_string, mimetype='application/json')
    except requests.exceptions.Timeout:
        return jsonify("The request to the external API timed out. Please try again later.",
            "Timeout occurred"),504
    except requests.exceptions.ConnectionError:
        return jsonify("Could not connect to the external API. Service may be temporarily unavailable.",
            "Connection error",),503
    except requests.exceptions.HTTPError as e:
        return jsonify("External API returned an error.",
            f"Status code: {e.response.status_code}",),502
    except Exception as e:
        return jsonify("An unexpected error occurred.",
            str(e)), 500


@app.route("/name", methods=["GET"])
def get_name():
    url = "https://catfact.ninja/fact"
    
    try:
        response = requests.get(url=url , timeout=5)
        response.raise_for_status()
        data = response.json()["fact"]
        time = (datetime.now(timezone.utc)).isoformat()
        result={
            "timestamp": time,
            "fact": data
            }
        json_string = json.dumps(result, indent=2)
        return Response(json_string, mimetype='application/json')
    except requests.exceptions.Timeout:
        return jsonify("The request to the external API timed out. Please try again later.",
            "Timeout occurred"),504
    except requests.exceptions.ConnectionError:
        return jsonify("Could not connect to the external API. Service may be temporarily unavailable.",
            "Connection error",),503
    except requests.exceptions.HTTPError as e:
        return jsonify("External API returned an error.",
            f"Status code: {e.response.status_code}",),502
    except Exception as e:
        return jsonify("An unexpected error occurred.",
            str(e)), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
 