#####################################################################
# linktest_req_header.py
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
"""Header for the hsms linktest request."""

from .header import HsmsHeader


class HsmsLinktestReqHeader(HsmsHeader):
    """
    Header for Linktest Request.

    Header for message with SType 5.
    """

    def __init__(self, system):
        """
        Initialize a hsms linktest request.

        :param system: message ID
        :type system: integer

        **Example**::

            >>> import secsgem.hsms
            >>>
            >>> secsgem.hsms.HsmsLinktestReqHeader(2)
            HsmsLinktestReqHeader({session_id:0xffff, stream:00, function:00, p_type:0x00, s_type:0x05, \
system:0x00000002, require_response:False})
        """
        super().__init__(system, 0xFFFF, 0, 0, False, 0x00, 0x05)
