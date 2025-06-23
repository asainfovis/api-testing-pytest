import pytest 

@pytest.fixture 
def new_user_payload():
    return {
        "name": "john",
        "job": "Tester"
    }


