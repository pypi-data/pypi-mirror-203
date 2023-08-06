#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Created Date: 2023.04.09 20:00:00                  #
# ================================================== #

import os


class PresetsDebug:
    def __init__(self, window=None):
        """
        Presets debug

        :param window: main window object
        """
        self.window = window
        self.id = 'presets'

    def update(self):
        """Updates debug window."""
        self.window.debugger.begin(self.id)

        # presets
        for key in self.window.config.presets:
            prefix = "[{}] ".format(key)
            preset = self.window.config.presets[key]
            path = os.path.join(self.window.config.path, 'presets', key + '.json')
            self.window.debugger.add(self.id, prefix + 'ID', str(key))
            self.window.debugger.add(self.id, prefix + 'File', str(path))
            self.window.debugger.add(self.id, prefix + 'name', str(preset['name']))
            self.window.debugger.add(self.id, prefix + 'ai_name', str(preset['ai_name']))
            self.window.debugger.add(self.id, prefix + 'user_name', str(preset['user_name']))
            self.window.debugger.add(self.id, prefix + 'prompt', str(preset['prompt']))
            self.window.debugger.add(self.id, prefix + 'chat', str(preset['chat']))
            self.window.debugger.add(self.id, prefix + 'completion', str(preset['completion']))
            self.window.debugger.add(self.id, prefix + 'img', str(preset['img']))
            self.window.debugger.add(self.id, prefix + 'temperature', str(preset['temperature']))

        self.window.debugger.end(self.id)
