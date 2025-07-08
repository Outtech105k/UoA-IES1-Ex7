import requests
import datetime
import zoneinfo
import json

class WebApi:
    url = "http://facedetect.outtech105.com/api"

    def approve_post(self):
        now_jst = datetime.datetime.now(zoneinfo.ZoneInfo("Asia/Tokyo"))
        body_dic = {
            'detected': now_jst.isoformat(),
            'status': 'approved',
        }
        requests.post(
            self.url + '/faceauth',
            json.dumps(body_dic),
            headers={'Content-Type': 'application/json'}
            )

    def reject_post(self):
        now_jst = datetime.datetime.now(zoneinfo.ZoneInfo("Asia/Tokyo"))
        body_dic = {
            'detected': now_jst.isoformat(),
            'status': 'rejected',
        }
        requests.post(
            self.url + '/faceauth',
            json.dumps(body_dic),
            headers={'Content-Type': 'application/json'}
            )
