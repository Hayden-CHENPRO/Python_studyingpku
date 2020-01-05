# !/usr/bin/env python
# -*- Coding:utf-8 -*-
# Created by Hayden at 2019/12/3


import os
import re
import pandas as pd
import numpy as np
from numpy import nan as NA
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from sklearn import linear_model


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
                df2[i] = float(each) / 10000
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
pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

new_data = DataCleaning()
df_plays_unsort = new_data.numtify_with_unit(df, '播放量')
# df_plays = new_data.numtify_with_unit(df, '播放量').sort_values(axis=0, ascending=True)
df_barCounts = new_data.numtify_with_unit(df, '弹幕量')
df_follows = new_data.numtify_with_unit(df, '追番数')
df_gradeCounts = df['评分人数'].fillna(0)
# df_avg_grade = df['总评分'].fillna(0).sort_values(axis=0, ascending=True)
df_avg_grade_unsort = df['总评分'].fillna(0)
# df_release_time = new_data.datify(df, '开播时间')
df_series = new_data.numtify_series(df, '剧集数')   # 统计数据不包含连载中的十月新番
# df_tags = new_data.tag_statistics(df, '标签')    # 返回每个标签的统计个数，字典类型
# df_actor = new_data.actor_statistics(df, 'actor')    # 返回一个声优的统计个数字典
# df_actors = new_data
# df_staff = new_data.staff_statistics(df, 'staff')    # 返回一个由导演和原作两个字典组成的元组


# 单变量分析
def dataTag(*plot_type, plot=None):
    '''
    显示柱形图的数据标签
    :param plot_type: (0)显示的数据类型，数值or百分数；(1)总数sum，用于计算百分数的分母
    :param plot: 绘图对象
    '''
    for each in plot:
        if plot_type[0] == 'num':    # 给纵向条形图显示计数标签
            height = each.get_height()
            plt.text(each.get_x()+each.get_width()/2, height, height, ha='center', va='bottom')    # 柱体的横坐标、宽度、高度属性可分别通过对象的get_x()、get_width()、get_height()方法获得
        elif plot_type[0] == 'percent':    # 给横向条形图添加百分数标签
            perc = '%.2f%%'%(each.get_width() / plot_type[1] * 100)
            plt.text(each.get_width()+5, each.get_y()+0.2, perc)
    return None

def plays_analysis_single(series):
    '''
    播放量单项分析：环形图
    :param series: df_plays
    '''
    sum = series.shape[0]

    labels = '<10', '10~100', '100~1000', '1000~10000', '>10000'
    size_10 = series[(series <= 10)].shape[0] / sum
    size_100 = series[(series > 10) & (series <= 100)].shape[0] / sum
    size_1000 = series[(series > 100) & (series <= 1000)].shape[0] / sum
    size_10000 = series[(series > 1000) & (series <= 10000)].shape[0] / sum
    size_40000 = series[(series > 10000) & (series <= 40000)].shape[0] / sum
    sizes = pd.Series([size_10, size_100, size_1000, size_10000, size_40000]).tolist()
    sizes_0 = [1, 0, 0, 0]

    plt.figure(figsize=(5, 5))    # 设置画布
    plt.title('不同播放量番剧的比例', size=15, family='YouYuan')
    plt.text(1.2, -1.2, '播放量单位：万', size=7, family='YouYuan')
    colors = ['lightpink','lightskyblue','lightsalmon','plum', 'lightgreen']
    explode = [0, 0, 0, 0, 0.1]
    plt.pie(sizes, labels=labels, autopct='%.2f%%', colors=colors, radius=1.0, pctdistance = 0.8, explode=explode)
    plt.pie(sizes_0, radius=0.6, colors = 'w')
    plt.show()
    return None

