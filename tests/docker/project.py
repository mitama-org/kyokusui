#!/usr/bin/python

import os

from mitama.project import Project, include
from mitama.db import DatabaseManager

project_dir = os.path.dirname(os.path.abspath(__file__))

DatabaseManager({
    "type":"mysql",
    "host":"mysql",
    "name":"mitama",
    "user":"mitama",
    "password":"mitama",
})

project = Project(
    include("mitama.portal", path="/"),
    include("kyokusui", path="/kyokusui"),
    project_dir = project_dir
)
application = project.wsgi


if __name__ == "__main__":
    project.command()
