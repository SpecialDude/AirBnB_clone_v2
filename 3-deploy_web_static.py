#!/usr/bin/python3

"""
This Fabric script generates an archive
from the contents of web static from the
AirBnB_Clone_v2 project
"""


from fabric.api import local, put, run, env
from datetime import datetime
import os


env.hosts = ['35.168.8.57', '3.84.222.106']


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


def do_deploy(archive_path):
    """deploys the web_static archives to the servers"""

    if not os.path.exists(archive_path):
        return False
    try:
        f_name = archive_path.split("/")[-1]
        f_no_ext = f_name.split(".")[0]
        path = "/data/web_static/releases/"

        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, f_no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(f_name, path, f_no_ext))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, f_no_ext))
        run('rm -rf {}{}/web_static'.format(path, f_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, f_no_ext))
        return True
    except Exception:
        return False


def deploy():
    """This function uploads the archive to the servers"""

    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