def grade_analysis_single(series):
    '''
    评分单项分析：纵向条形图
    :param series: df_avg_grade
    '''
    x_label_value = pd.Series(['0~2', '2~5', '5~7', '7~8', '8~9','9~9.5', '9.5~10'])
    y_value_2 = series[(series <= 2)].shape[0]
    y_value_5 = series[(series > 2) & (series <= 5)].shape[0]
    y_value_7 = series[(series > 5) & (series <= 7)].shape[0]
    y_value_8 = series[(series > 7) & (series <= 8)].shape[0]
    y_value_9 = series[(series > 8) & (series <= 9)].shape[0]
    y_value_95 = series[(series > 9) & (series <= 9.5)].shape[0]
    y_value_10 = series[(series > 9.5) & (series <= 10)].shape[0]
    y_label_value = pd.Series([y_value_2, y_value_5, y_value_7, y_value_8, y_value_9, y_value_95, y_value_10])

    plt.figure(figsize=(8,5))    # 设置画布尺寸
    plt.tick_params(labelsize=12)    # 设置坐标轴字符大小
    plt.title('评分标准下的番剧分布', size=20, family='YouYuan')    # 标题，字号大小为20，中文字体类型
    plt.xlabel('总评分', size=14, family='YouYuan')
    plt.ylabel('番剧数/部', size=14, family='YouYuan')
    plt.ylim((0, 1000))    # 设置纵坐标范围
    grade_plot = plt.bar(x_label_value, y_label_value, width=0.5, color='k', alpha=0.7)
    dataTag('num', plot=grade_plot)
    plt.show()
    return None

def tags_analysis_single(dicts):
    '''
    标签单项分析：横向条形图
    :param dicts: df_tags
    '''
    # 先把传入的字典转换为画图需要的元组和列表
    sorted_dict_item = sorted(dicts.items(), key=lambda x:x[1], reverse=True)
    sum = df.shape[0]; i = 0
    y_label_value = pd.Series([])
    x_label_value = pd.Series([])

    for each in sorted_dict_item:
        if i < 15:
            y_label_value = y_label_value.append(pd.Series([each[0]], index=[14-i]))
            x_label_value = x_label_value.append(pd.Series([each[1]], index=[14-i]))
            i += 1
        else:
            break

    plt.figure(figsize=(8, 5))    # 设置画布尺寸
    plt.yticks(fontproperties='YouYuan', size=12)    # 设置y轴文本属性
    plt.tick_params(labelsize=12)    # 设置坐标轴数字字符大小
    plt.title('番剧标签分布', size=20, family='YouYuan')    # 标题，字号大小为20，中文字体类型
    plt.xlabel('标签数/个', size=14, family='YouYuan')
    plt.ylabel('标签名', size=14, family='YouYuan')
    plt.xlim((0, 650))    # 设置横坐标范围
    y_label_value = y_label_value.sort_index()    # 按索引重排序，使条形图长度递减
    x_label_value = x_label_value.sort_index()
    tags_plot = plt.barh(y_label_value, width=x_label_value, alpha=0.6, color='k')
    dataTag('percent', sum, plot=tags_plot)
    plt.show()

def actor_analysis_single(dicts):
    '''
    标签单项分析：横向条形图
    :param dicts: df_tags
    '''
    # 先把传入的字典转换为画图需要的元组和列表
    sorted_dict_item = sorted(dicts.items(), key=lambda x:x[1], reverse=True)
    sum = 0; i = 0
    y_label_value = pd.Series([])
    x_label_value = pd.Series([])
    for each in sorted_dict_item:
        sum += each[1]
    for each in sorted_dict_item:
        if i < 15:
            y_label_value = y_label_value.append(pd.Series([each[0]], index=[14-i]))
            x_label_value = x_label_value.append(pd.Series([each[1]], index=[14-i]))
            i += 1
        else:
            break

    plt.figure(figsize=(8, 5))    # 设置画布尺寸
    plt.yticks(fontproperties='YouYuan', size=12)    # 设置y轴文本属性
    plt.tick_params(labelsize=12)    # 设置坐标轴数字字符大小
    plt.title('爆肝声优', size=20, family='YouYuan')    # 标题，字号大小为20，中文字体类型
    plt.xlabel('配音角色数/个', size=14, family='YouYuan')
    plt.ylabel('声优', size=14, family='YouYuan')
    plt.xlim((0, 150))    # 设置横坐标范围
    y_label_value = y_label_value.sort_index()    # 按索引重排序，使条形图长度递减
    x_label_value = x_label_value.sort_index()
    plot_actor = plt.barh(y_label_value, width=x_label_value, alpha=0.6, color='k')
    for each in plot_actor:
        plt.text(each.get_width() + 2, each.get_y() + 0.2, each.get_width())
    plt.show()

