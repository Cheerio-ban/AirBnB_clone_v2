#!/usr/bin/python3

"""
A python fabric script that generates an archive
from the web static folder using targz
"""

from os import path
from datetime import date
from fabric.api import local


def do_pack():
    """
    Embeds the content of the web static directory into
    an archive created by tgz.
    """
    date = datetime.now()
    archive_dir = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            date.year, date.month, date.day, day.hour, date.minute
            date.second)
    if not path.isdir("versions"):
        if local("mkdir versions").failed:
            return None
    crt_archive = "tar -czvf {} web_static".format(archive_dir)
    if local(crt_archive).succeeded:
        return archive_dir
    return None
