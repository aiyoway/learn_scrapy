# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from learning.mongo import db


class LearningPipeline(object):
    def process_item(self, item, spider):
        db.douban.insert_one({
            'name': item['name'],
            'scores': item['scores'],
            'comment': item['comment'],
            'cover_img': item['cover_img']
        })
        return item