def director_analysis_single(dicts):
    '''
    标签单项分析：横向条形图
    :param dicts: df_staff[0] 取导演
    '''
    # 先把传入的字典转换为画图需要的元组和列表
    sorted_dict_item = sorted(dicts.items(), key=lambda x:x[1], reverse=True)
    sum = 0; i = 0
    y_label_value = pd.Series([])
    x_label_value = pd.Series([])
    for each in sorted_dict_item:
        sum += each[1]
    for each in sorted_dict_item:
        if i < 15:
            y_label_value = y_label_value.append(pd.Series([each[0]], index=[14-i]))
            x_label_value = x_label_value.append(pd.Series([each[1]], index=[14-i]))
            i += 1
        else:
            break

    plt.figure(figsize=(8, 5))    # 设置画布尺寸
    plt.yticks(fontproperties='YouYuan', size=12)    # 设置y轴文本属性
    plt.tick_params(labelsize=12)    # 设置坐标轴数字字符大小
    plt.title('爆肝导演', size=20, family='YouYuan')    # 标题，字号大小为20，中文字体类型
    plt.xlabel('作品数/个', size=14, family='YouYuan')
    plt.ylabel('导演', size=14, family='YouYuan')
    plt.xlim((0, 30))    # 设置横坐标范围
    y_label_value = y_label_value.sort_index()    # 按索引重排序，使条形图长度递减
    x_label_value = x_label_value.sort_index()
    plot_actor = plt.barh(y_label_value, width=x_label_value, alpha=0.6, color='k')
    for each in plot_actor:
        plt.text(each.get_width()+0.5, each.get_y() + 0.2, each.get_width())
    plt.show()

def author_analysis_single(dicts):
    '''
    标签单项分析：横向条形图
    :param dicts: df_staff[0] 取导演
    '''
    # 先把传入的字典转换为画图需要的元组和列表
    sorted_dict_item = sorted(dicts.items(), key=lambda x:x[1], reverse=True)
    sum = 0; i = 0
    y_label_value = pd.Series([])
    x_label_value = pd.Series([])
    for each in sorted_dict_item:
        sum += each[1]
    for each in sorted_dict_item:
        if i < 9:
            if each[0] != '':
                y_label_value = y_label_value.append(pd.Series([each[0]], index=[8-i]))
                x_label_value = x_label_value.append(pd.Series([each[1]], index=[8-i]))
            i += 1
        else:
            break

    plt.figure(figsize=(8, 5))    # 设置画布尺寸
    plt.yticks(fontproperties='YouYuan', size=12)    # 设置y轴文本属性
    plt.tick_params(labelsize=12)    # 设置坐标轴数字字符大小
    plt.title('爆肝原作', size=20, family='YouYuan')    # 标题，字号大小为20，中文字体类型
    plt.xlabel('作品数/个', size=14, family='YouYuan')
    plt.ylabel('作者', size=14, family='YouYuan')
    plt.xlim((0, 70))    # 设置横坐标范围
    y_label_value = y_label_value.sort_index()    # 按索引重排序，使条形图长度递减
    x_label_value = x_label_value.sort_index()
    plot_actor = plt.barh(y_label_value, width=x_label_value, alpha=0.6, color='k')
    for each in plot_actor:
        plt.text(each.get_width()+0.5, each.get_y() + 0.2, each.get_width())
    plt.show()


