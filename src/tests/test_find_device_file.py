#!/usr/bin/env python3
#
# Copyright (C) 2020 VyOS maintainers and contributors
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 or later as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from unittest import TestCase
from vyos.utils.system import find_device_file
import json

class TestDeviceFile(TestCase):
    """ used to find USB devices on target """
    def setUp(self):
        pass

    def test_null(self):
        self.assertEqual(find_device_file('null'), '/dev/null')

    def test_zero(self):
        self.assertEqual(find_device_file('zero'), '/dev/zero')

    def test_input_event(self):
        self.assertEqual(find_device_file('event0'), '/dev/input/event0')

    def test_non_existing(self):
        self.assertFalse(find_device_file('vyos'))
