# -*- coding: utf-8 -*-
# @Time    : 2023/2/9 22:21
# @Author  : Euclid-Jie
# @File    : Get_single_weibo_details.py
import json
import os

import requests
from tqdm import tqdm

from .Get_longTextContent import Get_longTextContent
from ..Utils import Set_header
from ..Utils import MongoClient


class Get_single_weibo_details:
    """
    Usually a single weibo have three import information:
        1: reposts
        https://weibo.com/ajax/statuses/repostTimeline?id=4866288901690071&page=1&moduleID=feed&count=10
        2: comments
        https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4866288901690071&is_show_bulletin=2&is_mix=0&count=10&uid=1310272120
        3: attitudes
        https://weibo.com/ajax/statuses/likeShow?id=4866288901690071&attitude_type=0&attitude_enable=1&page=1&count=10

    Choose one or the other by setting para "method"
        method = ['reposts', 'comments', 'attitudes']
    """

    def __init__(self, method, mblogid):
        """
        :param method: ['reposts', 'comments', 'attitudes'],
        :param mblogid: just like "MrOtA75Fd",
        :return: None
        """
        self.col = None
        self.page = None
        self.data_json = None
        self.item = None
        self.pages = None
        self.mid = None
        self.total_pages = None
        self.singe_weibo_data = None
        self.mblogid = mblogid
        self.method = method

        # init header
        current_dir = os.path.abspath(os.path.dirname(__file__))
        self.header = Set_header(os.path.join(current_dir, 'cookie.txt'))
        # self.singe_weibo_data = Euclidweibo.Get_single_weibo_data(self.mblogid, self.header)
        # self.Get_single_weibo_infos()
        self.col = MongoClient('Weibo', mblogid + '_' + method)

    def Get_single_weibo_infos(self):
        self.total_pages = {
            'reposts_count': self.singe_weibo_data['reposts_count'],
            'comments_count': self.singe_weibo_data['comments_count'],
            'attitudes_count': self.singe_weibo_data['attitudes_count']
        }

        self.mid = self.singe_weibo_data['mid']

    def Get_json_data(self, URL):
        response = requests.get(URL, headers=self.header, timeout=60)  # 使用request获取网页
        html = response.content.decode('utf-8', 'ignore')  # 将网页源码转换格式为html
        data_json = json.loads(html)
        return data_json

    def get_data_json(self):
        data_json = {
            'mblogid': self.item['mblogid'],
            'mid': self.item['id'],
            'time': self.item['created_at'],
            'uid': self.item['user']['id'],
            'nick_name': self.item['user']['screen_name'],
            'attitudes_count': self.item['attitudes_count'],
            'comments_count': self.item['comments_count'],
            'reposts_count': self.item['reposts_count'],
            'text': self.item['text'],
            'text_raw': self.item['text_raw'],
            'mp4_720p_mp4': self.item['page_info']['media_info']['mp4_720p_mp4'],
            'mp4_hd_url': self.item['page_info']['media_info']['mp4_hd_url'],
            'mp4_sd_url': self.item['page_info']['media_info']['mp4_sd_url'],
            'media_info': self.item['page_info']['media_info']
        }
        self.data_json = Get_longTextContent(data_json, self.header)

    def Get_reposts_info(self):
        # total_pages = int(self.total_pages['comments_count'] / 15)
        total_pages = 100
        with tqdm(range(18, total_pages + 1)) as t:
            for self.page in t:
                t.set_description("pages:{}".format(self.page))  # bar's left info
                # URL = 'https://weibo.com/ajax/statuses/repostTimeline?id={}&page={}&moduleID=feed&count=10'. \
                #     format(self.mid, self.pages)
                URL = 'https://weibo.com/ajax/profile/searchblog?uid=2656274875&page={}&feature=0&q=主播说联播'.format(self.page)
                data_json = self.Get_json_data(URL)
                reposts_list = data_json['data']['list']
                for item in reposts_list:
                    self.item = item
                    self.get_data_json()
                    # write to mongoDB
                    self.col.insert_one(self.data_json)
                t.set_postfix({"状态": "已成功写入{}条".format(len(reposts_list))})  # bar's right info

        return data_json

    def Get_comments_info(self):
        pass

    def Get_attitudes_info(self):
        pass

    def main_get(self):
        if self.method == 'reposts':
            self.Get_reposts_info()
        elif self.method == 'comments':
            self.Get_comments_info()
        elif self.method == 'attitudes':
            self.Get_attitudes_info()
        else:
            raise AttributeError('please set correct para method: reposts, comments or attitudes')


if __name__ == '__main__':
    Get_single_weibo_details('reposts', mblogid='MrOtA75Fd').main_get()