# 播放量、总评分、评分人数、弹幕量、追番数五项的标准协方差矩阵以及相关系数矩阵
def std_cor():
    new_df = pd.DataFrame({'播放量': df_plays_unsort, '总评分': df_avg_grade_unsort ,'评分人数': df_gradeCounts,
                           '弹幕量': df_barCounts, '追番数': df_follows})
    filt_new_df = new_df[new_df['评分人数'] > 0]
    # print(filt_new_df)
    # print(filt_new_df.corr())    # 打印相关系数表
    # print(filt_new_df.cov())    # 打印协方差矩阵
    corr = filt_new_df.corr()

    matplotlib.rcParams['font.family'] = 'YouYuan'  # 设置全局字体为幼圆
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, vmax=1, square=True, cmap="Blues")    # 绘制相关系数矩阵热力图
    plt.title('各指标的相关系数矩阵', size=25, family='YouYuan')  # 标题，字号大小为20，中文字体类型
    plt.savefig('std_corr', dpi=150)
    plt.show()


# 双变量分析
def plays_grade():
    plays_grade = pd.DataFrame({'播放量': df_plays_unsort, '总评分': df_avg_grade_unsort})
    plt.figure(figsize=(7, 5))    # 设置画布尺寸
    plt.yticks(fontproperties='YouYuan', size=12)    # 设置y轴文本属性
    plt.tick_params(labelsize=12)    # 设置坐标轴数字字符大小
    plt.title('播放量与评分的关系', size=20, family='YouYuan')    # 标题，字号大小为20，中文字体类型
    plt.xlabel('评分', size=14, family='YouYuan')
    plt.ylabel('播放量/万', size=14, family='YouYuan')
    # plt.ylim((0, 40000))    # 设置纵坐标范围
    # plt.xlim((0, 10))    # 设置横坐标范围
    new_plays_grade = plays_grade[plays_grade['总评分'] >= 2]
    plt.scatter(new_plays_grade['总评分'], new_plays_grade['播放量'], marker='+')
    plt.savefig("plays_grade.jpg", dpi=150)
    plt.show()

def plays_gradeCounts():
    plays_gradeCounts = pd.DataFrame({'播放量': df_plays_unsort, '评分人数': df_gradeCounts})
    plt.figure(figsize=(7, 5))    # 设置画布尺寸
    plt.yticks(fontproperties='YouYuan', size=12)    # 设置y轴文本属性
    plt.tick_params(labelsize=12)    # 设置坐标轴数字字符大小
    plt.title('播放量与评分人数的关系', size=20, family='YouYuan')    # 标题，字号大小为20，中文字体类型
    plt.xlabel('评分人数/位', size=14, family='YouYuan')
    plt.ylabel('播放量/万', size=14, family='YouYuan')
    # plt.ylim((0, 40000))    # 设置纵坐标范围
    # plt.xlim((0, 10))    # 设置横坐标范围
    new_plays_gradeCounts = plays_gradeCounts[plays_gradeCounts['评分人数'] > 0]

    linear = linear_model.LinearRegression()
    linear.fit(np.array(new_plays_gradeCounts['评分人数']).reshape(-1,1), new_plays_gradeCounts['播放量'])  # 拟合输入输出数据

    print('Coefficients: ', linear.coef_)  # 查看回归方程系数
    print('intercept: ', linear.intercept_)  # 查看回归方程截距

    X = np.arange(min(df_gradeCounts), max(df_gradeCounts)).reshape(-1, 1)    # 以评分人数的最大值和最小值为范围建立等差数列，方便后续画图

    plt.scatter(new_plays_gradeCounts['评分人数'], new_plays_gradeCounts['播放量'])
    plt.plot(X, linear.predict(X), color='blue')
    plt.savefig("plays_gradeCounts.jpg", dpi=150)
    plt.show()

