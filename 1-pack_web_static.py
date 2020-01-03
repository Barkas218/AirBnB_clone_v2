#!/usr/bin/python3
from fabric.api import local
from datetime import datetime

def do_pack():
    """ Creats a trgz archive """
    time = datetime.now()
    file_name = "{}_{}{}{}{}{}{}.tgz".format("web_static", time.year,
                                            time.month, time.day,
                                            time.hour, time.minute,
                                            time.second)
    local("mkdir -p versions")
    local("tar -cavf versions/{} {}".format(file_name, "web_static")
