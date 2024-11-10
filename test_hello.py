from hello import hello


def test_default():
    hello("Sheu") == "hello, Sheu"


def test_argument():
    assert hello("Sheu") == "hello, Sheu"