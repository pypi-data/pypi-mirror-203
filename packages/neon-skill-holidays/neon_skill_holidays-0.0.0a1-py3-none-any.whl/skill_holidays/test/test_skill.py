# NEON AI (TM) SOFTWARE, Software Development Kit & Application Framework
# All trademark and other rights reserved by their respective owners
# Copyright 2008-2022 Neongecko.com Inc.
# Contributors: Daniel McKnight, Guy Daniels, Elon Gasper, Richard Leeds,
# Regina Bloomstine, Casimiro Ferreira, Andrii Pernatii, Kirill Hrymailo
# BSD-3 License
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from this
#    software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS  BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS;  OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE,  EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import shutil
import unittest
import pytest

from os import mkdir
from os.path import dirname, join, exists
from mock import Mock
from mycroft_bus_client import Message
from ovos_utils.messagebus import FakeBus
from datetime import datetime

from mycroft.skills.skill_loader import SkillLoader

from lingua_franca import load_language
load_language("en-us")


class TestSkill(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        bus = FakeBus()
        bus.run_in_thread()
        skill_loader = SkillLoader(bus, dirname(dirname(__file__)))
        skill_loader.load()
        cls.skill = skill_loader.instance

        # Define a directory to use for testing
        cls.test_fs = join(dirname(__file__), "skill_fs")
        if not exists(cls.test_fs):
            mkdir(cls.test_fs)

        # Override the configuration and fs paths to use the test directory
        cls.skill.settings_write_path = cls.test_fs
        cls.skill.file_system.path = cls.test_fs
        cls.skill._init_settings()
        cls.skill.initialize()

        # Override speak and speak_dialog to test passed arguments
        cls.skill.speak = Mock()
        cls.skill.speak_dialog = Mock()

    def setUp(self):
        self.skill.speak.reset_mock()
        self.skill.speak_dialog.reset_mock()

    @classmethod
    def tearDownClass(cls) -> None:
        shutil.rmtree(cls.test_fs)

    def test_00_skill_init(self):
        self.assertIsInstance(self.skill.nager_url, str)
        self.assertIsInstance(self.skill.default_locale, str)
        self.assertIsInstance(self.skill.holidays, dict)

    def test_update_holidays(self):
        self.skill._update_holidays("US")
        self.assertIsInstance(self.skill.holidays["US"], list)

    def test_holidays_by_date(self):
        this_year = datetime.now().year
        if datetime.now() > datetime.now().replace(month=12, day=25):
            this_year += 1
        christmas = self.skill.holidays_by_date("US")[f"{this_year}-12-25"]
        self.assertIsInstance(christmas, dict)
        self.assertEqual(christmas['name'], "Christmas Day")

        # TODO: Test other locales

    def test_holidays_by_name(self):
        juneteenth = self.skill.holidays_by_name("US")["juneteenth"]
        self.assertIsInstance(juneteenth, dict)
        self.assertEqual(juneteenth['name'], "Juneteenth")

    def test_cache_holidays(self):
        # TODO
        pass

    def test_format_response(self):
        real_render = self.skill.dialog_renderer.render
        self.skill.dialog_renderer.render = Mock()
        test_holiday = self.skill.holidays["US"][0]
        holiday_name = test_holiday['name']
        self.skill._format_response(test_holiday)
        self.skill.dialog_renderer.render.assert_called_once()
        call = self.skill.dialog_renderer.render.call_args[0]
        self.assertEqual(call[0], "holiday_date")
        self.assertEqual(call[1]["holiday"], holiday_name)
        self.assertIsInstance(call[1]["date"], str)

        self.skill.dialog_renderer.render = real_render

    def test_handle_holiday_on_date(self):
        from lingua_franca.parse import extract_datetime
        from lingua_franca.format import nice_date
        real_format = self.skill._format_response
        self.skill._format_response = Mock(return_value="test")

        valid_test_message = Message("test", {"date": "january first"})
        invalid_test_message = Message("test", {"date": "january 2"})

        # Test valid request
        self.skill.handle_holiday_on_date(valid_test_message)
        self.skill._format_response.assert_called_once()
        self.skill.speak.assert_called_once_with("test")

        # Test no holiday
        self.skill.handle_holiday_on_date(invalid_test_message)
        self.skill.speak_dialog.assert_called_once_with(
            "no_holiday_on_date",
            {"date": nice_date(extract_datetime("january 2")[0])})

        self.skill._format_response = real_format


if __name__ == '__main__':
    pytest.main()
