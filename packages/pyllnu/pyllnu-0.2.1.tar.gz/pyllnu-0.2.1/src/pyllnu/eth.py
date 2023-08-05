"""
Ethernet-related functions.

This file includes ways to pack and unpack ethernet headers,
allows the developer to create raw sockets, and query MAC
addresses.
"""

import ctypes
import socket
import struct
from ipaddress import IPv4Address, IPv6Address, ip_address
from typing import NewType

from src.pyllnu import util
from src.pyllnu.constants import *

ETHHeader = NewType('Header', bytes)


def create_and_bind_socket(iface: str, port: int = 0) -> socket.SocketType:
    """Helper function to create and bind a raw socket.

    Same as `util.create_and_bind_socket`.

    Args:
        iface (str):
            Interface to bind the socket to.
        port (int, optional):
            Port that the socket will use. Ports lower than 2048 need root privileges. Defaults to 0.

    Returns:
        socket.SocketType:
            Bound socket object.
    """
    return util.create_and_bind_socket(iface, port)


def create_raw_socket() -> socket.SocketType:
    """Helper function to create a raw socket.

    Same as `util.create_raw_socket`.

    For more information, refer to the [official documentation](https://docs.python.org/3/library/socket.html).

    Returns:
        socket.SocketType:
            The created socket.
    """
    return util.create_raw_socket()


def mac_str_to_int_list(mac: str) -> list[int]:
    """Translate a MAC address from string into a `list[int]`.

    Args:
        mac (str):
            MAC address to be translated.

    Returns:
        list[int]:
            MAC address in list format.
    """
    return [int(m, 16) for m in mac.split(':')]


def mac_to_byte_array(mac: list[int] | str) -> ctypes.Array:
    """Translate a MAC address from `list[int]` or `str` format into a ctypes array.

    Args:
        mac (list[int] | str):
            MAC address to be translated.

    Returns:
        ctypes.Array:
            ctypes array containing the MAC address.
    """
    if isinstance(mac, str):
        mac = mac_str_to_int_list(mac)
    return (ctypes.c_ubyte * 16)(*mac)


def get_mac_data(iface: str) -> tuple[list[int], str]:
    """Gets our MAC address in string and list format.

    Same as `util.get_mac_data`.

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
    return util.get_mac_data(iface)


def pack_eth_header(src: list[int], dst: list[int], packet_type: int) -> ETHHeader:
    """Creates a byte buffer with an ethernet header packed into it.

    Args:
        src (list[int]):
            Source MAC address.
        dst (list[int]):
            Destination MAC address.
        packet_type (int):
            Packet type. Usually this will be 0x0800 for IPv4 or 0x86DD for IPv6.

    Returns:
        ETHHeader:
            Byte buffer with the packed header.
    """
    return ETHHeader(struct.pack(ETH_HEADER_FMT, *dst, *src, packet_type))


def unpack_eth_header(buf: bytes) -> tuple[str, str, int]:
    """Unpacks an ethernet header from a buffer.

    Args:
        buf (bytes): Data buffer

    Returns:
        tuple[str, str, int]:
            str:
                Source MAC address.
            str:
                Destination MAC address.
            int:
                Packet type.
    """
    if len(buf) > 14:
        buf = ETHHeader(buf[:14])
    data = struct.unpack(ETH_HEADER_FMT, buf)
    dst = ':'.join(f'{hex(b)[2:].upper():>02}' for b in data[:6])
    src = ':'.join(f'{hex(b)[2:].upper():>02}' for b in data[6:12])
    packet_type = int(data[12:14][0])
    return src, dst, packet_type


def get_default_gateway_mac(gateway: IPv4Address | IPv6Address) -> str:
    """Get the MAC address for the specified gateway.

    Args:
        gateway (IPv4Address | IPv6Address):
            The local gateway's IP.

    Raises:
        ValueError:
            Couldn't find the MAC address for the specified gateway.

    Returns:
        str:
            A MAC address for the specified gateway.
    """
    with open('/proc/net/arp') as f:
        f.readline()
        for line in f:
            fields = line.split()
            try:
                if ip_address(fields[0]) == gateway:
                    return fields[3]
            except ValueError:
                continue
    raise ValueError('Could not get MAC for desired gateway')
