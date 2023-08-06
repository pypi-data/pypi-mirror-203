'''
Copyright (c) 2023 by HIL Group
Author: notmmao@gmail.com
Date: 2023-04-16 15:57:28
LastEditors: notmmao@gmail.com
LastEditTime: 2023-04-16 16:50:19
Description: 

==========  =============  ================
When        Who            What and why
==========  =============  ================

==========  =============  ================
'''

import pydantic_yaml
from typing import Dict, Union, List


class Ecu(pydantic_yaml.YamlModel):
    name: str
    cname: str
    txid: int
    rxid: int
    channel: str
    fd: bool = True
    dids: Dict[str, str] = {}
    echo: Dict[str, Union[List[int], str]] = {}

    def __str__(self) -> str:
        return f'{self.name}-{self.cname} {hex(self.txid)}-{hex(self.rxid)}'
