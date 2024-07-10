from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    try:
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        res = requests.get(
            "https://dummy.restapiexample.com/api/v1/employees", headers=headers)
        res.raise_for_status()  # Raises HTTPError for bad responses

        # Debugging information
        print("Response Headers:", res.headers)
        print("Response Content:", res.text)

        data = res.json()  # Attempt to parse JSON
        return jsonify(data)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return f"HTTP error occurred: {http_err}", 500
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        return f"Request error occurred: {req_err}", 500
    except ValueError as json_err:
        print(f"JSON decode error occurred: {json_err}")
        return f"JSON decode error occurred: {json_err}", 500


if __name__ == '__main__':
    app.run(debug=True)
