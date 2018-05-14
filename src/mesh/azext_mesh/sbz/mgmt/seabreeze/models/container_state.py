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


class ContainerState(Model):
    """The container state.

    :param state: The state of this container
    :type state: str
    :param start_time: Date/time when the container state started.
    :type start_time: datetime
    :param exit_code: The container exit code.
    :type exit_code: str
    :param finish_time: Date/time when the container state finished.
    :type finish_time: datetime
    :param detail_status: Human-readable status of this state.
    :type detail_status: str
    """

    _attribute_map = {
        'state': {'key': 'state', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'exit_code': {'key': 'exitCode', 'type': 'str'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'detail_status': {'key': 'detailStatus', 'type': 'str'},
    }

    def __init__(self, state=None, start_time=None, exit_code=None, finish_time=None, detail_status=None):
        self.state = state
        self.start_time = start_time
        self.exit_code = exit_code
        self.finish_time = finish_time
        self.detail_status = detail_status
