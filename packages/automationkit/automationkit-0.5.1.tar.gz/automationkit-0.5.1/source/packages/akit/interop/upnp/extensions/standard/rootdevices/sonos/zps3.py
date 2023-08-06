"""
.. module:: akit.interop.upnp.extensions.sonos.zps3
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the a Upnp device for a Sonos Zps3.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>

"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

from akit.extensible import LoadableExtension

from akit.interop.upnp.extensions.standard.rootdevices.sonos.sonosplayer import SonosPlayer
from akit.interop.upnp.devices.upnprootdevice import UpnpRootDevice

class SonosDeviceZpS3(SonosPlayer, LoadableExtension):
    """
    """

    MANUFACTURER = "Sonos, Inc."
    MODEL_NUMBER = "S3"
    MODEL_DESCRIPTION = "Sonos Play:3"
