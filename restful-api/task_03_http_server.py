#!/usr/bin/python3
"""Simple API using the http.server module."""
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """Handle GET requests for a simple API."""

    def _send(self, code, content_type, body):
        """Send a response with the given code, type and body."""
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def do_GET(self):
        """Route GET requests to the right endpoint."""
        if self.path == "/":
            self._send(200, "text/plain", "Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send(200, "application/json", json.dumps(data))
        elif self.path == "/status":
            self._send(200, "text/plain", "OK")
        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self._send(200, "application/json", json.dumps(info))
        else:
            self._send(404, "text/plain", "Endpoint not found")


def run(server_class=http.server.HTTPServer,
        handler_class=SimpleAPIHandler, port=8000):
    """Start the server on the given port."""
    server = server_class(("", port), handler_class)
    print(f"Serving on port {port}...")
    server.serve_forever()


if __name__ == "__main__":
    run()
