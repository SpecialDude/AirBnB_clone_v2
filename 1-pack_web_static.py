#!/usr/bin/python3

"""
This Fabric script generates an archive
from the contents of web static from the
AirBnB_Clone_v2 project
"""


from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
        This function generates a tar archive
    """

    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not os.path.isdir("versions"):
            local("mkdir versions")
        f_name = "versions/web_static_{}.tgz".format(date)

        local("tar -cvzf {} web_static".format(f_name))

        return f_name
    except Exception:
        return None
