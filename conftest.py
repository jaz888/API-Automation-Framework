import pytest
from api import product_api
from datetime import datetime
import pytest
from api.base_api import last_request, last_response


@pytest.fixture
def created_product():

    product = {
        "ProductName": "Fixture Phone",
        "Category": "Mobile",
        "Brand": "Apple",
        "Price": 1200,
        "Stock": 10,
        "Status": "Available"

    }

    product_data = product_api.create_product(product)
    yield product_data.json()

    product_api.delete_product(product_data.json()["ProductID"])


def pytest_configure(config):
    if hasattr(config, "_metadata"):
        config._metadata["Project"] = "Automation Framework"
        config._metadata["Tester"] = "Jaz"
        config._metadata["API"] = "Products API"



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        
        extra = ""
        extra += f"\n\nLast Request:\nMethod: {last_request.get('method')}\nURL: {last_request.get('url')}\nBody: {last_request.get('body')}"
        extra += f"\n\nLast Response:\nStatus Code: {last_response.get('status_code')}\nBody: {last_response.get('body')}"


        
      

    

     