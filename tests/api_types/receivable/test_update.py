#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from unittest import TestCase

from luckydonaldUtils.logger import logging

from pytgbot.api_types.receivable.updates import Update, Message

__author__ = 'luckydonald'

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logging.add_colored_handler(level=logging.DEBUG)


# end if

class TestUpdate(TestCase):
    def test_1(self):
        data = {
            "update_id": 10000,
        }
        update = Update.from_array(data)
        self.assertEqual(10000, update.update_id)

        self.assertIsNone(update.message, "element should be not set")
        self.assertIsNone(update.callback_query, "element should be not set")
        self.assertIsNone(update.inline_query, "element should be not set")
        self.assertIsNone(update.channel_post, "element should be not set")
        self.assertIsNone(update.chosen_inline_result, "element should be not set")
        self.assertIsNone(update.edited_channel_post, "element should be not set")
        self.assertIsNone(update.poll, "element should be not set")
        self.assertIsNone(update.pre_checkout_query, "element should be not set")
        self.assertIsNone(update.shipping_query, "element should be not set")

        self.assertNotIn("message", update, "__contains__ should be false as well")
        self.assertNotIn("callback_query", update, "__contains__ should be false as well")
        self.assertNotIn("inline_query", update, "__contains__ should be false as well")
        self.assertNotIn("channel_post", update, "__contains__ should be false as well")
        self.assertNotIn("chosen_inline_result", update, "__contains__ should be false as well")
        self.assertNotIn("edited_channel_post", update, "__contains__ should be false as well")
        self.assertNotIn("poll", update, "__contains__ should be false as well")
        self.assertNotIn("pre_checkout_query", update, "__contains__ should be false as well")
        self.assertNotIn("shipping_query", update, "__contains__ should be false as well")
    # end def


class TestMessage(TestCase):
    def test_1(self):
        data = {
                "date": 1441645532,
                "chat": {
                    "last_name": "Test Lastname A",
                    "id": 1111101,
                    "first_name": "Alfred",
                    "username": "TestA"
                },
                "message_id": 1365,
                "from": {
                    "last_name": "Test Lastname B",
                    "id": 1111102,
                    "first_name": "Beate",
                    "username": "TestB"
                },
                "text": "/start"
            }
        msg = Message.from_array(data)
        self.assertEqual(1441645532, msg.date)
