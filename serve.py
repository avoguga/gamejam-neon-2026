#!/usr/bin/env python3
"""
Servidor local que espelha o que o Coolify serve.

  /         -> index.html        (protótipo HTML de testes)
  /unity/   -> unity/index.html  (build WebGL da Unity, .unityweb)

Os .unityweb (Gzip + Decompression Fallback) NÃO precisam de header especial.

Uso:  python serve.py            (porta 8000)
      python serve.py 8080
"""
import http.server
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


if __name__ == "__main__":
    with http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"Protótipo  ->  http://localhost:{PORT}/")
        print(f"Unity      ->  http://localhost:{PORT}/unity/")
        print("Ctrl+C para parar.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor parado.")
