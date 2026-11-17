import json
import threading
import unittest
from http.server import ThreadingHTTPServer
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from pathlib import Path
from server import Handler

class ServerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = "http://127.0.0.1:" + str(cls.server.server_port)

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def test_assets_and_example(self):
        for path in ("/", "/app.js", "/style.css", "/example.json"):
            with urlopen(self.base + path) as response:
                self.assertEqual(response.status, 200)

    def test_json_evaluation(self):
        data = Path("examples/study.json").read_bytes()
        request = Request(self.base + "/api/evaluate", data=data,
                          headers={"Content-Type": "application/json", "X-ResearchOS": "offline"})
        with urlopen(request) as response:
            report = json.load(response)
        self.assertEqual(report["schema"], "researchos-market-resilience/v1")
        self.assertFalse(report["executionAuthorized"])

    def test_arbitrary_paths_and_cross_site_post_blocked(self):
        for request, code in ((self.base + "/../market_model.py", 404),
                              (Request(self.base + "/api/evaluate", data=b"{}"), 403)):
            with self.assertRaises(HTTPError) as context:
                urlopen(request)
            self.assertEqual(context.exception.code, code)

    def test_malformed_study_rejected(self):
        request = Request(self.base + "/api/evaluate", data=b"{}",
                          headers={"Content-Type": "application/json", "X-ResearchOS": "offline"})
        with self.assertRaises(HTTPError) as context:
            urlopen(request)
        self.assertEqual(context.exception.code, 400)
