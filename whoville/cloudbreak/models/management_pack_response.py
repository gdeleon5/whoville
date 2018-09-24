# coding: utf-8

"""
    Cloudbreak API

    Cloudbreak is a powerful left surf that breaks over a coral reef, a mile off southwest the island of Tavarua, Fiji. Cloudbreak is a cloud agnostic Hadoop as a Service API. Abstracts the provisioning and ease management and monitoring of on-demand clusters. SequenceIQ's Cloudbreak is a RESTful application development platform with the goal of helping developers to build solutions for deploying Hadoop YARN clusters in different environments. Once it is deployed in your favourite servlet container it exposes a REST API allowing to span up Hadoop clusters of arbitary sizes and cloud providers. Provisioning Hadoop has never been easier. Cloudbreak is built on the foundation of cloud providers API (Amazon AWS, Microsoft Azure, Google Cloud Platform, Openstack), Apache Ambari, Docker lightweight containers, Swarm and Consul. For further product documentation follow the link: <a href=\"http://hortonworks.com/apache/cloudbreak/\">http://hortonworks.com/apache/cloudbreak/</a>

    OpenAPI spec version: 2.7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ManagementPackResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'description': 'str',
        'mpack_url': 'str',
        'purge': 'bool',
        'purge_list': 'list[str]',
        'force': 'bool',
        'id': 'int',
        'public': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'mpack_url': 'mpackUrl',
        'purge': 'purge',
        'purge_list': 'purgeList',
        'force': 'force',
        'id': 'id',
        'public': 'public'
    }

    def __init__(self, name=None, description=None, mpack_url=None, purge=False, purge_list=None, force=False, id=None, public=False):
        """
        ManagementPackResponse - a model defined in Swagger
        """

        self._name = None
        self._description = None
        self._mpack_url = None
        self._purge = None
        self._purge_list = None
        self._force = None
        self._id = None
        self._public = None

        self.name = name
        if description is not None:
          self.description = description
        self.mpack_url = mpack_url
        if purge is not None:
          self.purge = purge
        if purge_list is not None:
          self.purge_list = purge_list
        if force is not None:
          self.force = force
        if id is not None:
          self.id = id
        if public is not None:
          self.public = public

    @property
    def name(self):
        """
        Gets the name of this ManagementPackResponse.
        name of the resource

        :return: The name of this ManagementPackResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ManagementPackResponse.
        name of the resource

        :param name: The name of this ManagementPackResponse.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")
        if name is not None and len(name) < 5:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `5`")
        if name is not None and not re.search('(^[a-z][-a-z0-9]*[a-z0-9]$)', name):
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/(^[a-z][-a-z0-9]*[a-z0-9]$)/`")

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this ManagementPackResponse.
        description of the resource

        :return: The description of this ManagementPackResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ManagementPackResponse.
        description of the resource

        :param description: The description of this ManagementPackResponse.
        :type: str
        """
        if description is not None and len(description) > 1000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")

        self._description = description

    @property
    def mpack_url(self):
        """
        Gets the mpack_url of this ManagementPackResponse.
        url of the ambari management pack

        :return: The mpack_url of this ManagementPackResponse.
        :rtype: str
        """
        return self._mpack_url

    @mpack_url.setter
    def mpack_url(self, mpack_url):
        """
        Sets the mpack_url of this ManagementPackResponse.
        url of the ambari management pack

        :param mpack_url: The mpack_url of this ManagementPackResponse.
        :type: str
        """
        if mpack_url is None:
            raise ValueError("Invalid value for `mpack_url`, must not be `None`")
        if mpack_url is not None and not re.search('^http[s]?:\/\/.*', mpack_url):
            raise ValueError("Invalid value for `mpack_url`, must be a follow pattern or equal to `/^http[s]?:\/\/.*/`")

        self._mpack_url = mpack_url

    @property
    def purge(self):
        """
        Gets the purge of this ManagementPackResponse.
        if true, management pack will be installed with '--purge' flag

        :return: The purge of this ManagementPackResponse.
        :rtype: bool
        """
        return self._purge

    @purge.setter
    def purge(self, purge):
        """
        Sets the purge of this ManagementPackResponse.
        if true, management pack will be installed with '--purge' flag

        :param purge: The purge of this ManagementPackResponse.
        :type: bool
        """

        self._purge = purge

    @property
    def purge_list(self):
        """
        Gets the purge_list of this ManagementPackResponse.
        if provided, management pack will be installed with '--purgeList' option with this values

        :return: The purge_list of this ManagementPackResponse.
        :rtype: list[str]
        """
        return self._purge_list

    @purge_list.setter
    def purge_list(self, purge_list):
        """
        Sets the purge_list of this ManagementPackResponse.
        if provided, management pack will be installed with '--purgeList' option with this values

        :param purge_list: The purge_list of this ManagementPackResponse.
        :type: list[str]
        """

        self._purge_list = purge_list

    @property
    def force(self):
        """
        Gets the force of this ManagementPackResponse.
        if true, management pack will be installed with '--force' flag

        :return: The force of this ManagementPackResponse.
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """
        Sets the force of this ManagementPackResponse.
        if true, management pack will be installed with '--force' flag

        :param force: The force of this ManagementPackResponse.
        :type: bool
        """

        self._force = force

    @property
    def id(self):
        """
        Gets the id of this ManagementPackResponse.
        id of the resource

        :return: The id of this ManagementPackResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManagementPackResponse.
        id of the resource

        :param id: The id of this ManagementPackResponse.
        :type: int
        """

        self._id = id

    @property
    def public(self):
        """
        Gets the public of this ManagementPackResponse.
        resource is visible in account

        :return: The public of this ManagementPackResponse.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """
        Sets the public of this ManagementPackResponse.
        resource is visible in account

        :param public: The public of this ManagementPackResponse.
        :type: bool
        """

        self._public = public

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ManagementPackResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other