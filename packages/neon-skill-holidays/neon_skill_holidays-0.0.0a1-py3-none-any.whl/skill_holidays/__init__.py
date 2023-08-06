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

import json
import requests

from datetime import datetime
from os.path import join, dirname
from ovos_utils.log import LOG
from lingua_franca.format import nice_date
from lingua_franca.parse import extract_datetime
from ovos_workshop.skills.common_query_skill import CommonQuerySkill, \
    CQSMatchLevel

from mycroft.skills.mycroft_skill.decorators import intent_file_handler


class HolidaySkill(CommonQuerySkill):
    def __init__(self):
        super(HolidaySkill, self).__init__(name="HolidaySkill")
        self.holidays = {}
        self._cache_file = join(dirname(__file__), "holidays.json")

        # Lower base confidence to prevent handling all holiday-related queries
        self.level_confidence[CQSMatchLevel.GENERAL] = 0.3

    @property
    def nager_url(self):
        """
        Get the base URL to use for holiday lookups.
        """
        return self.settings.get('url') or "https://date.nager.at/api/v3"

    @property
    def default_locale(self):
        """
        Get the default locale to use from a user's profile (if available) or
        global configuration.
        """
        return self.location.get('city',
                                 {}).get('state',
                                         {}).get('country',
                                                 {}).get('code') or "US"

    def initialize(self):
        try:
            with open(self._cache_file) as f:
                self.holidays = json.load(f)
        except Exception as e:
            LOG.error(e)

        self._update_holidays()

    def _update_holidays(self, locale: str = None):
        """
        Update holidays for the configured locale. Cached on local filesystem
        for future references.
        """
        locale = locale or self.default_locale

        url = f"{self.nager_url}/NextPublicHolidays/{locale}"
        resp = requests.get(url)
        if resp.ok:
            holidays = resp.json()
            LOG.debug(holidays)
            self.holidays[locale] = holidays
        self._cache_holidays()

    def _cache_holidays(self):
        """
        Write current holidays to disk for future reference
        """
        with open(self._cache_file, 'w+') as f:
            json.dump(self.holidays, f, indent=2)

    def holidays_by_date(self, locale: str = None) -> dict:
        """
        Get a dict of holidays, indexed by date 'YYYY-MM-DD'
        :param locale: locale to query holidays for
        :return: dict of holidays by date
        """
        locale = locale or self.default_locale
        if locale not in self.holidays:
            LOG.info(f"Updating holidays for: {locale}")
            self._update_holidays(locale)

        return {holiday['date']: holiday for holiday in self.holidays[locale]}

    def holidays_by_name(self, locale: str = None) -> dict:
        """
        Get a dict of holidays, indexed by name
        :param locale: locale to query holidays for
        :return: dict of holidays by name
        """
        locale = locale or self.default_locale
        if locale not in self.holidays:
            LOG.info(f"Updating holidays for: {locale}")
            self._update_holidays(locale)

        return {holiday['name'].lower(): holiday
                for holiday in self.holidays[locale]}

    def CQS_match_query_phrase(self, phrase):
        match_level = CQSMatchLevel.GENERAL
        if self.voc_match(phrase, "when"):
            # If we find a holiday, the request probably looks like: when is x
            match_level = CQSMatchLevel.EXACT
        match = None
        holiday_dict = self.holidays_by_name()
        for holiday in holiday_dict.keys():
            if holiday in phrase:
                LOG.debug(f"matched: {holiday} with confidence: {match_level}")
                match = holiday_dict[holiday]
                break
        if not match:
            return None
        resp = self._format_response(match)
        return match['name'], match_level, resp

    @intent_file_handler("holiday_on_date.intent")
    def handle_holiday_on_date(self, message):
        """
        Handle a user request for a holiday on a particular date
        :param message: Message associated with request
        """
        requested_date = message.data['date']
        requested_date = extract_datetime(requested_date)
        if requested_date:
            requested_date = requested_date[0]
        else:
            LOG.warning(f"Holiday request without valid date: {requested_date}")
            return

        formatted_date = requested_date.strftime("%Y-%m-%d")
        matched_holiday = self.holidays_by_date().get(formatted_date)
        if not matched_holiday:
            # TODO: Check other locales
            self.speak_dialog("no_holiday_on_date",
                              {"date": nice_date(requested_date)})
            return
        self.speak(self._format_response(matched_holiday))

    def _format_response(self, holiday: dict) -> str:
        """
        Get a speakable response for the given holiday
        :param holiday: dict holiday from `self.holidays`
        :return: speakable dialog string
        """
        holiday_name = holiday['name']
        year, month, day = holiday['date'].split('-')
        holiday_date = datetime(year=int(year), month=int(month), day=int(day))
        spoken_date = nice_date(holiday_date)
        dialog = self.dialog_renderer.render("holiday_date",
                                             {"holiday": holiday_name,
                                              "date": spoken_date})
        return dialog


def create_skill():
    return HolidaySkill()
