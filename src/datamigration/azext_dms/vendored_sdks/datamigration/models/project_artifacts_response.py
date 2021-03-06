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


class ProjectArtifactsResponse(Model):
    """Project artifacts properties.

    :param artifacts_location: An URL that points to the drop location to
     access project artifacts. When accessing this URL, requestor should
     provide an Authorization header with the Bearer authorization scheme,
     followed by his ARM JWT signature. Typical JWT will look like three
     dot-separated base64 encoded strings. We use last string as a shared
     secret between client and our artifacts service.
    :type artifacts_location: str
    """

    _attribute_map = {
        'artifacts_location': {'key': 'artifactsLocation', 'type': 'str'},
    }

    def __init__(self, artifacts_location=None):
        super(ProjectArtifactsResponse, self).__init__()
        self.artifacts_location = artifacts_location
