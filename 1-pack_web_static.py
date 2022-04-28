#!/usr/bin/python3
''' Module holds a fabric script that generates a
.tgz archive from the contents of the web_static folder '''

from datetime import datetime
from fabric.api import local
from os.path import isdir


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
