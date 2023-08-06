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

class Confirm:
    def __init__(self, window=None):
        """
        Confirm dialog controller

        :param window: main window object
        """
        self.window = window

    def accept(self, type, id):
        """
        Confirm dialog accept

        :param type: dialog type
        :param id: dialog object id
        """
        if type == 'preset_exists':
            self.window.controller.presets.save(True)
        elif type == 'preset_delete':
            self.window.controller.presets.delete(id, True)
        elif type == 'preset_clear':
            self.window.controller.presets.clear(True)
        elif type == 'ctx_delete':
            self.window.controller.context.delete(id, True)
        elif type == 'ctx_delete_all':
            self.window.controller.context.delete_history(True)
        elif type == 'img_delete':
            self.window.controller.image.img_action_delete(id, True)

        self.window.dialog['confirm'].close()

    def dismiss(self, type, id):
        """
        Confirm dialog dismiss

        :param type: dialog type
        :param id: dialog object id
        """
        self.window.dialog['confirm'].close()
