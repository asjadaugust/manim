#!/usr/bin/env python3
from __future__ import annotations

import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler, test  # type: ignore


class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()


if __name__ == "__main__":
    test(
        CORSRequestHandler,
        HTTPServer,
        port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000,
    )