def plays_time():
    plays_time = pd.DataFrame({'开播时间': df_release_time, '播放量': df_plays_unsort})
    Jan, Apr, Jul, Oct, oth = [], [], [], [], []
    # print(plays_time)
    for i in range(len(plays_time)):
        if '01-01' in str(plays_time.iloc[i][0]):
            Jan.append(plays_time.iloc[i][1])
        elif '04-01' in str(plays_time.iloc[i][0]):
            Apr.append(plays_time.iloc[i][1])
        elif '07-01' in str(plays_time.iloc[i][0]):
            Jul.append(plays_time.iloc[i][1])
        elif '10-01' in str(plays_time.iloc[i][0]):
            Oct.append(plays_time.iloc[i][1])
        else:
            oth.append(plays_time.iloc[i][1])

    # 绘制箱线图
    plt.boxplot((Jan, Apr, Jul, Oct, oth), labels=["Jan.", "Apr.", "July", "Oct.", "others"],showfliers=False)    # 绘制箱线图
    plt.yticks(fontproperties='YouYuan', size=12)  # 设置y轴文本属性
    plt.tick_params(labelsize=12)  # 设置坐标轴数字字符大小
    plt.title('播放量与上映季度的关系', size=20, family='YouYuan')  # 标题，字号大小为20，中文字体类型
    plt.xlabel('季度', size=14, family='YouYuan')
    plt.ylabel('播放量/万', size=14, family='YouYuan')
    plt.ylim((0, 2000))  # 设置纵坐标范围
    plt.savefig('plays_time.jpg', dpi=150)
    plt.show()

def plays_tags():
    plays_tags = pd.DataFrame({'标签': df["标签"], '播放量': df_plays_unsort})
    qihua, rexue, richang, kehuan, zhandou, mengxi, mangai, gaoxiao, xiaoyuan, zhiyu = [], [], [], [], [], [], [], [], [], []
    for i in range(len(plays_tags)):
        for each in eval(df["标签"][i]):
            if each == "奇幻":
                qihua.append(plays_tags.iloc[i][1])
            elif each == "热血":
                rexue.append(plays_tags.iloc[i][1])
            elif each == "日常":
                richang.append(plays_tags.iloc[i][1])
            elif each == "科幻":
                kehuan.append(plays_tags.iloc[i][1])
            elif each == "战斗":
                zhandou.append(plays_tags.iloc[i][1])
            elif each == "萌系":
                mengxi.append(plays_tags.iloc[i][1])
            elif each == "漫画改":
                mangai.append(plays_tags.iloc[i][1])
            elif each == "搞笑":
                gaoxiao.append(plays_tags.iloc[i][1])
            elif each == "校园":
                xiaoyuan.append(plays_tags.iloc[i][1])
            elif each == "治愈":
                zhiyu.append(plays_tags.iloc[i][1])

    # 绘制箱线图
    # 值得注意的是，由于番剧间播放量之间的差距较大，远距离的离群点被判定为异常值，所以箱线图中显示的最大值不代表绝对数据，可以认为是一个相对的概念
    matplotlib.rcParams['font.family'] = 'YouYuan'    # 设置全局字体为幼圆
    plt.boxplot((qihua, rexue, richang, kehuan, zhandou, mengxi, mangai, gaoxiao, xiaoyuan, zhiyu),
                labels=["奇幻", "热血", "日常", "科幻", "战斗", "萌系", "漫改", "搞笑", "校园", "治愈"],
                showfliers=False)  # 绘制箱线图
    plt.yticks(fontproperties='YouYuan', size=12)  # 设置y轴文本属性
    plt.tick_params(labelsize=12)  # 设置坐标轴数字字符大小
    plt.title('各类型番剧的播放量', size=20, family='YouYuan')  # 标题，字号大小为20，中文字体类型
    plt.xlabel('番剧类型', size=14, family='YouYuan')
    plt.ylabel('播放量/万', size=14, family='YouYuan')
    # plt.ylim((0, 2000))  # 设置纵坐标范围
    plt.savefig('plays_tags.jpg', dpi=150)
    plt.show()

