# Copyright (c) 2015 Infortrend Technology, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
"""Infortrend Exception Handler for Development.
It would move to cinder exception on release.
"""

from cinder import exception
from cinder.i18n import _


# Infortrend EonStor DS Driver
class InfortrendAPIException(exception.VolumeBackendAPIException):
    message = _("The wrong parameters were transmitted from "
                "Cinder API: %(err)s")


class InfortrendDriverException(exception.VolumeDriverException):
    message = _("Infortrend cinder driver exception: %(err)s")


class InfortrendCliException(exception.CinderException):
    message = _("Infortrend CLI exception: %(err)s Param: %(param)s "
                "(Return Code: %(rc)s) (Output: %(out)s)")
