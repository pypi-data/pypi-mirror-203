__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

from typing import NamedTuple

class StationInfo(NamedTuple):
    mac: str
    inactive_time: int
    rx_bytes: int
    rx_packets: int
    rx_drop_misc: int
    rx_bitrate: int
    tx_bytes: int
    tx_packets: int
    tx_retries: int
    tx_failed: int
    tx_bitrate: int
    signal: int
    signal_avg: int
    exp_throughput: int
    count_authorized: int
    count_authenticated: int
    count_associated: int
    wmm: int
    mfp: int
    tdls_peer: str
    dtim_period: str
    beacon_interval: float
    preamble: int
    short_preamble: int
    short_slot_time: int
    connected_time: int
