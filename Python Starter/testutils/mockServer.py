# Standard library imports...
import json
import re
import socket
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any, List, Optional, TypedDict

import requests
from attr import dataclass


class MockApi(TypedDict):
    path: str
    response: Optional[Any]


@dataclass
class RecordedRequest:
    path: str
    headers: Any
    body: Optional[str] = None


# TODO: Figure out how to differentiate between gql mocks and rest mocks
def _getMockServerRequestHandler(mocks: List[MockApi]):
    class MockServerRequestHandler(BaseHTTPRequestHandler):
        MOCK_PATTERNS = list(
            map(
                lambda x: {
                    "path_pattern": re.compile(x["path"]),
                    "response": x["response"],
                },
                mocks,
            )
        )

        recorded_request: Any

        def __mockRequests(self):
            for mock_pattern in self.MOCK_PATTERNS:
                if re.search(mock_pattern["path_pattern"], self.path):
                    # Add response status code.
                    self.send_response(requests.codes.ok)

                    # Add response headers.
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.end_headers()

                    # Add response content.
                    response_content = json.dumps(mock_pattern["response"])
                    self.wfile.write(response_content.encode("utf-8"))
                    return

        def do_POST(self):
            content_length = int(
                self.headers["Content-Length"]
            )  # <--- Gets the size of data
            post_data = self.rfile.read(content_length)  # <--- Gets the data itself
            path = str(self.path)
            headers = self.headers
            body = post_data.decode("utf-8")
            self.recorded_request = RecordedRequest(
                path=path, headers=headers, body=body
            )
            self.__mockRequests()

        def do_GET(self):
            path = str(self.path)
            headers = self.headers
            self.recorded_request = RecordedRequest(path=path, headers=headers)
            self.__mockRequests()

    return MockServerRequestHandler


class MockHttpServer(ThreadingHTTPServer):
    requests = []

    def finish_request(self, request, client_address):
        handler = self.RequestHandlerClass(request, client_address, self)
        self.requests.append(handler.recorded_request)


def _get_free_port() -> int:
    s = socket.socket()
    s.bind(("localhost", 0))
    address, port = s.getsockname()
    s.close()
    return port


class MockServer:
    _server: MockHttpServer | None = None
    _handler = None

    def start_mock_server(self, mocks: List[MockApi] = [], port: int = -1) -> int:
        if port == -1:
            port = _get_free_port()

        self._handler = _getMockServerRequestHandler(mocks)
        self._server = MockHttpServer(
            ("localhost", port),
            self._handler,
        )
        server_thread = threading.Thread(target=self._server.serve_forever)
        server_thread.daemon = True
        server_thread.start()

        return port

    def stop(self):
        if self._server == None:
            return
        self._server.shutdown()

    def get_last_request(self):
        requests = self._server.requests
        if len(requests) == 0:
            raise Exception("No requests were made")
        return requests[-1]
