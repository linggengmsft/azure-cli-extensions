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


class ContainerInstanceView(Model):
    """Runtime information of a container instance.

    :param restart_count: The number of times the container has been
     restarted.
    :type restart_count: int
    :param current_state: Current container instance state.
    :type current_state: ~azure.seabreeze.models.ContainerState
    :param previous_state: Previous container instance state.
    :type previous_state: ~azure.seabreeze.models.ContainerState
    :param events: The events of this container instance.
    :type events: list[~azure.seabreeze.models.ContainerEvent]
    """

    _attribute_map = {
        'restart_count': {'key': 'restartCount', 'type': 'int'},
        'current_state': {'key': 'currentState', 'type': 'ContainerState'},
        'previous_state': {'key': 'previousState', 'type': 'ContainerState'},
        'events': {'key': 'events', 'type': '[ContainerEvent]'},
    }

    def __init__(self, restart_count=None, current_state=None, previous_state=None, events=None):
        self.restart_count = restart_count
        self.current_state = current_state
        self.previous_state = previous_state
        self.events = events
