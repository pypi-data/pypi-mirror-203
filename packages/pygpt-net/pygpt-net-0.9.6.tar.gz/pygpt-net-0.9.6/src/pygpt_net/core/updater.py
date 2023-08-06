#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2023.04.16 22:00:00                  #
# ================================================== #

from urllib.request import urlopen, Request
from packaging.version import parse as parse_version
import json
import ssl
from .utils import trans


class Updater:
    def __init__(self, window=None):
        """
        Updates handler

        :param window: main window
        """
        self.window = window

    def check(self):
        """Checks for updates"""
        print("Checking for updates...")
        url = self.window.website + "/api/version?v=" + str(self.window.version)
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE

            req = Request(
                url=url,
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            response = urlopen(req, context=ctx, timeout=3)
            data_json = json.loads(response.read())
            newest_version = data_json["version"]
            newest_build = data_json["build"]

            # changelog
            changelog = ""
            if "changelog" in data_json:
                changelog = data_json["changelog"]

            parsed_newest_version = parse_version(newest_version)
            parsed_current_version = parse_version(self.window.version)
            if parsed_newest_version > parsed_current_version:
                self.show_version_dialog(newest_version, newest_build, changelog)
            else:
                print("No updates available")
        except Exception as e:
            print("Failed to check for updates")
            print(e)

    def show_version_dialog(self, version, build, changelog):
        """
        Displays new version dialog

        :param version: version number
        :param build: build date
        :param changelog: changelog
        """
        txt = trans('update.new_version') + ": " + str(version) + " (" + trans('update.released') + ": " + str(
            build) + ")"
        txt += "\n" + trans('update.current_version') + ": " + self.window.version
        self.window.dialog['update'].changelog.setPlainText(changelog)
        self.window.dialog['update'].message.setText(txt)
        self.window.ui.dialogs.open('update')

    def patch(self):
        """Patch config files to current version"""
        try:
            self.patch_config()
            self.patch_models()
            self.patch_presets()
            # TODO: add context patcher
        except Exception as e:
            print("Failed to patch config files!")
            print(e)

    def patch_models(self):
        """Migrates models to current version"""
        data = self.window.config.models
        version = "0.0.0"
        updated = False
        if '__meta__' in data and 'version' in data['__meta__']:
            version = data['__meta__']['version']
        old = parse_version(version)
        current = parse_version(self.window.version)
        if old < current:
            if old < parse_version("0.9.1"):
                # apply meta only (not attached in 0.9.0)
                updated = True

        # update file
        if updated:
            print("Migrated models.json.")
            self.window.config.models = data
            self.window.config.save_models()

    def patch_presets(self):
        """Migrates presets to current version"""
        for k in self.window.config.presets:
            data = self.window.config.presets[k]
            version = "0.0.0"
            updated = False
            if '__meta__' in data and 'version' in data['__meta__']:
                version = data['__meta__']['version']
            old = parse_version(version)
            current = parse_version(self.window.version)
            if old < current:
                if old < parse_version("0.9.1"):
                    pass

            # update file
            if updated:
                print("Migrated presets.")
                self.window.config.presets[k] = data
                self.window.config.save_preset(k)

    def patch_config(self):
        """Migrates config to current version"""
        data = self.window.config.data
        version = "0.0.0"
        updated = False
        if '__meta__' in data and 'version' in data['__meta__']:
            version = data['__meta__']['version']
        old = parse_version(version)
        current = parse_version(self.window.version)
        if old < current:
            if old < parse_version("0.9.6"):
                print("Migrating config from < 0.9.6...")
                data['debug'] = True  # enable debug by default
                updated = True
            if old < parse_version("0.9.4"):
                print("Migrating config from < 0.9.4...")
                if 'plugins' not in data:
                    data['plugins'] = {}
                if 'plugins_enabled' not in data:
                    data['plugins_enabled'] = {}
                updated = True
            if old < parse_version("0.9.2"):
                print("Migrating config from < 0.9.2...")
                keys_to_remove = ['ui.ctx.min_width',
                                  'ui.ctx.max_width',
                                  'ui.toolbox.min_width',
                                  'ui.toolbox.max_width',
                                  'ui.dialog.settings.width',
                                  'ui.dialog.settings.height',
                                  'ui.chatbox.font.color']
                for key in keys_to_remove:
                    if key in data:
                        del data[key]
                if 'theme' not in data:
                    data['theme'] = "dark_teal"
                updated = True

            if old < parse_version("0.9.1"):
                print("Migrating config from < 0.9.1...")
                keys_to_remove = ['user_id', 'custom']  # not needed anymore
                for key in keys_to_remove:
                    if key in data:
                        del data[key]
                keys_to_add = ['organization_key']
                for key in keys_to_add:
                    if key not in data:
                        data[key] = ""
                updated = True

        # update file
        if updated:
            print("Migrated config.json.")
            self.window.config.data = data
            self.window.config.save()
