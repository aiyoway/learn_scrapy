import requests
import json
from pymongo import errors
from learning.mongo import client

db = client.proxy


class Ip(object):
    # url = 'http://lab.crossincode.com/proxy/get/?num=20'

    def get_ips(self):
        ip_list = db.useful_proxy.find()
        return list(ip_list)

    # 静态方法
    @staticmethod
    def remove_ip(ip):
        db.useful_proxy.delete_one({'proxy': ip})
