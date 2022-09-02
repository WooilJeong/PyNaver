import json
import requests
import pandas as pd

class Naver:
    """
    네이버 OPEN API 클래스
    """

    def __init__(self, client_id, client_secret):
        """
        API 인증 정보 초기화
        """
        self.headers = {
            "X-Naver-Client-Id": client_id,
            "X-Naver-Client-Secret": client_secret,
            "Content-Type": "application/json",
        }

    def datalab_search(self, **kwargs):
        """
        네이버 통합 검색어 트렌드 조회
        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/datalab/search/search.md
        """
        url = "https://openapi.naver.com/v1/datalab/search"
        data = {}
        for k, v in kwargs.items():
            data[k] = v
        data = json.dumps(data, ensure_ascii=False).encode("utf-8")
        res = requests.post(url, data=data, headers=self.headers)

        if res.status_code == 200:
            data = res.json()['results']
            num = len(data)
            df = pd.DataFrame()
            for i in range(num):
                sub = pd.DataFrame(data[i]['data'])
                sub['title'] = data[i]['title']
                sub = sub[['title', 'period', 'ratio']]
                df = pd.concat([df, sub], axis=0, ignore_index=True)
            pivot = pd.pivot(df, index='period', columns='title',
                             values='ratio').reset_index()
            pivot.columns.name = None
            pivot = pivot.rename(columns={"period": "날짜"})
            return pivot

        else:
            return res

    def datalab_shopping_categories(self, **kwargs):
        """
        쇼핑인사이트 분야별 트렌드 조회
        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/datalab/shopping/shopping.md
        """
        url = "https://openapi.naver.com/v1/datalab/shopping/categories"
        data = {}
        for k, v in kwargs.items():
            data[k] = v
        data = json.dumps(data, ensure_ascii=False).encode("utf-8")
        res = requests.post(url, data=data, headers=self.headers)
        if res.status_code == 200:
            data = res.json()['results']
            num = len(data)
            df = pd.DataFrame()
            for i in range(num):
                sub = pd.DataFrame(data[i]['data'])
                sub['title'] = data[i]['title']
                sub = sub[['title', 'period', 'ratio']]
                df = pd.concat([df, sub], axis=0, ignore_index=True)
            pivot = pd.pivot(df, index='period', columns='title',
                             values='ratio').reset_index()
            pivot.columns.name = None
            pivot = pivot.rename(columns={"period": "날짜"})
            return pivot

        else:
            return res

    def datalab_shopping_category_device(self, **kwargs):
        """
        쇼핑인사이트 분야 내 기기별 트렌드 조회
        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/datalab/shopping/shopping.md
        """
        url = "https://openapi.naver.com/v1/datalab/shopping/category/device"
        data = {}
        for k, v in kwargs.items():
            data[k] = v
        data = json.dumps(data, ensure_ascii=False).encode("utf-8")
        res = requests.post(url, data=data, headers=self.headers)
        if res.status_code == 200:
            data = res.json()['results']
            df = pd.DataFrame(data[0]['data'])
            df = df[['group', 'period', 'ratio']]
            pivot = pd.pivot(df, index='period', columns=[
                             'group'], values='ratio').reset_index()
            pivot.columns.name = None
            pivot = pivot.rename(columns={"period": "날짜"})
            return pivot

        else:
            return res

    def datalab_shopping_category_gender(self, **kwargs):
        """
        쇼핑인사이트 분야 내 성별 트렌드 조회
        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/datalab/shopping/shopping.md
        """
        url = "https://openapi.naver.com/v1/datalab/shopping/category/gender"
        data = {}
        for k, v in kwargs.items():
            data[k] = v
        data = json.dumps(data, ensure_ascii=False).encode("utf-8")
        res = requests.post(url, data=data, headers=self.headers)
        if res.status_code == 200:
            data = res.json()['results']
            df = pd.DataFrame(data[0]['data'])
            df = df[['group', 'period', 'ratio']]
            pivot = pd.pivot(df, index='period', columns=[
                             'group'], values='ratio').reset_index()
            pivot.columns.name = None
            pivot = pivot.rename(columns={"period": "날짜"})
            return pivot

        else:
            return res

    def datalab_shopping_category_age(self, **kwargs):
        """
        쇼핑인사이트 분야 내 연령별 트렌드 조회
        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/datalab/shopping/shopping.md
        """
        url = "https://openapi.naver.com/v1/datalab/shopping/category/age"
        data = {}
        for k, v in kwargs.items():
            data[k] = v
        data = json.dumps(data, ensure_ascii=False).encode("utf-8")
        res = requests.post(url, data=data, headers=self.headers)
        if res.status_code == 200:
            data = res.json()['results']
            df = pd.DataFrame(data[0]['data'])
            df = df[['group', 'period', 'ratio']]
            pivot = pd.pivot(df, index='period', columns=[
                             'group'], values='ratio').reset_index()
            pivot.columns.name = None
            pivot = pivot.rename(columns={"period": "날짜"})
            return pivot

        else:
            return res

    def datalab_shopping_category_keywords(self, **kwargs):
        """
        쇼핑인사이트 키워드별 트렌드 조회
        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/datalab/shopping/shopping.md
        """
        url = "https://openapi.naver.com/v1/datalab/shopping/category/keywords"
        data = {}
        for k, v in kwargs.items():
            data[k] = v
        data = json.dumps(data, ensure_ascii=False).encode("utf-8")
        res = requests.post(url, data=data, headers=self.headers)
        if res.status_code == 200:
            data = res.json()['results']
            num = len(data)
            df = pd.DataFrame()
            for i in range(num):
                sub = pd.DataFrame(data[i]['data'])
                sub['title'] = data[i]['title']
                sub = sub[['title', 'period', 'ratio']]
                df = pd.concat([df, sub], axis=0, ignore_index=True)
            pivot = pd.pivot(df, index='period', columns='title',
                             values='ratio').reset_index()
            pivot.columns.name = None
            pivot = pivot.rename(columns={"period": "날짜"})
            return pivot

        else:
            return res

    def datalab_shopping_category_keyword_device(self, **kwargs):
        """
        쇼핑인사이트 키워드 기기별 트렌드 조회
        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/datalab/shopping/shopping.md
        """
        url = "https://openapi.naver.com/v1/datalab/shopping/category/keyword/device"
        data = {}
        for k, v in kwargs.items():
            data[k] = v
        data = json.dumps(data, ensure_ascii=False).encode("utf-8")
        res = requests.post(url, data=data, headers=self.headers)

        if res.status_code == 200:
            data = res.json()['results']
            df = pd.DataFrame(data[0]['data'])
            df = df[['group', 'period', 'ratio']]
            pivot = pd.pivot(df, index='period', columns=[
                             'group'], values='ratio').reset_index()
            pivot.columns.name = None
            pivot = pivot.rename(columns={"period": "날짜"})
            return pivot

        else:
            return res

    def datalab_shopping_category_keyword_gender(self, **kwargs):
        """
        쇼핑인사이트 키워드 성별 트렌드 조회
        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/datalab/shopping/shopping.md
        """
        url = "https://openapi.naver.com/v1/datalab/shopping/category/keyword/gender"
        data = {}
        for k, v in kwargs.items():
            data[k] = v
        data = json.dumps(data, ensure_ascii=False).encode("utf-8")
        res = requests.post(url, data=data, headers=self.headers)

        if res.status_code == 200:
            data = res.json()['results']
            df = pd.DataFrame(data[0]['data'])
            df = df[['group', 'period', 'ratio']]
            pivot = pd.pivot(df, index='period', columns=[
                             'group'], values='ratio').reset_index()
            pivot.columns.name = None
            pivot = pivot.rename(columns={"period": "날짜"})
            return pivot

        else:
            return res

    def datalab_shopping_category_keyword_age(self, **kwargs):
        """
        쇼핑인사이트 키워드 연령별 트렌드 조회
        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/datalab/shopping/shopping.md
        """
        url = "https://openapi.naver.com/v1/datalab/shopping/category/keyword/age"
        data = {}
        for k, v in kwargs.items():
            data[k] = v
        data = json.dumps(data, ensure_ascii=False).encode("utf-8")
        res = requests.post(url, data=data, headers=self.headers)

        if res.status_code == 200:
            data = res.json()['results']
            df = pd.DataFrame(data[0]['data'])
            df = df[['group', 'period', 'ratio']]
            pivot = pd.pivot(df, index='period', columns=[
                             'group'], values='ratio').reset_index()
            pivot.columns.name = None
            pivot = pivot.rename(columns={"period": "날짜"})
            return pivot

        else:
            return res

    def util_shorturl(self, url):
        """
        단축 URL 요청(JSON)
        - API 레퍼런스: https://developers.naver.com/docs/utils/shortenurl/
        """
        req_url = f"https://openapi.naver.com/v1/util/shorturl?url={url}"
        res = requests.get(req_url, headers=self.headers)
        if res.status_code == 200:
            return res.json()
        else:
            return res

    def papago_n2mt(self, **kwargs):
        """
        Papago 번역
        - API 레퍼런스: https://developers.naver.com/docs/papago/papago-nmt-api-reference.md
        """
        url = "https://openapi.naver.com/v1/papago/n2mt"
        data = {}
        for k, v in kwargs.items():
            data[k] = v
        data = json.dumps(data, ensure_ascii=False).encode("utf-8")
        res = requests.post(url, data=data, headers=self.headers)
        if res.status_code == 200:
            return res.json()['message']['result']['translatedText']
        else:
            return res

    def krdict_romanization(self, **kwargs):
        """
        한글 인명-로마자 변환
        - API 레퍼런스: https://developers.naver.com/docs/papago/papago-romanization-api-reference.md
        """
        url = "https://openapi.naver.com/v1/krdict/romanization?"
        for k, v in kwargs.items():
            url += f"{k}={v}&"
        res = requests.get(url, headers=self.headers)
        if res.status_code == 200:
            return pd.DataFrame(res.json()['aResult'][0]['aItems'])
        else:
            return res

    def search_blog(self, **kwargs):
        """
        검색 블로그
        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/search/blog/blog.md
        """
        url = "https://openapi.naver.com/v1/search/blog.json?"
        for k, v in kwargs.items():
            url += f"{k}={v}&"
        res = requests.get(url, headers=self.headers)
        if res.status_code == 200:
            return pd.DataFrame(res.json()['items'])
        else:
            return res

    def search_news(self, **kwargs):
        """
        검색 뉴스
        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/search/news/news.md
        """
        url = "https://openapi.naver.com/v1/search/news.json?"
        for k, v in kwargs.items():
            url += f"{k}={v}&"
        res = requests.get(url, headers=self.headers)
        if res.status_code == 200:
            return pd.DataFrame(res.json()['items'])
        else:
            return res

    def search_shop(self, **kwargs):
        """
        검색 쇼핑
        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/search/shopping/shopping.md
        """
        url = "https://openapi.naver.com/v1/search/shop.json?"
        for k, v in kwargs.items():
            url += f"{k}={v}&"
        res = requests.get(url, headers=self.headers)
        if res.status_code == 200:
            return pd.DataFrame(res.json()['items'])
        else:
            return res

    def search_local(self, **kwargs):
        """
        검색 지역
        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/search/local/local.md
        """
        url = "https://openapi.naver.com/v1/search/local.json?"
        for k, v in kwargs.items():
            url += f"{k}={v}&"
        res = requests.get(url, headers=self.headers)
        if res.status_code == 200:
            return pd.DataFrame(res.json()['items'])
        else:
            return res


