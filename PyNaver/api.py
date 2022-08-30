import json
import requests
import pandas as pd


class Naver:
    """
    네이버 API 클래스
    """
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret


class NaverCloudPlatform:
    """
    네이버 클라우드 플랫폼 API 클래스
    """
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret