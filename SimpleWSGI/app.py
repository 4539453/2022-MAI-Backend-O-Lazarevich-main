from collections.abc import Callable, Iterator


def app(environ, start_response):
    path = environ.get("PATH_INFO")
    if path == "/":
        response_body = b"Home Page\n"
    else:
        response_body = b"A new pagen\n"
    status = "200 OK"
    response_headers = [("Content-Length", str(len(response_body)))]
    start_response(status, response_headers)
    yield response_body


class AppClass(object):
    def __init__(
        self,
        environ: dict,
        start_response: Callable[[str, list[tuple[str, str]]], object],
    ) -> None:
        self.environ = environ
        self.start = start_response

    def __iter__(self) -> Iterator[bytes]:
        response_body: bytes = self.get_responce_body()
        status: str = "200 OK"
        response_headers: list[tuple[str, str]] = [
            ("Content-type", "text/plain"),
            ("Content-Length", str(len(response_body))),
        ]

        self.start(status, response_headers)
        yield response_body

    def get_responce_body(self) -> bytes:
        path = self.environ.get("PATH_INFO")
        response_body: bytes
        if path == "/":
            response_body = "Home Page\n".encode("UTF-8")
        else:
            response_body = "A new page\n".encode("UTF-8")
        return response_body
