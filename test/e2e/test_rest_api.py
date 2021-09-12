import time,subprocess,requests

proc = subprocess.Popen(['app.cmd'])
time.sleep(5)

def test_rest_api():
    r = requests.get(
        'http://localhost:8098/v1/productdetails?name=%25biscuit%25',
        auth=('andrew.gordon','P@ssw0rd!')
    )
    assert r.status_code == 200
    proc.terminate()