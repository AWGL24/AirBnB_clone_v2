#!/usr/bin/python3
''' Module holds a Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers,
using the function deploy '''

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

env.hosts = ["34.139.253.47", "107.21.145.67"]


def do_pack():
    ''' do_pack function '''
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        fname = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(fname))
        return fname
    except None:
        return None


def do_deploy(archive_path):
    ''' do_deploy function '''
    if exists(archive_path) is False:
        return False
    try:
        file = archive_path.split("/")[-1]
        no_ext = file.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file, path, no_ext))
        run('rm /tmp/{}'.format(file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False


def deploy():
    ''' deploy function '''
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
