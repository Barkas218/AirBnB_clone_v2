#!/usr/bin/python3
from fabric.api import local
from datatime import datatime

def do_pack():
    	""" Creats a trgz archive """
	file_name = "{}_{}{}{}{}{}{}.tgz".format("web_static", time.year,
						time.month, time.day,
						time.hour, time.minute,
						time.second)
	local("mkdir -p versions")
	local("tar -czvf versions/{} {}".format(file_name, "web_static")
