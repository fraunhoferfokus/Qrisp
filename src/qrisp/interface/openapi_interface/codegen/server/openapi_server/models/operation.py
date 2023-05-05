# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Operation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, num_qubits=None, num_clbits=None, params=None, definition=None):  # noqa: E501
        """Operation - a model defined in OpenAPI

        :param name: The name of this Operation.  # noqa: E501
        :type name: str
        :param num_qubits: The num_qubits of this Operation.  # noqa: E501
        :type num_qubits: int
        :param num_clbits: The num_clbits of this Operation.  # noqa: E501
        :type num_clbits: int
        :param params: The params of this Operation.  # noqa: E501
        :type params: List[float]
        :param definition: The definition of this Operation.  # noqa: E501
        :type definition: Operation
        """
        self.openapi_types = {
            'name': str,
            'num_qubits': int,
            'num_clbits': int,
            'params': List[float],
            'definition': Operation
        }

        self.attribute_map = {
            'name': 'name',
            'num_qubits': 'num_qubits',
            'num_clbits': 'num_clbits',
            'params': 'params',
            'definition': 'definition'
        }

        self._name = name
        self._num_qubits = num_qubits
        self._num_clbits = num_clbits
        self._params = params
        self._definition = definition

    @classmethod
    def from_dict(cls, dikt) -> 'Operation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Operation of this Operation.  # noqa: E501
        :rtype: Operation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this Operation.


        :return: The name of this Operation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Operation.


        :param name: The name of this Operation.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def num_qubits(self):
        """Gets the num_qubits of this Operation.


        :return: The num_qubits of this Operation.
        :rtype: int
        """
        return self._num_qubits

    @num_qubits.setter
    def num_qubits(self, num_qubits):
        """Sets the num_qubits of this Operation.


        :param num_qubits: The num_qubits of this Operation.
        :type num_qubits: int
        """
        if num_qubits is None:
            raise ValueError("Invalid value for `num_qubits`, must not be `None`")  # noqa: E501

        self._num_qubits = num_qubits

    @property
    def num_clbits(self):
        """Gets the num_clbits of this Operation.


        :return: The num_clbits of this Operation.
        :rtype: int
        """
        return self._num_clbits

    @num_clbits.setter
    def num_clbits(self, num_clbits):
        """Sets the num_clbits of this Operation.


        :param num_clbits: The num_clbits of this Operation.
        :type num_clbits: int
        """
        if num_clbits is None:
            raise ValueError("Invalid value for `num_clbits`, must not be `None`")  # noqa: E501

        self._num_clbits = num_clbits

    @property
    def params(self):
        """Gets the params of this Operation.


        :return: The params of this Operation.
        :rtype: List[float]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this Operation.


        :param params: The params of this Operation.
        :type params: List[float]
        """

        self._params = params

    @property
    def definition(self):
        """Gets the definition of this Operation.


        :return: The definition of this Operation.
        :rtype: Operation
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this Operation.


        :param definition: The definition of this Operation.
        :type definition: Operation
        """

        self._definition = definition