def time_grade():
    time_grade = pd.DataFrame({'开播时间': df_release_time, '总评分': df_avg_grade_unsort})
    time_grade = time_grade[time_grade["总评分"] > 0]
    Jan, Apr, Jul, Oct, oth = [], [], [], [], []
    # print(time_grade)
    for i in range(len(time_grade)):
        if '01-01' in str(time_grade.iloc[i][0]):
            Jan.append(time_grade.iloc[i][1])
        elif '04-01' in str(time_grade.iloc[i][0]):
            Apr.append(time_grade.iloc[i][1])
        elif '07-01' in str(time_grade.iloc[i][0]):
            Jul.append(time_grade.iloc[i][1])
        elif '10-01' in str(time_grade.iloc[i][0]):
            Oct.append(time_grade.iloc[i][1])
        else:
            oth.append(time_grade.iloc[i][1])

    # 绘制箱线图
    plt.boxplot((Jan, Apr, Jul, Oct, oth), labels=["Jan.", "Apr.", "July", "Oct.", "others"],showfliers=False)    # 绘制箱线图
    plt.yticks(fontproperties='YouYuan', size=12)  # 设置y轴文本属性
    plt.tick_params(labelsize=12)  # 设置坐标轴数字字符大小
    plt.title('评分与上映季度的关系', size=20, family='YouYuan')  # 标题，字号大小为20，中文字体类型
    plt.xlabel('季度', size=14, family='YouYuan')
    plt.ylabel('评分', size=14, family='YouYuan')
    # plt.ylim((-2, 10))  # 设置纵坐标范围
    plt.savefig('time_grade.jpg', dpi=150)
    plt.show()

def grade_tags():
    grade_tags = pd.DataFrame({'标签': df["标签"], '总评分': df_avg_grade_unsort})
    grade_tags = grade_tags[grade_tags["总评分"] > 0]
    qihua, rexue, richang, kehuan, zhandou, mengxi, mangai, gaoxiao, xiaoyuan, zhiyu = [], [], [], [], [], [], [], [], [], []
    for i in range(len(grade_tags)):
        for each in eval(df["标签"][i]):
            if each == "奇幻":
                qihua.append(grade_tags.iloc[i][1])
            elif each == "热血":
                rexue.append(grade_tags.iloc[i][1])
            elif each == "日常":
                richang.append(grade_tags.iloc[i][1])
            elif each == "科幻":
                kehuan.append(grade_tags.iloc[i][1])
            elif each == "战斗":
                zhandou.append(grade_tags.iloc[i][1])
            elif each == "萌系":
                mengxi.append(grade_tags.iloc[i][1])
            elif each == "漫画改":
                mangai.append(grade_tags.iloc[i][1])
            elif each == "搞笑":
                gaoxiao.append(grade_tags.iloc[i][1])
            elif each == "校园":
                xiaoyuan.append(grade_tags.iloc[i][1])
            elif each == "治愈":
                zhiyu.append(grade_tags.iloc[i][1])

    # 绘制箱线图
    # 值得注意的是，由于番剧间播放量之间的差距较大，远距离的离群点被判定为异常值，所以箱线图中显示的最大值不代表绝对数据，可以认为是一个相对的概念
    matplotlib.rcParams['font.family'] = 'YouYuan'    # 设置全局字体为幼圆
    plt.boxplot((qihua, rexue, richang, kehuan, zhandou, mengxi, mangai, gaoxiao, xiaoyuan, zhiyu),
                labels=["奇幻", "热血", "日常", "科幻", "战斗", "萌系", "漫改", "搞笑", "校园", "治愈"],
                showfliers=False)  # 绘制箱线图
    plt.yticks(fontproperties='YouYuan', size=12)  # 设置y轴文本属性
    plt.tick_params(labelsize=12)  # 设置坐标轴数字字符大小
    plt.title('各类型番剧的评分', size=20, family='YouYuan')  # 标题，字号大小为20，中文字体类型
    plt.xlabel('番剧类型', size=14, family='YouYuan')
    plt.ylabel('评分', size=14, family='YouYuan')
    # plt.ylim((0, 2000))  # 设置纵坐标范围
    plt.savefig('grade_tags.jpg', dpi=150)
    plt.show()


# 多变量分析
new_df = pd.DataFrame({'播放量': df_plays_unsort, '弹幕量': df_barCounts, '追番数': df_follows,
                       '评分人数': df_gradeCounts, '剧集数': df_series, '总评分': df_avg_grade_unsort,
                       '标签': df["标签"]}).replace(0, NA).dropna()

