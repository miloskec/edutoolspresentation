#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 3367
ROOT = os.path.abspath(os.path.dirname(__file__))  # folder gde je index.html

if __name__ == "__main__":
    # Serve everything from ROOT (index.html, CSS, JS, slike...)
    os.chdir(ROOT)

    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.ThreadingTCPServer(("", PORT), handler) as httpd:
        print(f"Serving at http://localhost:{PORT} (Ctrl+C to stop)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            httpd.server_close()
