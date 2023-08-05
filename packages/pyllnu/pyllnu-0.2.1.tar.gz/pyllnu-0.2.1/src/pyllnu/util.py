
import socket
from ctypes import BigEndianStructure, memmove, pointer, sizeof
from ipaddress import ip_address
from typing import Any

try:
    import netifaces
except ModuleNotFoundError:
    pass

from src.pyllnu.constants import *
from src.pyllnu.exceptions import *


def load_cls_from_buffer(_class: BigEndianStructure, buf: bytes):
    """Load data from a buffer as the given class.

    Args:
        _class (BigEndianStructure): Struct to cast into the buffer data
        buf (bytes): Bytes buffer

    Returns:
        BigEndiantStructure: An instance of `_class`
    """
    header = _class()
    memmove(pointer(header), buf, sizeof(header))
    return header


def calc_pseudo_header_checksum(ip_src: str, ip_dst: str, protocol: int, hdr_len: int) -> int:
    """Calculates the checksum of a generic pseudo-header.

    Args:
        ip_src (str): Source IP (IPv4 or IPv6)
        ip_dst (str): Destination IP (IPv4 or IPv6)
        protocol (int): Protocol being used, such as TCP or UDP
        hdr_len (int): Length of the header

    Returns:
        int: Sum of the created pseudo-header
    """
    _ip_src = ip_address(ip_src)
    _ip_dst = ip_address(ip_dst)
    
    _sum_phdr = int(_ip_src) + int(_ip_dst) + protocol + hdr_len
    return _sum_phdr


def calc_buf_checksum(buf: bytes) -> int:
    """Calculate a pseudo-header checksum.

    Args:
        buf (bytes): Header to calculate the checksum.

    Returns:
        int: Header checksum.
    """
    _sum = 0 
    for i in range(0, len(buf), 2):
        a = buf[i]
        try:
            b = buf[i + 1]
        except IndexError:
            break
        _sum += a + (b << 8)
    _sum += _sum >> 16
    _sum = ~_sum & 0xffff
    _sum = socket.htons(_sum)
    return _sum


def eth_packet_type_to_str(packet_id: int) -> ETHPacketType:
    """Try to translate a packet ID into a `ETHPacketType` enum.

    Args:
        packet_id (int): Decoded packet ID.

    Raises:
        TypeError: Unknown packet.

    Returns:
        ETHPacketType: Packet type enum.
    """
    try:
        return ETHPacketType(packet_id)
    except TypeError:
        raise TypeError('Unknown packet')


def get_application_layer_protocol_from_port(port: int) -> str:
    """Try to guess the protocol by its port.

    Args:
        port (int): Packet port whose protocol we want to guess.

    Returns:
        str: Protocol name and its port (e.g. `'SSH (22)'`).
    """
    try:
        return \
            f'{PortToApplicationType(port).name} ({PortToApplicationType(port).value})'
    except ValueError:
        return f'Unknown destination port: {port}'


def get_other_key(dict_keys: dict[str, Any], ignore_key: str = 'next') -> str:
    """Utility function. Gets any other key in a dictionary except `ignore_key`.

    Args:
        dict_keys (dict[str, Any]): Dictionary to filter the keys from.
        ignore_key (str, optional): Key to ignore. Defaults to 'next'.

    Returns:
        str: Name of the other key in the dictionary.
    """
    return list(set(dict_keys.keys()) - {ignore_key})[0]


def get_our_ip_and_net_mask(iface: str) -> tuple[str, str]:
    """Get an interface's IP address and network mask.

    Args:
        iface (str):
            Interface to query.

    Returns:
        tuple[str, str]: 
            str:
                Interface's IP address.
            str:
                Network mask.
    """
    addr_info = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]
    return addr_info['addr'], addr_info['netmask']


def get_mac_data(iface: str) -> tuple[list[int], str]:
    """Gets our MAC address in string and list format.

    Args:
        iface (str):
            Desired interface to search.

    Returns:
        tuple[list[int], str]:
            list[int]:
                MAC address in number format.
            str:
                MAC address in string format, separated by colons.
    """
    src_mac_data = netifaces.ifaddresses(iface)[netifaces.AF_LINK][0]
    src_mac_addr = [int(d, 16) for d in src_mac_data['addr'].split(':')]
    return (src_mac_addr, src_mac_data['addr'].upper())


def create_and_bind_socket(iface: str, port: int = 0) -> socket.SocketType:
    """Helper function to create and bind a raw socket.

    Args:
        iface (str):
            Interface to bind the socket to.
        port (int, optional):
            Port that the socket will use. Ports lower than 2048 need root privileges. Defaults to 0.

    Returns:
        socket.SocketType:
            Bound socket object.
    """
    s = create_raw_socket()
    s.bind((iface, port))
    return s


def create_raw_socket() -> socket.SocketType:
    """Helper function to create a raw socket.

    For more information, refer to the [official documentation](https://docs.python.org/3/library/socket.html).

    Returns:
        socket.SocketType:
            The created socket.
    """
    return socket.socket(
        socket.AF_PACKET,
        socket.SOCK_RAW,
        socket.PACKET_OTHERHOST
    )
