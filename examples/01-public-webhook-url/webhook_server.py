#!/usr/bin/env python3
"""Dependency-free webhook receiver for the Route6 public-URL example.

Listens on localhost:8080 and prints every request it receives.
Expose it with:  route6 tunnel start --hostname my-agent --to 8080
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class Hook(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length).decode(errors='replace')
        print(f'{self.command} {self.path}')
        for k, v in self.headers.items():
            print(f'  {k}: {v}')
        try:
            print('  body:', json.dumps(json.loads(body), indent=2))
        except ValueError:
            print('  body:', body)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"ok": true}')

    do_GET = do_POST

    def log_message(self, *args):
        pass  # request details are printed in do_POST


if __name__ == '__main__':
    print('webhook receiver on http://127.0.0.1:8080 — Ctrl+C to stop')
    HTTPServer(('127.0.0.1', 8080), Hook).serve_forever()
