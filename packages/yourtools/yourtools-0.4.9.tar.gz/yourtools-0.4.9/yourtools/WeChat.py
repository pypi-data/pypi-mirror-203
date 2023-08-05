# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@version    : v1.0
@author     : fangzheng
@contact    : fangzheng@rp-pet.cn
@software   : PyCharm
@filename   : WeChat.py
@create time: 2022/9/27 2:54 PM
@modify time: 2022/9/27 2:54 PM
@describe   : 
-------------------------------------------------
"""
import json
import requests
from requests_toolbelt import MultipartEncoder


def send_chat_msg(key, data):
    """
    发送机器人消息到企微群
    :param key: 机器人地址key
    :return:
    """
    try:
        url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}"
        header = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=header, data=json.dumps(data))
        if response.status_code == 200:
            result = json.loads(response.text)
            return result
    except Exception as err:
        raise Exception("Send Chat Message error", err)


class WeChat:
    def __init__(self, corpid, corpsecret, agentid):
        self.corpid = corpid
        self.corpsecret = corpsecret
        self.agentid = agentid
        self.access_token = self._getToken()

    def _getToken(self):
        try:
            if all([self.corpid, self.corpsecret]):
                url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}".format(
                    corpid=self.corpid, corpsecret=self.corpsecret)
                response = requests.get(url)
                if response.status_code == 200:
                    result = json.loads(response.text)
                    return result['access_token']
        except Exception as err:
            raise Exception("get WeChat access Token error", err)

    def _send_msg(self, data):
        self._check_token()
        try:
            send_url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}".format(
                access_token=self.access_token)
            response = requests.post(send_url, json.dumps(data))
            if response.status_code == 200:
                result = json.loads(response.text)
                return result
        except Exception as err:
            raise Exception("send WeChat Message error", err)

    def _check_token(self):
        if self.access_token is None:
            self._getToken()

    def send_msg(self, data):
        return self._send_msg(data)

    def upload_media(self, filetype, filepath, filename):
        """
        上传临时素材到企微并获取media_id
        :param filetype: 图片（image）、语音（voice）、视频（video），普通文件（file）
        :param filepath:
        :param filename:
        :return: media_id
        """
        try:
            self._check_token()
            post_file_url = "https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={access_token}&type={filetype}".format(
                filetype=filetype,
                access_token=self.access_token)

            m = MultipartEncoder(
                fields={filename: (filename, open(filepath + filename, 'rb'), 'text/plain')},
            )
            response = requests.post(url=post_file_url, data=m, headers={'Content-Type': m.content_type})
            if response.status_code == 200:
                result = json.loads(response.text)
                return result['media_id']
            else:
                print("HTTP Error:", response.status_code)
                return None
        except Exception as err:
            raise Exception("upload media error", err)

    def get_media(self, media_id):
        """
        获取临时素材
        :param media_id:
        :return: 返回二进制形式
        """
        try:
            self._check_token()
            url = "https://qyapi.weixin.qq.com/cgi-bin/media/get"
            params = {
                "access_token": self.access_token,
                "media_id": media_id
            }
            response = requests.get(url=url, params=params)
            if response.status_code == 200:
                content_type = response.headers.get('Content-Type')
                if content_type == 'application/json':
                    response_data = json.loads(response.text)
                    print("Error:", response_data.get("errmsg"))
                    return None
                else:
                    return response.content
            else:
                print("HTTP Error:", response.status_code)
                return None
        except Exception as err:
            raise Exception("get media error", err)
