import os, requests as req
def test_reverse():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/demo/reverse"
    res = req.get(url).json()
    1==1