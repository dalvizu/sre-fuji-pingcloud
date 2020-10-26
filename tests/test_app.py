import datetime
from context import App
from context import GitCommit

"""
Example unit tests
"""


def test_app():

    app = App()
    ticket = GitCommit("7bdf804ae1e659a19a499f21a1551f00dbc7f868",
                       "Dan Alvizu <dalvizu@pingidentity.com>",
                       "SSD-101 I made a ticket!",
                       datetime.datetime.now())
    assert True
