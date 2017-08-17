# encoding = "utf-8"
import requests
import sys
import os
import configparser
import json
import tkinter
import tkinter.messagebox

class SchoolWeb:
    headers = {
        'HOST':'223.2.10.172',
        'Connection':'keep-alive',
        'Origin':'http://223.2.10.172',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept':'*/*',
        'Referer':'http://223.2.10.172/eportal/index.jsp',
        'Accept-Encoding':'gzip, deflate'
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
        self.queryString = self.config.get('SchoolWeb','queryString')
        self.__session = requests.Session()

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
