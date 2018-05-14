# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Layer4IngressConfig(Model):
    """Describes the layer4 configuration for public connectivity for this
    network.

    :param public_port: Specifies the public port at which the service
     endpoint below needs to be exposed.
    :type public_port: str
    :param application_name: The application name which contains the service
     to be exposed.
    :type application_name: str
    :param service_name: The service whose endpoint needs to be exposed at the
     public port.
    :type service_name: str
    :param endpoint_name: The service endpoint that needs to be exposed.
    :type endpoint_name: str
    """

    _attribute_map = {
        'public_port': {'key': 'publicPort', 'type': 'str'},
        'application_name': {'key': 'applicationName', 'type': 'str'},
        'service_name': {'key': 'serviceName', 'type': 'str'},
        'endpoint_name': {'key': 'endpointName', 'type': 'str'},
    }

    def __init__(self, public_port=None, application_name=None, service_name=None, endpoint_name=None):
        self.public_port = public_port
        self.application_name = application_name
        self.service_name = service_name
        self.endpoint_name = endpoint_name
