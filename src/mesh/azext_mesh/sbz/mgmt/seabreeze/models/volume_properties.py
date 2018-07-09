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


class VolumeProperties(Model):
    """This type describes properties of a volume resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param description: User readable description of the volume.
    :type description: str
    :ivar provider: Provider of the volume. Default value: "SFAzureFile" .
    :vartype provider: str
    :param azure_file_parameters: This type describes a volume provided by an
     Azure Files file share.
    :type azure_file_parameters:
     ~azure.seabreeze.models.VolumeProviderParametersAzureFile
    """

    _validation = {
        'provider': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'provider': {'key': 'provider', 'type': 'str'},
        'azure_file_parameters': {'key': 'azureFileParameters', 'type': 'VolumeProviderParametersAzureFile'},
    }

    provider = "SFAzureFile"

    def __init__(self, description=None, azure_file_parameters=None):
        super(VolumeProperties, self).__init__()
        self.description = description
        self.azure_file_parameters = azure_file_parameters
