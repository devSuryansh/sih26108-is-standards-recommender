import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__))); os.chdir(os.path.dirname(os.path.dirname(__file__)))
import app as A

def test_led_street_light_top_hit():
    r = A.app.test_client().post("/api/recommend", json={"spec": "LED street light luminaire for roads"}).get_json()
    assert r["results"][0]["title"] == "LED street luminaires"
    assert "led" in r["results"][0]["matched_terms"]

def test_empty_spec_400():
    assert A.app.test_client().post("/api/recommend", json={}).status_code == 400
