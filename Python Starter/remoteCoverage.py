import io
import sys
from contextlib import redirect_stdout, suppress

import coverage
from fastapi import FastAPI, Response

_cov = coverage.Coverage()


def is_debugging() -> bool:
    with suppress(AttributeError):
        return sys.gettrace()


def start_coverage_tracking():
    if is_debugging():
        print("Running in debug mode. Turning coverage tracking off")
        return
    print(
        "Running in coverage mode. Make a request to /coverage to receive a coverage report"
    )
    _cov.start()


def start_coverage_server(app: FastAPI):
    @app.get("/coverage")
    async def coverageRoute():
        f = io.StringIO()
        with redirect_stdout(f):
            # "-" outfile redirects to stdout
            _cov.xml_report(outfile="-")
        xml_coverage_report = f.getvalue()
        return Response(content=xml_coverage_report, media_type="application/xml")

    # .. call your code ..
    # cov.stop()
    # cov.save()
    # cov.html_report()
# TO START
# if is_local():
#     start_coverage_tracking()
# if is_local():
#     start_coverage_server(app)