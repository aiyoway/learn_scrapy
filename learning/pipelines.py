# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from learning.mongo import client
from pymongo import errors

db = client.scrapy


class LearningPipeline(object):
    def process_item(self, item, spider):
        db.douban.insert_one({
            'name': item['name'],
            'scores': item['scores'],
            'comment': item['comment'],
            'cover_img': item['cover_img']
        })
        return item


class QiushiPipeline(object):
    def process_item(self, item, spider):
        try:
            db.qiushi.insert_one({
                'unique': item['unique'],
                'author': item['author'],
                'sex': item['sex'],
                'content': item['content'],
                'starts': item['starts'],
                'comments_num': item['comments_num']
            })
        except errors.DuplicateKeyError:
            pass
        return item
