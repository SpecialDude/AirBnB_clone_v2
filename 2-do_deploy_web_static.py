#!/usr/bin/python3

"""
This scripts deploys the web_static contents
to my nginx servers
"""

import os
from fabric.api import put, run, env


env.hosts = ['35.168.8.57', '3.84.222.106']


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
