#####################################################################
# s14f01.py
#
# (c) Copyright 2021, Benjamin Parzella. All rights reserved.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#####################################################################
"""Class for stream 14 function 01."""

from secsgem.secs.functions.base import SecsStreamFunction
from secsgem.secs.data_items import OBJSPEC
from secsgem.secs.data_items import OBJTYPE
from secsgem.secs.data_items import OBJID
from secsgem.secs.data_items import ATTRID
from secsgem.secs.data_items import ATTRDATA
from secsgem.secs.data_items import ATTRRELN


class SecsS14F01(SecsStreamFunction):
    """
    GetAttr request.

    **Data Items**

    - :class:`OBJSPEC <secsgem.secs.data_items.OBJSPEC>`
    - :class:`OBJTYPE <secsgem.secs.data_items.OBJTYPE>`
    - :class:`OBJID <secsgem.secs.data_items.OBJID>`
    - :class:`ATTRID <secsgem.secs.data_items.ATTRID>`
    - :class:`ATTRDATA <secsgem.secs.data_items.ATTRDATA>`
    - :class:`ATTRRELN <secsgem.secs.data_items.ATTRRELN>`

    **Structure**::

        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS14F01
        {
            OBJSPEC: A
            OBJTYPE: U1/U2/U4/U8/A
            OBJID: [
                DATA: U1/U2/U4/U8/A
                ...
            ]
            FILTER: [
                {
                    ATTRID: U1/U2/U4/U8/A
                    ATTRDATA: L/BOOLEAN/U1/U2/U4/U8/I1/I2/I4/I8/F4/F8/A/B
                    ATTRRELN: U1
                }
                ...
            ]
            ATTRID: [
                DATA: U1/U2/U4/U8/A
                ...
            ]
        }

    **Example**::

        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS14F01({
        ...     "OBJSPEC": '',
        ...     "OBJTYPE": 'StripMap',
        ...     "OBJID": ['MAP001'],
        ...     "FILTER": [],
        ...     "ATTRID": ['OriginLocation', 'Rows', 'Columns', 'CellStatus', 'LotID']})
        S14F1 W
          <L [5]
            <A>
            <A "StripMap">
            <L [1]
              <A "MAP001">
            >
            <L>
            <L [5]
              <A "OriginLocation">
              <A "Rows">
              <A "Columns">
              <A "CellStatus">
              <A "LotID">
            >
          > .

    :param value: parameters for this function (see example)
    :type value: dict
    """

    _stream = 14
    _function = 1

    _data_format = [
        OBJSPEC,
        OBJTYPE,
        [OBJID],
        [
            [
                "FILTER",
                ATTRID,
                ATTRDATA,
                ATTRRELN
            ]
        ],
        [ATTRID]
    ]

    _to_host = True
    _to_equipment = True

    _has_reply = True
    _is_reply_required = True

    _is_multi_block = False
