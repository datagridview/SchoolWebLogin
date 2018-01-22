# encoding = "utf-8"
import requests
import sys
import os
import configparser
import json
import tkinter
import tkinter.messagebox
from urllib.parse import urlparse,parse_qs,unquote,quote

class SchoolWeb:
    headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    __session = ''
    username = ''
    password = ''
    service = ''
    queryString = ''


    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.username = self.config.get('SchoolWeb','userId')
        self.password = self.config.get('SchoolWeb','password')
        self.service = self.config.get('SchoolWeb','service')
        if self.service == '10010':
            self.service = self.config.get('Server','liantong')
        elif self.service == '10000':
            self.service = self.config.get('Server','dianxin')
        self.queryString = self.getqueryString()
        self.__session = requests.Session()


    def getqueryString(self):
        response = requests.get('http://223.2.10.172/',headers=self.headers)
        script = response.text
        script_list = script.split("\'")
        location = script_list[1]
        queryString = location.split("?")[1]
        return quote(queryString)
        # location_parse = urlparse(location)
        # location_dict = parse_qs(location_parse.query)

    def login_InterFace(self):
        cgi_url = "http://223.2.10.172/eportal/InterFace.do?method=login"
        post_data = {
            'userId': self.username,
            'password': self.password,
            'service': self.service,
            'queryString': self.queryString,
            'operatorPwd':'',
            'operatorUserId':'',
            'validcode':''
        }
        response = self.__session.post(cgi_url, data=post_data, headers=self.headers, timeout=35)
        with open('xiaoyuanwang.json','wb') as f:
            f.write(bytes(response.text, 'utf-8'))
            f.close()       
        f1 = open('xiaoyuanwang.json', 'r')
        response = json.load(f1)
        return response['userIndex']

    def login_success_page(self):
        destination_url = "http://223.2.10.172/eportal/success.jsp"
        if self.login_InterFace()!='':
            playload = {
                'userIndex': self.login_InterFace(),
                'keepaliveInterval':'0'
            }
            response = self.__session.get(destination_url, headers=self.headers, params=playload)
            self.GUI()
        else:
            self.GUI_error()


    def GUI(self):
        root=tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showinfo('提示', '登录成功')
    
    def GUI_error(self):
        root=tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showerror('提示', '登录失败')

login = SchoolWeb()
login.login_success_page()
