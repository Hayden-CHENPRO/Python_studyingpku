# !/usr/bin/env python
# -*- Coding:utf-8 -*-
# Created by Hayden at 2019/12/3


import os
import re
import pandas as pd
from datetime import datetime


class DataCleaning():
    def chSub(self, char):
        '''
        字符替换函数
        :param char: 传入的初始字符串
        :return: 替换好的字符串
        '''
        char = char.replace(":", "：").replace(r'\t', '').replace(' ', '').replace('（Vtuber）', '').replace('　', '')
        char = char.replace('.', '').replace('。', '').replace('\\u3000', '').replace('（猴子ver）', '')
        char = char.replace('（少年ver）', '').replace('(幼年)', '').replace('(#01-15)', '').replace('(#31)', '')
        char = char.replace('（Jiena）', '').replace('\\u200e', '').replace('（导演版）', '').replace('（声优版）', '')
        char = char.replace('（乃木坂46）', '').replace('（母亲时代)', '').replace('（第10～14集）', '').replace('\\u200b', '')
        char = char.replace('（加藤奈奈绘）', '').replace('（少年）', '').replace('\\u003E', '').replace('\\u003C', '')
        char = char.replace('BONES・', '').replace('・BONES', '')

        char = re.sub(r'[(]', '（', char)
        char = re.sub(r'[)]', '）', char)
        char = re.sub(r'（.*?）', '', char)
        char = re.sub(r'[（）?？]', '', char)

        char = re.sub(r'《.*?》', '', char)
        char = re.sub(r'『.*?』', '', char)
        char = re.sub(r'「.*?」', '', char)

        char = char.replace('導', '导').replace('監', '监').replace('畫', '画').replace('劃', '划').replace('綱', '纲')
        char = char.replace('宮', '宫').replace('釘', '钉').replace('恵', '惠').replace('樹', '树').replace('藍', '蓝')
        char = char.replace('澤', '泽').replace('戸', '户').replace('貴', '贵').replace('羅', '罗').replace('龍', '龙')
        char = char.replace('々', '奈').replace('愛', '爱').replace('紗', '纱').replace('葉', '叶').replace('遠', '远')
        char = char.replace('気', '气').replace('條', '条').replace('禎', '祯').replace('縄', '绳').replace('島', '岛')
        char = char.replace('綾', '绫').replace('飯', '饭').replace('倫', '伦').replace('曄', '晔').replace('淵', '渊')
        char = char.replace('勝', '胜').replace('渋', '涩').replace('嶺', '岭').replace('舎', '舍').replace('諒', '谅')
        char = char.replace('憂', '夏').replace('勲', '勋').replace('誌', '志').replace('鄭', '郑').replace('維', '维')
        char = char.replace('國', '国').replace('橋', '桥').replace('絵', '绘').replace('駒', '驹').replace('獎', '奖')
        char = char.replace('黒', '黑').replace('鷹', '鹰').replace('見', '见').replace('晉', '晋').replace('貝', '贝')
        char = char.replace('織', '织').replace('斉', '齐').replace('馬', '马').replace('燈', '灯').replace('時', '时')
        char = char.replace('壯', '壮').replace('関', '关').replace('進', '进').replace('場', '场').replace('訓', '训')
        char = char.replace('歩', '步').replace('鈴', '铃').replace('裏', '里').replace('親', '亲').replace('憲', '宪')
        char = char.replace('東', '东').replace('種', '种').replace('圓', '圆').replace('壽', '寿').replace('綠', '绿')
        char = char.replace('誠', '诚').replace('齋', '斋').replace('廣', '广').replace('繩', '绳').replace('倖', '幸')
        char = char.replace('輔', '辅').replace('優', '优').replace('諸', '诸').replace('節', '节').replace('邊', '边')
        char = char.replace('亞', '亚').replace('長', '长').replace('陽', '阳').replace('遙', '遥').replace('銀', '银')
        char = char.replace('倉', '仓').replace('実', '实').replace('間', '间').replace('極', '极').replace('統', '统')
        char = char.replace('雛', '雏').replace('岡', '冈').replace('樫', '㭴').replace('軌', '轨').replace('髙', '高')
        char = char.replace('啓', '启').replace('聡', '聪').replace('賢', '贤').replace('堅', '坚').replace('巻', '卷')
        char = char.replace('達', '达').replace('篤', '笃').replace('栄', '荣').replace('幾', '几').replace('呂', '吕')
        char = char.replace('斎', '斋').replace('細', '细').replace('剛', '刚').replace('豐', '丰').replace('禮', '礼')
        char = char.replace('総', '总').replace('豊', '礼').replace('潤', '润').replace('穀', '谷').replace('儀', '仪')
        char = char.replace('紀', '纪').replace('則', '则').replace('嵐', '岚').replace('陸', '陆').replace('濟', '济')
        char = char.replace('穣', '穰').replace('麗', '丽').replace('済', '济').replace('賀', '贺').replace('關', '关')
        char = char.replace('濱', '滨').replace('紘', '纮').replace('後', '后').replace('納', '纳').replace('氷', '冰')
        char = char.replace('渓', '溪').replace('輝', '辉').replace('義', '义').replace('麥', '麦').replace('鎬', '镐')
        char = char.replace('遊', '游').replace('亜', '亚').replace('緒', '绪').replace('紳', '绅').replace('満', '满')
        char = char.replace('夢', '梦').replace('鷄', '鸡').replace('諏', '诹').replace('邉', '边').replace('紅', '红')
        char = char.replace('訪', '访').replace('風', '风').replace('齊', '齐').replace('峯', '峰').replace('堺', '界')
        char = char.replace('咲', '笑').replace('氣', '气').replace('楓', '枫').replace('陣', '阵').replace('滝', '泷')
        char = char.replace('渕', '渊').replace('瀬', '濑').replace('純', '纯').replace('靜', '静').replace('駿', '骏')
        char = char.replace('鮎', '鲇').replace('裡', '里').replace('脅', '胁').replace('來', '来').replace('聖', '圣')
        char = char.replace('礫', '砾').replace('資', '资').replace('順', '顺').replace('児', '儿').replace('須', '须')
        char = char.replace('郷', '乡').replace('並', '并').replace('寛', '宽').replace('読', '读').replace('頼', '赖')
        char = char.replace('務', '务').replace('奨', '奖').replace('篠', '筱').replace('鎌', '镰').replace('鳴', '鸣')
        char = char.replace('鵜', '鹈').replace('燿', '耀').replace('畠', '町').replace('磯', '矶').replace('頭', '头')
        char = char.replace('興', '与').replace('於', '于').replace('瑠', '琉').replace('範', '范').replace('円', '圆')
        char = char.replace('広', '广').replace('設', '设').replace('楽', '乐').replace('記', '记').replace('脩', '修')
        char = char.replace('﨑', '崎').replace('緑', '绿').replace('眞', '真').replace('墻', '墙').replace('響', '响')
        char = char.replace('辺', '边').replace('嶋', '岛').replace('嵜', '崎').replace('譲', '让').replace('蒼', '苍')
        char = char.replace('慶', '庆').replace('筆', '笔').replace('園', '园').replace('詩', '诗').replace('溝', '沟')
        char = char.replace('稲', '稻').replace('脇', '胁').replace('鳥', '鸟').replace('亀', '龟').replace('華', '华')
        char = char.replace('冨', '富').replace('櫻', '樱').replace('細', '细').replace('詠', '咏').replace('渉', '涉')
        char = char.replace('運', '运').replace('詰', '诘').replace('飛', '飞').replace('貫', '贯').replace('繪', '绘')
        char = char.replace('檜', '桧').replace('樺', '桦').replace('鶴', '鹤').replace('結', '结').replace('規', '规')
        char = char.replace('蘭', '兰').replace('桜', '樱').replace('尋', '寻').replace('鳳', '凤').replace('剣', '剑')
        char = char.replace('塩', '盐').replace('戶', '户').replace('壹', '一').replace('欽', '钦').replace('輪', '轮')
        char = char.replace('宍', '肉').replace('積', '积').replace('環', '环').replace('穂', '穗').replace('蔵', '藏')
        char = char.replace('瀧', '泷').replace('瑤', '瑶').replace('實', '实').replace('師', '师').replace('彌', '边')
        char = char.replace('淺', '浅').replace('彥', '彦').replace('兒', '儿').replace('賓', '宾').replace('颯', '飒')
        char = char.replace('電', '电').replace('隠', '隐').replace('竜', '龙').replace('暁', '晓').replace('軽', '轻')
        char = char.replace('諫', '谏').replace('創', '创').replace('凍', '冻').replace('異', '异').replace('識', '识')
        char = char.replace('亰', '京').replace('喬', '乔').replace('観', '观').replace('鏡', '镜').replace('會', '会')
        char = char.replace('煙', '烟').replace('酔', '醉').replace('衛', '卫').replace('戯', '戏').replace('紡', '纺')
        char = char.replace('論', '论').replace('湯', '汤').replace('欄', '栏').replace('連', '连').replace('載', '载')
        char = char.replace('綴', '缀').replace('雙', '双').replace('鐮', '镰').replace('錯', '错').replace('烏', '乌')
        char = char.replace('鍋', '锅').replace('動', '动')
        return char

    def numtify_with_unit(self, df, col_name):
        df2 = pd.Series([])
        df_inside = df.fillna(0)
        df_inside = df_inside.replace('-', 0)
        for each, i in zip(df_inside[col_name], range(df_inside.shape[0])):
            if each == 0:
                df2[i] = 0
            elif '万' in each:
                df2[i] = float(each[:-1])
            elif '亿' in each:
                df2[i] = float(each[:-1]) * 10000
            else:
                df2[i] = float(each)
        return df2

    def datify(self, df, col_name):
        df2 = pd.Series([])
        for each, i in zip(df[col_name], range(df.shape[0])):
            if '年' in each:
                df2[i] = each.split('月')[0]
                df2[i] = datetime.strptime(df2[i].replace('年', '-'), '%Y-%m')
            else:
                df2[i] = datetime.strptime('0001-01', '%Y-%m')
        return df2

    def numtify_series(self, df, col_name):
        df2 = pd.Series([])
        df_inside = df[col_name].fillna(0)
        for each, i in zip(df_inside, range(df_inside.shape[0])):
            if each == 0:
                df2[i] = 0
            elif '已完结' in each:
                df2[i] = float(each.split('全')[1][:-1])
            else:
                df2[i] = 0
        return df2

    def tag_statistics(self, df, col_name):
        tags_count = {}
        for each in df[col_name]:
            for tag in eval(each):
                if tag == '':
                    continue
                elif tag in tags_count:
                    tags_count[tag] += 1
                else:
                    tags_count[tag] = 1
        return tags_count

    def ch_judge_count(self, ch_list, strs, dicts):
        '''
        用于分割组合人名法函数
        :param ch_list: 用于切分的字符列表
        :param strs: 需要被分割的组合人名，字符串
        :param dicts: 分割好的以及不需要分割的人名最后放入的字典
        :return: 无返回值
        '''
        j = 0
        for ch in ch_list:
            if ch in strs:
                strs_info = strs.split(ch)
                for every in strs_info:
                    if every in dicts:
                        dicts[every] += 1
                    else:
                        dicts[every] = 1
                break
            else:
                j += 1
                continue
        if j == len(ch_list):
            if strs in dicts:
                dicts[strs] += 1
            else:
                dicts[strs] = 1
        return None

    ch_list = ['\\u002F', '、', '／', '+']

    def actor_statistics(self, df, col_name):
        actor_count = {}
        df_inside = df[col_name].fillna('')
        for each in df_inside:    # each是一个超长字符串，包含每部番剧的全声优
            if each == '':
                continue
            else:
                try:
                    each = self.chSub(each)
                    actor_list = each.split('\\n')
                    for peop in actor_list:
                        actor = peop.split('：')[1]    # actor是每一个声优（未分离）
                        self.ch_judge_count(self.ch_list, actor, actor_count)
                except IndexError:
                    continue
        return actor_count

    def staff_statistics(self, df, col_name):
        director_count = {}
        author_count = {}
        df_inside = df[col_name].fillna('')
        for each in df_inside:    # each是一个超长字符串，包含每部番剧的全职员
            if each == '':
                continue
            else:
                try:
                    each = self.chSub(each)
                    staff_list = each.split('\\n')
                    for peop in staff_list:
                        work = peop.split('：')[0]
                        stf = peop.split('：')[1]
                        if work in ['导演', '监督', '总导演', '总监督']:
                            self.ch_judge_count(self.ch_list, stf, director_count)
                        elif work in ['原作', '企划', '企画']:
                            self.ch_judge_count(self.ch_list, stf, author_count)
                        else:
                            continue
                except IndexError:
                    continue
        return director_count, author_count


