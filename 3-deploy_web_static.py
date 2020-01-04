#!/usr/bin/python3
from fabric.api import local, put, run, env
from datetime import datetime
from os import path


env.hosts = ["35.196.2.249", "35.196.95.206"]


def do_pack():
    """ Creats a trgz archive """
    time = datetime.now()
    file_name = "{}_{}{}{}{}{}{}.tgz".format("web_static", time.year,
                                             time.month, time.day,
                                             time.hour, time.minute,
                                             time.second)
    local("mkdir -p versions")
    local("tar -cavf versions/{} {}".format(file_name, "web_static"))


def do_deploy(archive_path):
    """ DEploys """
    if not path.exists(archive_path):
        return False

    short_name = archive_path[9:-4]
    full_name = archive_path[9:]

    try:
        """ Upload the archive to the /tmp/ directory of the web server"""
        put(archive_path, "/tmp/{}".format(full_name))

        """Uncompress the archive to the folder """
        run("mkdir -p /data/web_static/releases/{}".format(short_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(full_name, short_name))
        run("rm /tmp/{}".format(full_name))
        run("mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/".format(short_name, short_name))

        """ Delete the archive from the web server """
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(short_name))

        run("rm -rf /data/web_static/current")

        """ create symlink """
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(short_name))

        print("New version deployed!")

    except Exception:
        return False


def deploy():
    """ deploy this """

    pack_it = do_pack()

    if not pack_it:
        return False

    return do_deploy(pack_it)
