"""Loopback-only offline app server. No external requests or broker integration."""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from market_model import evaluate

ROOT = Path(__file__).resolve().parent
ASSETS = {"/": ("web/index.html", "text/html; charset=utf-8"),
          "/app.js": ("web/app.js", "text/javascript; charset=utf-8"),
          "/style.css": ("web/style.css", "text/css; charset=utf-8"),
          "/example.json": ("examples/study.json", "application/json")}

class Handler(BaseHTTPRequestHandler):
    def respond(self, code, data, content_type="application/json"):
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self'; object-src 'none'; frame-ancestors 'none'")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        asset = ASSETS.get(self.path)
        if asset is None:
            self.respond(404, b'{"error":"Not found"}')
            return
        self.respond(200, (ROOT / asset[0]).read_bytes(), asset[1])

    def do_POST(self):
        if self.path != "/api/evaluate":
            self.respond(404, b'{"error":"Not found"}')
            return
        # Block cross-site browser submissions; app requests use this JSON header.
        if self.headers.get("X-ResearchOS") != "offline" or self.headers.get("Content-Type") != "application/json":
            self.respond(403, b'{"error":"Local JSON app request required"}')
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= 1000000:
                raise ValueError("Body must be 1–1000000 bytes")
            study = json.loads(self.rfile.read(length))
            report = evaluate(study)
            self.respond(200, json.dumps(report, allow_nan=False).encode())
        except (ValueError, TypeError, KeyError) as error:
            self.respond(400, json.dumps({"error": str(error)}).encode())

    def log_message(self, *_args):
        pass

if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
