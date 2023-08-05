"""
Exceptions for the PyLLNU package.
"""

class InvalidIPError(Exception):
    """
    Raised when casting to IPAddress fails.
    """
    pass

class DHCPError(Exception):
    """
    Raised when a DHCP error occurrs.
    """
    pass

class GatewayNotFoundError(Exception):
    """
    Raised when a gateway could not be found for the specified interface.
    """
    pass

class UnknownProtocolError(Exception):
    """
    Raised when a packet using an unknown L3 protocol was read.
    """
    pass