def retentionRate_grade():
    '''
    每部番剧的观众留存率和评分间的关系
    画散点图
    :return:
    '''
    new_df_inside = new_df[new_df["剧集数"] > 10]
    retentionRate = new_df_inside['播放量'] / new_df_inside['剧集数'] / new_df_inside["追番数"]

    plt.figure(figsize=(7, 5))    # 设置画布尺寸
    plt.yticks(fontproperties='YouYuan', size=12)    # 设置y轴文本属性
    plt.tick_params(labelsize=12)    # 设置坐标轴数字字符大小
    plt.title('留存率与评分的关系', size=20, family='YouYuan')    # 标题，字号大小为20，中文字体类型
    plt.xlabel('评分', size=14, family='YouYuan')
    plt.ylabel('留存率', size=14, family='YouYuan')
    plt.ylim((0, 6))    # 设置纵坐标范围
    # plt.xlim((0, 10))    # 设置横坐标范围
    plt.scatter(new_df_inside['总评分'], retentionRate, marker='+')
    plt.savefig("retentionRate_grade.jpg", dpi=150)
    plt.show()

def retentionRate_tags():
    '''
     每部番剧的观众留存率和评分间的关系
     画箱线图
     :return:
     '''
    new_df_inside = new_df[new_df["剧集数"] > 10]
    retentionRate = new_df_inside['播放量'] / new_df_inside['剧集数'] / new_df_inside["追番数"]

    qihua, rexue, richang, kehuan, zhandou, mengxi, mangai, gaoxiao, xiaoyuan, zhiyu = [], [], [], [], [], [], [], [], [], []
    for index in new_df_inside.index:
        for each in eval(new_df_inside["标签"][index]):
            if each == "奇幻":
                qihua.append(retentionRate[index])
            elif each == "热血":
                rexue.append(retentionRate[index])
            elif each == "日常":
                richang.append(retentionRate[index])
            elif each == "科幻":
                kehuan.append(retentionRate[index])
            elif each == "战斗":
                zhandou.append(retentionRate[index])
            elif each == "萌系":
                mengxi.append(retentionRate[index])
            elif each == "漫画改":
                mangai.append(retentionRate[index])
            elif each == "搞笑":
                gaoxiao.append(retentionRate[index])
            elif each == "校园":
                xiaoyuan.append(retentionRate[index])
            elif each == "治愈":
                zhiyu.append(retentionRate[index])

    # 绘制箱线图
    # 值得注意的是，由于番剧间播放量之间的差距较大，远距离的离群点被判定为异常值，所以箱线图中显示的最大值不代表绝对数据，可以认为是一个相对的概念
    matplotlib.rcParams['font.family'] = 'YouYuan'    # 设置全局字体为幼圆
    plt.boxplot((qihua, rexue, richang, kehuan, zhandou, mengxi, mangai, gaoxiao, xiaoyuan, zhiyu),
                labels=["奇幻", "热血", "日常", "科幻", "战斗", "萌系", "漫改", "搞笑", "校园", "治愈"],
                showfliers=False)  # 绘制箱线图
    plt.yticks(fontproperties='YouYuan', size=12)  # 设置y轴文本属性
    plt.tick_params(labelsize=12)  # 设置坐标轴数字字符大小
    plt.title('各类型番剧的留存率', size=20, family='YouYuan')  # 标题，字号大小为20，中文字体类型
    plt.xlabel('番剧类型', size=14, family='YouYuan')
    plt.ylabel('留存率', size=14, family='YouYuan')
    # plt.ylim((0, 2000))  # 设置纵坐标范围
    plt.savefig('retentionRate_tags', dpi=150)
    plt.show()

