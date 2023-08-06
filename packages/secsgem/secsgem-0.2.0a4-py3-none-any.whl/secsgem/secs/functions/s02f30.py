#####################################################################
# s02f30.py
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
"""Class for stream 02 function 30."""

from secsgem.secs.functions.base import SecsStreamFunction
from secsgem.secs.data_items import ECID
from secsgem.secs.data_items import ECNAME
from secsgem.secs.data_items import ECMIN
from secsgem.secs.data_items import ECMAX
from secsgem.secs.data_items import ECDEF
from secsgem.secs.data_items import UNITS


class SecsS02F30(SecsStreamFunction):
    """
    equipment constant namelist.

    **Data Items**

    - :class:`ECID <secsgem.secs.data_items.ECID>`
    - :class:`ECNAME <secsgem.secs.data_items.ECNAME>`
    - :class:`ECMIN <secsgem.secs.data_items.ECMIN>`
    - :class:`ECMAX <secsgem.secs.data_items.ECMAX>`
    - :class:`ECDEF <secsgem.secs.data_items.ECDEF>`
    - :class:`UNITS <secsgem.secs.data_items.UNITS>`

    **Structure**::

        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS02F30
        [
            {
                ECID: U1/U2/U4/U8/I1/I2/I4/I8/A
                ECNAME: A
                ECMIN: BOOLEAN/I8/I1/I2/I4/F8/F4/U8/U1/U2/U4/A/B
                ECMAX: BOOLEAN/I8/I1/I2/I4/F8/F4/U8/U1/U2/U4/A/B
                ECDEF: BOOLEAN/I8/I1/I2/I4/F8/F4/U8/U1/U2/U4/A/B
                UNITS: A
            }
            ...
        ]

    **Example**::

        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS02F30([
        ...     {"ECID": 1,
        ...       "ECNAME": "EC1",
        ...       "ECMIN": secsgem.secs.variables.U1(0),
        ...       "ECMAX": secsgem.secs.variables.U1(100),
        ...       "ECDEF": secsgem.secs.variables.U1(50),
        ...       "UNITS": "mm"},
        ...     {"ECID": 1337,
        ...       "ECNAME": "EC2",
        ...       "ECMIN": "",
        ...       "ECMAX": "",
        ...       "ECDEF": "",
        ...       "UNITS": ""}])
        S2F30
          <L [2]
            <L [6]
              <U1 1 >
              <A "EC1">
              <U1 0 >
              <U1 100 >
              <U1 50 >
              <A "mm">
            >
            <L [6]
              <U2 1337 >
              <A "EC2">
              <A>
              <A>
              <A>
              <A>
            >
          > .

    :param value: parameters for this function (see example)
    :type value: list
    """

    _stream = 2
    _function = 30

    _data_format = [
        [
            ECID,
            ECNAME,
            ECMIN,
            ECMAX,
            ECDEF,
            UNITS
        ]
    ]

    _to_host = True
    _to_equipment = False

    _has_reply = False
    _is_reply_required = False

    _is_multi_block = True
