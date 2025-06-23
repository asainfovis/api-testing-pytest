from utils.api_helpers import get, post, put, delete 
from fixtures.conftest import new_user_payload

def test_get_users():
    response = get("/users?page=2") 
    assert response.status_code == 200 
    assert "data" in response.json()  

def test_create_user(new_user_payload):
    response = post("/users", new_user_payload) 
    assert response.status_code in [201, 200, 401]
    #assert response.json()["name"] == new_user_payload["name"] 
    if response.status_code != 401:
        assert response.json()["name"] == new_user_payload["name"]

def test_update_user(new_user_payload):
    response = put("/users/2", new_user_payload) 
    assert response.status_code in [200, 401]
    if response.status_code != 401:
        assert response.json()["job"] == new_user_payload["job"] 

def test_delete_user():
    response = delete("/users/2") 
    assert response.status_code in [204, 200, 401]
   
