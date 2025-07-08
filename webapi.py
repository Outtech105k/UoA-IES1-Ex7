import requests
import datetime
import zoneinfo
import json

class ApiRequestException(Exception):
    def __str__(self):
        return "API Error"

class WebApi:
    url = "http://facedetect.outtech105.com/api"

    def approve_post(self):
        now_jst = datetime.datetime.now(zoneinfo.ZoneInfo("Asia/Tokyo"))
        body_dic = {
            'detected': now_jst.isoformat(),
            'status': 'approved',
        }
        responce = requests.post(
            self.url + '/faceauth',
            json.dumps(body_dic),
            headers={'Content-Type': 'application/json'}
            )
        if responce.status_code != 200:
            raise ApiRequestException

    def reject_post(self):
        now_jst = datetime.datetime.now(zoneinfo.ZoneInfo("Asia/Tokyo"))
        body_dic = {
            'detected': now_jst.isoformat(),
            'status': 'rejected',
        }
        responce = requests.post(
            self.url + '/faceauth',
            json.dumps(body_dic),
            headers={'Content-Type': 'application/json'}
            )
        if responce.status_code != 200:
            raise ApiRequestException
