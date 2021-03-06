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


class SupportedExternalDatabaseServiceEntryResponse(object):
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
        'display_name': 'str',
        'databases': 'list[SupportedDatabaseEntryResponse]'
    }

    attribute_map = {
        'name': 'name',
        'display_name': 'displayName',
        'databases': 'databases'
    }

    def __init__(self, name=None, display_name=None, databases=None):
        """
        SupportedExternalDatabaseServiceEntryResponse - a model defined in Swagger
        """

        self._name = None
        self._display_name = None
        self._databases = None

        if name is not None:
          self.name = name
        if display_name is not None:
          self.display_name = display_name
        if databases is not None:
          self.databases = databases

    @property
    def name(self):
        """
        Gets the name of this SupportedExternalDatabaseServiceEntryResponse.
        Name of the service

        :return: The name of this SupportedExternalDatabaseServiceEntryResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SupportedExternalDatabaseServiceEntryResponse.
        Name of the service

        :param name: The name of this SupportedExternalDatabaseServiceEntryResponse.
        :type: str
        """

        self._name = name

    @property
    def display_name(self):
        """
        Gets the display_name of this SupportedExternalDatabaseServiceEntryResponse.
        Display name of the service

        :return: The display_name of this SupportedExternalDatabaseServiceEntryResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SupportedExternalDatabaseServiceEntryResponse.
        Display name of the service

        :param display_name: The display_name of this SupportedExternalDatabaseServiceEntryResponse.
        :type: str
        """

        self._display_name = display_name

    @property
    def databases(self):
        """
        Gets the databases of this SupportedExternalDatabaseServiceEntryResponse.
        Supported database list

        :return: The databases of this SupportedExternalDatabaseServiceEntryResponse.
        :rtype: list[SupportedDatabaseEntryResponse]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """
        Sets the databases of this SupportedExternalDatabaseServiceEntryResponse.
        Supported database list

        :param databases: The databases of this SupportedExternalDatabaseServiceEntryResponse.
        :type: list[SupportedDatabaseEntryResponse]
        """

        self._databases = databases

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
        if not isinstance(other, SupportedExternalDatabaseServiceEntryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