class NaverCloudPlatform:
    """
    네이버 클라우드 플랫폼 OPEN API 클래스
    """
    def __init__(self, client_id, client_secret):
        """
        API 인증 정보 초기화
        """
        self.headers = {
            "X-NCP-APIGW-API-KEY-ID": client_id,
            "X-NCP-APIGW-API-KEY": client_secret,
        }
        
    def geocoding(self, query):
        """
        지오코딩 API
        - API 레퍼런스: https://api.ncloud-docs.com/docs/ai-naver-mapsgeocoding
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
        - API 레퍼런스: https://api.ncloud-docs.com/docs/ai-naver-mapsreversegeocoding
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
        - API 레퍼런스: https://api.ncloud-docs.com/docs/ai-naver-mapsdirections
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
        - API 레퍼런스: https://api.ncloud-docs.com/docs/ai-naver-mapsdirections15
        """
        url = f"https://naveropenapi.apigw.ntruss.com/map-direction-15/v1/driving?"
        for k, v in kwargs.items():
            url += f"{k}={v}&"
        res = requests.get(url, headers=self.headers)
        if res.status_code == 200:
            return res.json()
        else:
            return res


class Map:
    """
    네이버 지도 API 클래스
    """
    def _init_(self):
        pass

    def transit_directions_point_to_point(self, **kwargs):
        """
        네이버 지도 길찾기 대중교통 API
        """
        url = "https://map.naver.com/v5/api/transit/directions/point-to-point?"
        params = {
            "crs": "EPSG:4326",
            "mode": "TIME",
            "lang": "ko",
            "includeDetailOperation": "true",
        }
        kwargs.update(params)
        for k, v in kwargs.items():
            url += f"{k}={v}&"
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
        else:
            return res