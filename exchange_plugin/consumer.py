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
Exchange plugin messages consumer
"""

# Library dependencies
from abc import ABC
from typing import Dict, Optional, Union
from modules_metadata.routing import RoutingKey
from modules_metadata.types import ModuleOrigin


class IConsumer(ABC):  # pylint: disable=too-few-public-methods
    """
    Data exchange consumer interface

    @package        FastyBird:ExchangePlugin!
    @module         consumer

    @author         Adam Kadlec <adam.kadlec@fastybird.com>
    """
    def consume(
        self,
        origin: ModuleOrigin,
        routing_key: RoutingKey,
        data: Optional[Dict[str, Union[str, int, float, bool, None]]],
    ) -> None:
        """Consume data received from exchange bus"""
