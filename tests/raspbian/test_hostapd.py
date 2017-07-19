import unittest

from netjsonconfig import Raspbian
from netjsonconfig.utils import _TabsMixin


class TestHostapdRenderer(unittest.TestCase, _TabsMixin):

    def test_wpa2_personal(self):
        o = Raspbian({
            "radios": [
                {
                    "name": "radio0",
                    "phy": "phy0",
                    "driver": "mac80211",
                    "protocol": "802.11n",
                    "channel": 3,
                    "channel_width": 20,
                    "tx_power": 3
                },
            ],
            "interfaces": [
                {
                    "name": "wlan0",
                    "type": "wireless",
                    "wireless": {
                        "radio": "radio0",
                        "mode": "access_point",
                        "ssid": "wpa2-personal",
                        "encryption": {
                            "protocol": "wpa2_personal",
                            "cipher": "tkip+ccmp",
                            "key": "passphrase012345"
                        }
                    }
                }
            ]
        })

        expected = '''# config: /etc/hostapd/hostapd.conf

interface=wlan0
driver=nl80211
hw_mode=g
channel=3
ieee80211n=1
ssid=wpa2-personal
auth_algs=1
wpa=2
wpa_key_mgmt=WPA-PSK
wpa_passphrase=passphrase012345
wpa_pairwise=TKIP CCMP
# config: /etc/network/interfaces

auto wlan0
iface wlan0 inet manual

'''
        self.assertEqual(o.render(), expected)

    def test_wpa_personal(self):
        o = Raspbian({
            "radios": [
                {
                    "name": "radio0",
                    "phy": "phy0",
                    "driver": "mac80211",
                    "protocol": "802.11n",
                    "channel": 3,
                    "channel_width": 20,
                    "tx_power": 3
                },
            ],
            "interfaces": [
                {
                    "name": "wlan0",
                    "type": "wireless",
                    "wireless": {
                        "radio": "radio0",
                        "mode": "access_point",
                        "ssid": "wpa-personal",
                        "encryption": {
                            "protocol": "wpa_personal",
                            "cipher": "auto",
                            "key": "passphrase012345"
                        }
                    }
                }
            ]
        })

        expected = '''# config: /etc/hostapd/hostapd.conf

interface=wlan0
driver=nl80211
hw_mode=g
channel=3
ieee80211n=1
ssid=wpa-personal
auth_algs=1
wpa=1
wpa_key_mgmt=WPA-PSK
wpa_passphrase=passphrase012345
# config: /etc/network/interfaces

auto wlan0
iface wlan0 inet manual

'''
        self.assertEqual(o.render(), expected)

    @unittest.skip('Test skipping')
    def test_wep_open(self):
        o = Raspbian({
            "radios": [
                {
                    "name": "radio0",
                    "phy": "phy0",
                    "driver": "mac80211",
                    "protocol": "802.11n",
                    "channel": 3,
                    "channel_width": 20,
                    "tx_power": 3
                },
            ],
            "interfaces": [
                {
                    "name": "wlan0",
                    "type": "wireless",
                    "wireless": {
                        "radio": "radio0",
                        "mode": "access_point",
                        "ssid": "wep",
                        "encryption": {
                            "protocol": "wep_open",
                            "key": "wepkey1234567"
                        }
                    }
                }
            ]
        })

        expected = ''''''
        self.assertEqual(o.render(), expected)

    @unittest.skip('Test skipping')
    def test_wep_shared(self):
        o = Raspbian({
            "radios": [
                {
                    "name": "radio0",
                    "phy": "phy0",
                    "driver": "mac80211",
                    "protocol": "802.11n",
                    "channel": 3,
                    "channel_width": 20,
                    "tx_power": 3
                },
            ],
            "interfaces": [
                {
                    "name": "wlan0",
                    "type": "wireless",
                    "wireless": {
                        "radio": "radio0",
                        "mode": "access_point",
                        "ssid": "wep",
                        "encryption": {
                            "protocol": "wep_shared",
                            "key": "wepkey1234567"
                        }
                    }
                }
            ]
        })

        expected = ''''''
        self.assertEqual(o.render(), expected)

    def test_encryption_disabled(self):
        o = Raspbian({
            "radios": [
                {
                    "name": "radio0",
                    "phy": "phy0",
                    "driver": "mac80211",
                    "protocol": "802.11n",
                    "channel": 3,
                    "channel_width": 20,
                    "tx_power": 3
                },
            ],
            "interfaces": [
                {
                    "name": "wlan0",
                    "type": "wireless",
                    "wireless": {
                        "radio": "radio0",
                        "mode": "access_point",
                        "ssid": "MyNetwork",
                        "encryption": {
                            "disabled": True,
                            "protocol": "wpa2_personal",
                            "cipher": "tkip+ccmp",
                            "key": "passphrase012345"
                        }
                    }
                }
            ]
        })

        expected = '''# config: /etc/hostapd/hostapd.conf

interface=wlan0
driver=nl80211
hw_mode=g
channel=3
ieee80211n=1
ssid=MyNetwork
# config: /etc/network/interfaces

auto wlan0
iface wlan0 inet manual

'''
        self.assertEqual(o.render(), expected)

    def test_no_encryption(self):
        o = Raspbian({
            "radios": [
                {
                    "name": "radio0",
                    "phy": "phy0",
                    "driver": "mac80211",
                    "protocol": "802.11n",
                    "channel": 3,
                    "channel_width": 20,
                    "tx_power": 3
                },
            ],
            "interfaces": [
                {
                    "name": "wlan0",
                    "type": "wireless",
                    "wireless": {
                        "radio": "radio0",
                        "mode": "access_point",
                        "ssid": "open",
                        "encryption": {"protocol": "none"}
                    }
                }
            ]
        })

        expected = '''# config: /etc/hostapd/hostapd.conf

interface=wlan0
driver=nl80211
hw_mode=g
channel=3
ieee80211n=1
ssid=open
# config: /etc/network/interfaces

auto wlan0
iface wlan0 inet manual

'''
        self.assertEqual(o.render(), expected)

    @unittest.skip('Test skipping')
    def test_wps(self):
        o = Raspbian({
            "radios": [
                {
                    "name": "radio0",
                    "phy": "phy0",
                    "driver": "mac80211",
                    "protocol": "802.11n",
                    "channel": 3,
                    "channel_width": 20,
                    "tx_power": 3
                },
            ],
            "interfaces": [
                {
                    "name": "wlan0",
                    "type": "wireless",
                    "wireless": {
                        "radio": "radio0",
                        "mode": "access_point",
                        "ssid": "wps-ssid",
                        "encryption": {
                            "protocol": "wps",
                            "wps_label": False,
                            "wps_pushbutton": True,
                            "wps_pin": ""
                        }
                    }
                }
            ]
        })

        expected = ''''''
        self.assertEqual(o.render(), expected)
