#!/usr/bin/python3

#     Copyright 2021. FastyBird s.r.o.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

"""
Common module events
"""

# Python base dependencies
import uuid
from typing import List, Optional

# Library libs
from exchange_plugin.events.event import IEvent


class CommonProvidePropertiesDataEvent(IEvent):  # pylint: disable=too-few-public-methods
    """
    Event fired by any module requesting properties data

    @package        FastyBird:ExchangePlugin!
    @module         common

    @author         Adam Kadlec <adam.kadlec@fastybird.com>
    """

    __property_ids: Optional[List[str]] = None

    EVENT_NAME: str = "common.providePropertiesData"

    # -----------------------------------------------------------------------------

    def __init__(
        self,
        property_ids: List[uuid.UUID],
    ) -> None:
        if len(property_ids):
            self.__property_ids = []

            for property_id in property_ids:
                self.__property_ids.append(property_id.__str__())

    # -----------------------------------------------------------------------------

    @property
    def property_ids(self) -> Optional[List[uuid.UUID]]:
        """Properties entities identifiers"""
        if self.__property_ids is None:
            return None

        return list(map(lambda property_id: uuid.UUID(property_id, version=4), self.__property_ids))
