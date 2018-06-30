"""
Write unittest for `http_response_status_code` function in 'response.py' module using own custom parameter from the command line including next steps:

1.Write plugin that contains:
  - additional info to report headers with home work name and your initials (use `pytest_report_header` hook)
  - custom parameter option for `url` (use `pytest_addoption` hook)
2.Load plugin in `conftest.py` module
3.Use `200` http response status code as an acceptance criteria for your test

Prerequisite:
 - Install `requests` package with `pip install requests` from the shell interface
"""

from chapter_three.response import http_response_status_code
