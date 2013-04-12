from factories.param_factory import ParamFactory
from ovirtsdk.xml import params
from ovirtsdk.infrastructure.errors import RequestError
from ovirtsdk.api import API
import jsonpickle

class Config:
    def __init__(self):
        self.datacenter = ParamFactory().create_datacenter()
        self.cluster    = ParamFactory().create_cluster(datacenter_broker=self.datacenter)
        self.hosts = []
        self.hosts.append(ParamFactory().create_host(self.cluster,"node1","rhevm-sf101-node-a"))
        self.hosts.append(ParamFactory().create_host(self.cluster,"node2","rhevm-sf101-node-b"))

    def to_json(self):
      return jsonpickle.encode(self)

    @classmethod
    def from_json(cls,json):
        return jsonpickle.decode(json)

    @classmethod
    def get_instance(cls,json):
        json = open('config/config.json', 'r').read()
        return Config.from_json(json)


#config = Config()
#print config.to_json()
#
#print Config.from_json(config.to_json()).to_json()
#
#
#json = """
#{
#    "py/object": "__main__.Config",
#    "cluster": {
#        "py/object": "ovirtsdk.xml.params.Cluster",
#        "gluster_service": true,
#        "virt_service": false,
#        "version": {
#            "py/object": "ovirtsdk.xml.params.Version",
#            "major": 3,
#            "minor": 1
#        },
#        "data_center": {
#            "py/object": "ovirtsdk.xml.params.DataCenter"
#        },
#        "link": [],
#        "creation_status": null,
#        "error_handling": null,
#        "cpu": {
#            "py/object": "ovirtsdk.xml.params.CPU",
#            "mode": "CUSTOM",
#            "id": "Intel SandyBridge Family"
#        },
#        "scheduling_policy": null,
#        "name": "mycluster"
#    },
#    "hosts": [
#        {
#            "cluster": {
#                "py/id": 1
#            },
#            "py/object": "ovirtsdk.xml.params.Host",
#            "root_password": "redhat",
#            "address": "rhevm-sf101-node-a",
#            "name": "node1"
#        },
#        {
#            "cluster": {
#                "py/id": 1
#            },
#            "py/object": "ovirtsdk.xml.params.Host",
#            "root_password": "redhat",
#            "address": "rhevm-sf101-node-b",
#            "name": "node2"
#        }
#    ],
#    "datacenter": {
#        "py/object": "ovirtsdk.xml.params.DataCenter",
#        "storage_type": "posixfs",
#        "version": {
#            "py/object": "ovirtsdk.xml.params.Version",
#            "major": 3,
#            "minor": 1,
#            "creation_status": null,
#            "id": null
#        },
#        "name": "mydatacenter"
#    }
#}
#"""
#print "----------"
#print Config.from_json(json).to_json()
##import pdb; pdb.set_trace()
#print "hi"
#print "----------"
#json = open('config/config.json', 'r').read()
#print Config.from_json(json).to_json()
