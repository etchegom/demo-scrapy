from scraper import utils


def test_hash_value():
    assert (
        utils.hash_value(u"https://www.thomann.de")
        == "e5c91d508789b1d48bafaaedd3e966c7"
    )
