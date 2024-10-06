#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7893216255:AAFsYF2OLaVcrJakxo_tTZWXaqwD6YMs9vo")
    API_ID = int(os.environ.get("API_ID", "22188044"))
    API_HASH = os.environ.get("API_HASH", "099e3a1dce52b7677299c3ab8ab3b6ca")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7080075962")
