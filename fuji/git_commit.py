import datetime
from dataclasses import dataclass


@dataclass
class GitCommit:
    """
    A domain object representing a git commit message. The intent is
    for another program to provide these values by parsing a git repository. For
    your purposes, you will initialize them in your tests (See test_app.py)
    """

    # Parsed from git commit message - the git commit sha e.g "7bdf804ae1e659a19a499f21a1551f00dbc7f868"
    sha1: str

    # Parsed from git commit message - who created this e.g "Dan Alvizu <dalvizu@pingidentity.com>"
    author: str

    # parsed from the git commit message - the human message of the commit e.g "SSD-101 implement some feature"
    message: str

    # Parsed from git commit message - when this was created
    date: datetime
