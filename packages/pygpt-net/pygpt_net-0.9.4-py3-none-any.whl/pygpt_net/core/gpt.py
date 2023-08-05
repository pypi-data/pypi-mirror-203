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

import openai

from .tokens import num_tokens_prompt, num_tokens_extra
from .context import Context, ContextItem
from .history import History


class Gpt:
    def __init__(self, config):
        """
        GPT Wrapper

        :param config: Config object
        """
        self.config = config
        self.context = Context(config)
        self.history = History(config)

        self.ai_name = None
        self.user_name = None
        self.system_prompt = None

        if not self.config.initialized:
            self.config.init()

    def init(self):
        """Initializes OpenAI API key"""
        openai.api_key = self.config.data["api_key"]
        openai.organization = self.config.data["organization_key"]

    def completion(self, prompt, max_tokens):
        """
        Calls OpenAI API for completion

        :param prompt: Prompt (user message)
        :param max_tokens: Max output tokens
        :return: Response dict
        """
        # build prompt message
        message = self.build_completion(prompt)

        # prepare stop word if user_name is set
        stop = None
        if self.user_name is not None and self.user_name != '':
            stop = [self.user_name + ':']

        response = openai.Completion.create(
            prompt=message,
            model=self.config.data['model'],
            max_tokens=int(max_tokens),
            temperature=self.config.data['temperature'],
            top_p=self.config.data['top_p'],
            frequency_penalty=self.config.data['frequency_penalty'],
            presence_penalty=self.config.data['presence_penalty'],
            stop=stop,
        )
        return response

    def chat(self, prompt, max_tokens):
        """
        Call OpenAI API for chat

        :param prompt: Prompt (user message)
        :param max_tokens: Max output tokens
        :return: Response dict
        """
        # build chat messages
        messages = self.build_chat_messages(prompt)
        response = openai.ChatCompletion.create(
            messages=messages,
            model=self.config.data['model'],
            max_tokens=int(max_tokens),
            temperature=self.config.data['temperature'],
            top_p=self.config.data['top_p'],
            frequency_penalty=self.config.data['frequency_penalty'],
            presence_penalty=self.config.data['presence_penalty'],
            stop=None,
        )
        return response

    def build_chat_messages(self, prompt):
        """
        Builds chat messages dict

        :param prompt: Prompt
        :return: Messages dict
        """
        messages = []

        model = self.config.data['model']
        used_tokens = self.count_used_tokens(prompt)
        max_tokens = self.config.data['max_total_tokens']

        # append initial (system) message
        if self.system_prompt is not None and self.system_prompt != "":
            messages.append({"role": "system", "content": self.system_prompt})

        # append messages from context (memory)
        if self.config.data['use_context']:
            items = self.context.get_prompt_items(model, used_tokens, max_tokens)
            for item in items:
                # input
                if item.input is not None and item.input != "":
                    messages.append({"role": "user", "content": item.input})

                # output
                if item.output is not None and item.output != "":
                    messages.append({"role": "assistant", "content": item.output})

        # append current prompt
        messages.append({"role": "user", "content": str(prompt)})

        return messages

    def build_completion(self, prompt):
        """
        Builds completion string

        :param prompt: Prompt (current)
        :return: Message string (parsed with context)
        """
        message = ""
        model = self.config.data['model']
        used_tokens = self.count_used_tokens(prompt)
        max_tokens = self.config.data['max_total_tokens']

        if self.system_prompt is not None and self.system_prompt != "":
            message += self.system_prompt

        if self.config.data['use_context']:
            items = self.context.get_prompt_items(model, used_tokens, max_tokens)
            for item in items:
                if item.input_name is not None \
                        and item.output_name is not None \
                        and item.input_name != "" \
                        and item.output_name != "":
                    if item.input is not None and item.input != "":
                        message += "\n" + item.input_name + ": " + item.input
                    if item.output is not None and item.output != "":
                        message += "\n" + item.output_name + ": " + item.output
                else:
                    if item.input is not None and item.input != "":
                        message += "\n" + item.input
                    if item.output is not None and item.output != "":
                        message += "\n" + item.output

        if self.user_name is not None \
                and self.ai_name is not None \
                and self.user_name != "" \
                and self.ai_name != "":
            message += "\n" + self.user_name + ": " + str(prompt)
            message += "\n" + self.ai_name + ":"
        else:
            message += "\n" + str(prompt)

        return message

    def count_used_tokens(self, input_text):
        """
        Counts used tokens

        :param input_text: Input text
        :return: Used tokens
        """
        model = self.config.data['model']
        tokens = 0
        tokens += num_tokens_prompt(self.system_prompt, self.user_name,
                                    model)  # init (system) prompt
        tokens += num_tokens_prompt(input_text, self.user_name, model)  # current input
        tokens += self.config.data['context_threshold']  # context threshold (reserved for next output)
        tokens += num_tokens_extra(model)  # extra tokens (required for output)
        return tokens

    def call(self, prompt, ctx=None):
        """
        Calls OpenAI API

        :param prompt: User input (prompt)
        :param ctx: Context item (memory)
        :return: Context item (memory)
        """
        # prepare max tokens
        model_tokens = self.config.get_model_tokens(self.config.data['model'])
        max_tokens = self.config.data['max_output_tokens']
        if max_tokens > model_tokens:
            max_tokens = model_tokens

        # minimum 1 token is required
        if max_tokens < 1:
            max_tokens = 1

        # store history
        if self.config.data['store_history']:
            self.history.save(prompt)

        # get response
        response = None
        if self.config.data['mode'] == "completion":
            response = self.completion(prompt, max_tokens)
        elif self.config.data['mode'] == "chat":
            response = self.chat(prompt, max_tokens)

        if response is None:
            return None

        # check for errors
        if "error" in response:
            print("Error: " + str(response["error"]))
            return None

        # get output
        output = ""
        if self.config.data['mode'] == "completion":
            output = response["choices"][0]["text"].strip()
        elif self.config.data['mode'] == "chat":
            output = response["choices"][0]["message"]["content"].strip()

        # store context (memory)
        if ctx is None:
            ctx = ContextItem(self.config.data['mode'])
            ctx.set_input(prompt, self.user_name)

        ctx.set_output(output, self.ai_name)
        ctx.set_tokens(response["usage"]["prompt_tokens"], response["usage"]["completion_tokens"])
        self.context.add(ctx)

        # store history
        if self.config.data['store_history']:
            self.history.save(output)

        return ctx

    def clear(self):
        """Clears context (memory)"""
        self.context.clear()
