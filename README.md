# CampusWebLogin
An Easy way to log in the campus network, written in [Python](https://www.python.org/).

Welcome to read the Campus-Web-Login Source code! From this repository, you can login the NXXU School Web under **Windows** with just one click.Also you can use python file to login under **OS X** and **Linux**.

## Installation

with web server download zip(just click the Download Zip):

![github](/download.png)

also you can clone it with git(git needed):

```git
git clone git@github.com:datagridview/SchoolWebLogin.git
```

## Usage

you can use it in two ways.Windows **exe** or **py**

### exe

1. update the config.ini **in the dist directory**(/dist/config.ini). Change the `userId`  `password`  `service`


```ini
[SchoolWeb]
userId = # 学号
password = # 校园卡密码
service = # 10000 as 电信,10010 as 联通
```

2. click the **loginSchoolCampus.exe**
### py

1. update the config.ini (/config.ini).Change the `userId`  `password`  `service`  as exe settings
2. open you terminal and enter the project directory.
3. open with python.windows:

```
C:\Users\***\Desktop\SchoolWebLogin>python loginSchoolCampus.py
```

4. linux:
```shell
he@ubuntuServer:~/SchoolWebLogin$ python loginSchoolCampus.py
```

​	tips:use `alias` to make it easier

```shell
he@ubuntuServer:~/SchoolWebLogin$ alias webLogin='python loginSchoolCampus.py'
he@ubuntuServer:~/SchoolWebLogin$ webLogin
```

## Result

With two kind of result in the form of message box.

Login Success or Login failed.

## Others

* Email:[heyunfan1996@gmail.com](mailto:heyunfan1996@gmail.com)



**datagridview**