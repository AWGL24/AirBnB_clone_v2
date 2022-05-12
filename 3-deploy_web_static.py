#!/usr/bin/python3
''' Write a Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers,
using the function deploy '''

import os
from os import path
from os.path import isdir
from time import strftime
from fabric.api import local
from datetime import datetime
from fabric.api import run, put, env


def do_pack():
    """ do_pack function """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        fname = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(fname))
        return fname
    except None:
        return None


env.hosts = ["34.139.253.47", "107.21.145.67"]


def do_deploy(archive_path):
    """ do_deploy function """
    if path.exists(archive_path):
        try:
            put(archive_path, '/tmp/')
            filename = archive_path[9:]
            no_ext = filename[:-4]
            dir_name = '/data/web_static/releases/' + no_ext + '/'
            run('mkdir -p ' + dir_name)
            run('tar -xzf /tmp/' + filename + ' -C ' + dir_name)
            run('rm -f /tmp/' + filename)
            run('mv ' + dir_name + '/web_static/* ' + dir_name)
            run('rm -rf /data/web_static/current')
            run('ln -s ' + dir_name + ' /data/web_static/current')
            print('New version deployed!')
            return True
        except:
            return False
    else:
        return False


def deploy():
    ''' deploy function '''
    archive_path = do_pack()
    if path is None:
        return False
    return do_deploy(archive_path)
