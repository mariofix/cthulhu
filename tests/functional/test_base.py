
def test_root(TestClient):
    resp = TestClient.get("/")
    assert resp.status_code == 200
    assert b'/' in resp.data


def test_root_error(TestClient):
    resp = TestClient.post("/")
    assert resp.status_code not in [200, 201]
    assert b'/' != resp.data
