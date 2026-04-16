import pytest
from app import app


# Test 1: Header is present
def test_header(dash_duo):
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert "PINK MORSEL SALES DASHBOARD" in header.text


# Test 2: Graph is present
def test_graph(dash_duo):
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-graph")
    assert graph is not None


# Test 3: Region filter is present
def test_region_picker(dash_duo):
    dash_duo.start_server(app)

    radio = dash_duo.find_element("#region-filter")
    assert radio is not None