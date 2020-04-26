#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2018/09/05
# 淘宝秒杀脚本，扫码登录版
import os
from selenium import webdriver
import datetime
import time
from os import path
from selenium.webdriver.common.action_chains import ActionChains

d = path.dirname(__file__)
abspath = path.abspath(d)

browser = webdriver.Chrome()
browser.maximize_window()


def login():
    # 打开淘宝登录页，并进行扫码登录
    browser.get("https://www.taobao.com")
    time.sleep(3)
    if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()

    print("请在15秒内完成扫码")
    time.sleep(15)

    browser.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)
    # 点击购物车里全选按钮
    # if browser.find_element_by_id("J_CheckBox_939775250537"):
    # browser.find_element_by_id("J_CheckBox_939775250537").click()
    # if browser.find_element_by_id("J_CheckBox_939558169627"):
    # browser.find_element_by_id("J_CheckBox_939558169627").click()
    if browser.find_element_by_id("J_SelectAll1"):
        browser.find_element_by_id("J_SelectAll1").click()
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    # 对比时间，时间到的话就点击结算
        if now > buytime:
            try:
        # 点击结算按钮
                if browser.find_element_by_id("J_Go"):
                    browser.find_element_by_id("J_Go").click()
                    browser.find_element_by_link_text('提交订单').click()
            except:
                time.sleep(0.1)
        print(now)
        time.sleep(0.1)


if __name__ == "__main__":
    times = "2018-10-22 18:55:00.000000"
    # 时间格式："2018-09-06 11:20:00.000000"
    login()
    buy("2018-10-22 18:55:00.000000")