os.chdir(r'C:\Users\怠惰的金枪小鱼干\Desktop')
df = pd.read_csv('contents_1.csv', names=['番剧名', '播放量', '总评分', '评分人数', '开播时间', '标签',
                                      '弹幕量', '追番数', '剧集数', '会员否', 'actor', 'staff'])
# pd.set_option('display.max_columns',1000)
# pd.set_option('display.width', 1000)
# pd.set_option('display.max_colwidth',1000)
# pd.set_option('display.unicode.ambiguous_as_wide', True)
# pd.set_option('display.unicode.east_asian_width', True)

new_data = DataCleaning()
df_plays = new_data.numtify_with_unit(df, '播放量')
df_barCounts = new_data.numtify_with_unit(df, '弹幕量')
df_follows = new_data.numtify_with_unit(df, '追番数')
df_gradeCounts = df['评分人数'].fillna(0)
df_avg_grade = df['总评分'].fillna(0)
df_release_time = new_data.datify(df, '开播时间')
df_series = new_data.numtify_series(df, '剧集数')   # 统计数据不包含连载中的十月新番
df_tags = new_data.tag_statistics(df, '标签')    # 返回每个标签的统计个数
df_actor = new_data.actor_statistics(df, 'actor')    # 返回一个声优的统计个数字典
df_staff = new_data.staff_statistics(df, 'staff')    # 返回一个职员的统计个数字典

# print(df)
# print(df['播放量'])
# print(df_tags)
# df_actor = actor_statistics(df, 'actor')
# with open('actor_list.txt', 'w', encoding='utf-8') as f:
#     f.write(str(df_actor))
