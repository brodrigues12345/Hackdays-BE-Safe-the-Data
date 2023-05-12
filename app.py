from flask import Flask, request, jsonify

def convert_to_safe_date(file_path):
    # here will be the code that changes XML tags
    pass

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_route():
    data = request.get_json()
    file_path = data.get('file_path')
    if not file_path:
        return jsonify({"error": "No file path provided"}), 400

    try:
        changes = convert_to_safe_date(file_path)
        return jsonify({"message": "File successfully converted", "changes": changes}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)

# how to test this route:
# curl -X POST -H "Content-Type: application/json" -d '{"file_path":"/path/to/your/file"}' http://localhost:5000/convert
