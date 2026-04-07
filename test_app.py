def test_import():
    from app import app
    assert app is not None

def test_math():
    assert 1 + 1 == 2
