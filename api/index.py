import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Load data
        with open("data.json", "r") as f:
            data = json.load(f)

        # Parse query parameters
        query = parse_qs(self.path[1:])
        names = query.get("name", [])

        # Fetch marks
        marks = [data["students"].get(name, "Not found") for name in names]

        # Send response
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")  # Enable CORS
        self.end_headers()
        self.wfile.write(json.dumps({"marks": marks}).encode("utf-8"))
