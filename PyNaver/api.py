import json
import requests
import pandas as pd


class NaverCloudPlatform:
    """
    네이버 클라우드 플랫폼 API 클래스
    """
    def __init__(self, client_id, client_secret):
        self.headers = {
            "X-NCP-APIGW-API-KEY-ID": client_id,
            "X-NCP-APIGW-API-KEY": client_secret,
        }
        
    def geocoding(self, query):
        """
        지오코딩 API
        """
        url = f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={query}"
        res = requests.get(url, headers=self.headers)
        if res.status_code == 200:
            return res.json()
        else:
            return res

    def reverse_geocoding(self, lon, lat):
        """
        리버스 지오코딩 API
        """
        coords = f"{lon},{lat}"
        url = f"https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc?coords={coords}&output=json&orders=addr"
        res = requests.get(url, headers=self.headers)
        if res.status_code == 200:
            return res.json()
        else:
            return res
        
    def directions5(self, **kwargs):
        """
        Directions5 API
        
        - start: 출발지 (필수)
        - goal: 목적지 (필수)
            하나 이상의 목적지 정보를 전달할 수 있으며, 복수 개의 목적지를 입력할 때는 :로 연결
            입력한 목적지 정보 중 가장 적은 비용으로 도달할 수 있는 목적지로 경로가 생성됨
            목적지의 최대 개수는 10개이며, 최초의 최적 목적지 좌표를 기준으로 직선거리 3km 이내의 좌표만 유효하게 판정
        - waypoints: 경유지
            최대 5개를 입력할 수 있으며 서로 다른 경유지의 구분자로 |(pipe char)를 사용
        - option: 탐색 옵션
            옵션은 최대 3개까지 동시에 요청할 수 있으며, 여러 옵션은 ‘:'로 연결
            기본값은 traoptimal
        - cartype: 톨게이트 요금 계산용 차종 정보
            기본값은 1
            차종을 바탕으로 차량의 중량 또는 크기를 판단하지 않음
            3, 4, 5종은 option에서 traavoidtoll이 적용되지 않았더라도 하이패스 전용 톨게이트를 회피해서 탐색
            일반적인 승용차는 모두 1종
        - fueltype: 유류비 계산용 유종
            기본값은 gasoline
        - mileage: 설정된 유류에 해당하는 연비
            사용하는 차량의 연비를 사용자가 직접 입력하고자 할 때 사용하는 파라미터
            기본값은 14
        - lang: 언어 종류
            기본값은 ko
        """
        url = f"https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving?"
        for k, v in kwargs.items():
            url += f"{k}={v}&"
        res = requests.get(url, headers=self.headers)
        if res.status_code == 200:
            return res.json()
        else:
            return res

    def directions15(self, **kwargs):
        """
        Directions15 API
        
        - start: 출발지 (필수)
        - goal: 목적지 (필수)
            하나 이상의 목적지 정보를 전달할 수 있으며, 복수 개의 목적지를 입력할 때는 :로 연결
            입력한 목적지 정보 중 가장 적은 비용으로 도달할 수 있는 목적지로 경로가 생성됨
            목적지의 최대 개수는 10개이며, 최초의 최적 목적지 좌표를 기준으로 직선거리 3km 이내의 좌표만 유효하게 판정
        - waypoints: 경유지
            최대 15개를 입력할 수 있음
            서로 다른 경유지의 구분자로 |(pipe char)를 사용
        - option: 탐색 옵션
            옵션은 최대 3개까지 동시에 요청할 수 있음
            여러 옵션은 ‘:'로 연결하며 기본값은 traoptimal
        - cartype: 톨게이트 요금 계산용 차종 정보
            기본값은 1
            차종을 바탕으로 차량의 중량 또는 크기를 판단하지는 않음
            3, 4, 5종은 option에서 traavoidtoll이 적용되지 않았더라도 하이패스 전용 톨게이트를 회피해서 탐색
            일반적인 승용차는 모두 1종
        - fueltype: 유류비 계산용 유종
            기본값은 gasoline
        - mileage: 설정된 유류에 해당하는 연비
            사용하는 차량의 연비를 사용자가 직접 입력하고자 할 때 사용하는 파라미터
            기본값은 14
        - lang: 언어 종류
            기본값은 ko
        """
        url = f"https://naveropenapi.apigw.ntruss.com/map-direction-15/v1/driving?"
        for k, v in kwargs.items():
            url += f"{k}={v}&"
        res = requests.get(url, headers=self.headers)
        if res.status_code == 200:
            return res.json()
        else:
            return res