def userActivity_grade():
    '''
    每部番剧的用户活跃度和评分间的关系
    画散点图
    :return:
    '''
    new_df_inside = new_df
    userActivity = new_df_inside["弹幕量"] / new_df_inside["播放量"] / new_df_inside["剧集数"] * 10    # 10为调整系数

    plt.figure(figsize=(7, 5))    # 设置画布尺寸
    plt.yticks(fontproperties='YouYuan', size=12)    # 设置y轴文本属性
    plt.tick_params(labelsize=12)    # 设置坐标轴数字字符大小
    plt.title('用户活跃度与评分的关系', size=20, family='YouYuan')    # 标题，字号大小为20，中文字体类型
    plt.xlabel('评分', size=14, family='YouYuan')
    plt.ylabel('活跃度', size=14, family='YouYuan')
    plt.ylim((0, 0.75))    # 设置纵坐标范围
    # plt.xlim((0, 10))    # 设置横坐标范围
    plt.scatter(new_df_inside['总评分'], userActivity, marker='+')
    plt.savefig("uesrActivity_grade.jpg", dpi=150)
    plt.show()

def userActivity_tags():
    '''
     每部番剧的用户活跃度和评分间的关系
     画箱线图
     :return:
     '''
    new_df_inside = new_df
    userActivity = new_df_inside["弹幕量"] / new_df_inside["播放量"] / new_df_inside["剧集数"] * 10    # 10为调整系数

    qihua, rexue, richang, kehuan, zhandou, mengxi, mangai, gaoxiao, xiaoyuan, zhiyu = [], [], [], [], [], [], [], [], [], []
    for index in new_df_inside.index:
        for each in eval(new_df_inside["标签"][index]):
            if each == "奇幻":
                qihua.append(userActivity[index])
            elif each == "热血":
                rexue.append(userActivity[index])
            elif each == "日常":
                richang.append(userActivity[index])
            elif each == "科幻":
                kehuan.append(userActivity[index])
            elif each == "战斗":
                zhandou.append(userActivity[index])
            elif each == "萌系":
                mengxi.append(userActivity[index])
            elif each == "漫画改":
                mangai.append(userActivity[index])
            elif each == "搞笑":
                gaoxiao.append(userActivity[index])
            elif each == "校园":
                xiaoyuan.append(userActivity[index])
            elif each == "治愈":
                zhiyu.append(userActivity[index])

    # 绘制箱线图
    # 值得注意的是，由于番剧间播放量之间的差距较大，远距离的离群点被判定为异常值，所以箱线图中显示的最大值不代表绝对数据，可以认为是一个相对的概念
    matplotlib.rcParams['font.family'] = 'YouYuan'    # 设置全局字体为幼圆
    plt.boxplot((qihua, rexue, richang, kehuan, zhandou, mengxi, mangai, gaoxiao, xiaoyuan, zhiyu),
                labels=["奇幻", "热血", "日常", "科幻", "战斗", "萌系", "漫改", "搞笑", "校园", "治愈"],
                showfliers=False)  # 绘制箱线图
    plt.yticks(fontproperties='YouYuan', size=12)  # 设置y轴文本属性
    plt.tick_params(labelsize=12)  # 设置坐标轴数字字符大小
    plt.title('各类型番剧的留存率', size=20, family='YouYuan')  # 标题，字号大小为20，中文字体类型
    plt.xlabel('番剧类型', size=14, family='YouYuan')
    plt.ylabel('留存率', size=14, family='YouYuan')
    # plt.ylim((0, 2000))  # 设置纵坐标范围
    plt.savefig('userActivity_tags', dpi=150)
    plt.show()


# 执行指令：
# plays_analysis_single(df_plays)
# grade_analysis_single(df_avg_grade)
# tags_analysis_single(df_tags)
# actor_analysis_single(df_actor)
# director_analysis_single(df_staff[0])
# author_analysis_single(df_staff[1])

# plays_grade()    # 画播放量和总评分关系图
# plays_gradeCounts()    # 画播放量和评分人数关系图
# std_cor()    # 打印协方差矩阵和相关系数矩阵
# plays_time()    # 画播放量和开播时间的箱线图
# plays_tags()    # 画播放量和标签的箱线图
# time_grade()    # 画开播时间和评分的箱线图
# grade_tags()    # 画评分和番剧类型的箱线图

# retentionRate_grade()    # 观众留存率与评分的关系
# retentionRate_tags()    # 观众留存率与标签之间的关系
# userActivity_grade()    # 用户活跃度和评分的关系
# userActivity_tags()    # 用户活跃度与标签之间的关系