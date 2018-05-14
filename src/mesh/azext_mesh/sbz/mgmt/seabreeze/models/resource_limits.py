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


class ResourceLimits(Model):
    """This type describes the resource limits for a given container. It describes
    the most amount of resources a container is allowed to use before being
    restarted.

    :param memory_in_gb: The memory limit in GB.
    :type memory_in_gb: float
    :param cpu: CPU limits in cores. At present, only full cores are
     supported.
    :type cpu: float
    """

    _attribute_map = {
        'memory_in_gb': {'key': 'memoryInGB', 'type': 'float'},
        'cpu': {'key': 'cpu', 'type': 'float'},
    }

    def __init__(self, memory_in_gb=None, cpu=None):
        self.memory_in_gb = memory_in_gb
        self.cpu = cpu
