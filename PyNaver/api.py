import json
import requests
import pandas as pd


class Naver:
    """
    네이버 OPEN API 클래스

    Parameters
    ----------
    client_id : string
        네이버 개발자 센터에서 발급받은 클라이언트 ID
    client_secret : string
        네이버 개발자 센터에서 발급받은 클라이언트 SECRET
    """

    def __init__(self, client_id, client_secret):
        self.headers = {
            "X-Naver-Client-Id": client_id,
            "X-Naver-Client-Secret": client_secret,
            "Content-Type": "application/json",
        }

    def datalab_search(self, startDate, endDate, timeUnit, keywordGroups, **kwargs):
        """
        네이버 통합 검색어 트렌드 조회

        Parameters
        ----------
        startDate : string
            조회 시작일
        endDate : string
            조회 종료일
        timeUnit : string
            조회 기간
        keywordGroups : list
            키워드 그룹
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        DataFrame
            키워드 그룹별 트렌드

        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/datalab/search/search.md
        """
        url = "https://openapi.naver.com/v1/datalab/search"
        data = {
            "startDate": startDate,
            "endDate": endDate,
            "timeUnit": timeUnit,
            "keywordGroups": keywordGroups,
        }
        data.update(kwargs)
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

    def datalab_shopping_categories(self, startDate, endDate, timeUnit, category, **kwargs):
        """
        쇼핑인사이트 분야별 트렌드 조회

        Parameters
        ----------
        startDate : string
            조회 시작일
        endDate : string
            조회 종료일
        timeUnit : string
            구간 단위
        category : list
            분야
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        DataFrame
            분야별 트렌드

        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/datalab/shopping/shopping.md
        """
        url = "https://openapi.naver.com/v1/datalab/shopping/categories"
        data = {
            "startDate": startDate,
            "endDate": endDate,
            "timeUnit": timeUnit,
            "category": category,
        }
        data.update(kwargs)
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

    def datalab_shopping_category_device(self, startDate, endDate, timeUnit, category, **kwargs):
        """
        쇼핑인사이트 분야 내 기기별 트렌드 조회

        Parameters
        ----------
        startDate : string
            조회 시작일
        endDate : string
            조회 종료일
        timeUnit : string
            구간 단위
        category : list
            분야
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        DataFrame
            분야 내 기기별 트렌드

        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/datalab/shopping/shopping.md
        """
        url = "https://openapi.naver.com/v1/datalab/shopping/category/device"
        data = {
            "startDate": startDate,
            "endDate": endDate,
            "timeUnit": timeUnit,
            "category": category,
        }
        data.update(kwargs)
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

    def datalab_shopping_category_gender(self, startDate, endDate, timeUnit, category, **kwargs):
        """
        쇼핑인사이트 분야 내 성별 트렌드 조회

        Parameters
        ----------
        startDate : string
            조회 시작일
        endDate : string
            조회 종료일
        timeUnit : string
            구간 단위
        category : list
            분야
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        DataFrame
            분야 내 성별 트렌드

        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/datalab/shopping/shopping.md
        """
        url = "https://openapi.naver.com/v1/datalab/shopping/category/gender"
        data = {
            "startDate": startDate,
            "endDate": endDate,
            "timeUnit": timeUnit,
            "category": category,
        }
        data.update(kwargs)
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

    def datalab_shopping_category_age(self, startDate, endDate, timeUnit, category, **kwargs):
        """
        쇼핑인사이트 분야 내 연령별 트렌드 조회

        Parameters
        ----------
        startDate : string
            조회 시작일
        endDate : string
            조회 종료일
        timeUnit : string
            구간 단위
        category : list
            분야
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        DataFrame
            분야 내 연령별 트렌드

        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/datalab/shopping/shopping.md
        """
        url = "https://openapi.naver.com/v1/datalab/shopping/category/age"
        data = {
            "startDate": startDate,
            "endDate": endDate,
            "timeUnit": timeUnit,
            "category": category,
        }
        data.update(kwargs)
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

    def datalab_shopping_category_keywords(self, startDate, endDate, timeUnit, category, keyword, **kwargs):
        """
        쇼핑인사이트 키워드별 트렌드 조회

        Parameters
        ----------
        startDate : string
            조회 시작일
        endDate : string
            조회 종료일
        timeUnit : string
            구간 단위
        category : list
            분야
        keyword : list
            키워드
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        DataFrame
            키워드별 트렌드

        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/datalab/shopping/shopping.md
        """
        url = "https://openapi.naver.com/v1/datalab/shopping/category/keywords"
        data = {
            "startDate": startDate,
            "endDate": endDate,
            "timeUnit": timeUnit,
            "category": category,
            "keyword": keyword,
        }
        data.update(kwargs)
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

    def datalab_shopping_category_keyword_device(self, startDate, endDate, timeUnit, category, keyword, **kwargs):
        """
        쇼핑인사이트 키워드 기기별 트렌드 조회

        Parameters
        ----------
        startDate : string
            조회 시작일
        endDate : string
            조회 종료일
        timeUnit : string
            구간 단위
        category : list
            분야
        keyword : list
            키워드
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        DataFrame
            키워드 기기별 트렌드

        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/datalab/shopping/shopping.md
        """
        url = "https://openapi.naver.com/v1/datalab/shopping/category/keyword/device"
        data = {
            "startDate": startDate,
            "endDate": endDate,
            "timeUnit": timeUnit,
            "category": category,
            "keyword": keyword,
        }
        data.update(kwargs)
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

    def datalab_shopping_category_keyword_gender(self, startDate, endDate, timeUnit, category, keyword, **kwargs):
        """
        쇼핑인사이트 키워드 성별 트렌드 조회

        Parameters
        ----------
        startDate : string
            조회 시작일
        endDate : string
            조회 종료일
        timeUnit : string
            구간 단위
        category : list
            분야
        keyword : list
            키워드
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        DataFrame
            키워드 성별 트렌드

        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/datalab/shopping/shopping.md
        """
        url = "https://openapi.naver.com/v1/datalab/shopping/category/keyword/gender"
        data = {
            "startDate": startDate,
            "endDate": endDate,
            "timeUnit": timeUnit,
            "category": category,
            "keyword": keyword,
        }
        data.update(kwargs)
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

    def datalab_shopping_category_keyword_age(self, startDate, endDate, timeUnit, category, keyword, **kwargs):
        """
        쇼핑인사이트 키워드 연령별 트렌드 조회

        Parameters
        ----------
        startDate : string
            조회 시작일
        endDate : string
            조회 종료일
        timeUnit : string
            구간 단위
        category : list
            분야
        keyword : list
            키워드
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        DataFrame
            키워드 연령별 트렌드

        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/datalab/shopping/shopping.md
        """
        url = "https://openapi.naver.com/v1/datalab/shopping/category/keyword/age"
        data = {
            "startDate": startDate,
            "endDate": endDate,
            "timeUnit": timeUnit,
            "category": category,
            "keyword": keyword,
        }
        data.update(kwargs)
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

        Parameters
        ----------
        url : string
            원본 URL

        Returns
        -------
        dict
            단축 URL

        - API 레퍼런스: https://developers.naver.com/docs/utils/shortenurl/
        """
        req_url = f"https://openapi.naver.com/v1/util/shorturl"
        params = {
            "url": url
        }
        res = requests.get(req_url, headers=self.headers, params=params)
        if res.status_code == 200:
            return res.json()
        else:
            return res

    def papago_n2mt(self, source, target, text, **kwargs):
        """
        Papago 번역

        Parameters
        ----------
        source : string
            번역할 언어
        target : string
            번역될 언어
        text : string
            번역할 텍스트
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        string
            번역된 텍스트

        - API 레퍼런스: https://developers.naver.com/docs/papago/papago-nmt-api-reference.md
        """
        url = "https://openapi.naver.com/v1/papago/n2mt"
        data = {
            "source": source,
            "target": target,
            "text": text
        }
        data.update(kwargs)
        data = json.dumps(data, ensure_ascii=False).encode("utf-8")
        res = requests.post(url, data=data, headers=self.headers)
        if res.status_code == 200:
            return res.json()['message']['result']['translatedText']
        else:
            return res

    def krdict_romanization(self, query, **kwargs):
        """
        한글 인명-로마자 변환

        Parameters
        ----------
        query : string
            변환할 한글 인명
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        DataFrame
            변환된 로마자

        - API 레퍼런스: https://developers.naver.com/docs/papago/papago-romanization-api-reference.md
        """
        url = "https://openapi.naver.com/v1/krdict/romanization"
        params = {
            "query": query
        }
        params.update(kwargs)
        res = requests.get(url, headers=self.headers, params=params)
        if res.status_code == 200:
            return pd.DataFrame(res.json()['aResult'][0]['aItems'])
        else:
            return res

    def search_blog(self, query, **kwargs):
        """
        검색 블로그

        Parameters
        ----------
        query : string
            검색어
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        DataFrame
            검색 결과

        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/search/blog/blog.md
        """
        url = "https://openapi.naver.com/v1/search/blog.json"
        params = {
            "query": query
        }
        params.update(kwargs)
        res = requests.get(url, headers=self.headers, params=params)
        if res.status_code == 200:
            return pd.DataFrame(res.json()['items'])
        else:
            return res

    def search_news(self, query, **kwargs):
        """
        검색 뉴스

        Parameters
        ----------
        query : string
            검색어
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        DataFrame
            검색 결과

        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/search/news/news.md
        """
        url = "https://openapi.naver.com/v1/search/news.json"
        params = {
            "query": query
        }
        params.update(kwargs)
        res = requests.get(url, headers=self.headers, params=params)
        if res.status_code == 200:
            return pd.DataFrame(res.json()['items'])
        else:
            return res

    def search_book(self, query, **kwargs):
        """
        검색 책

        Parameters
        ----------
        query : string
            검색어
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        DataFrame
            검색 결과

        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/search/book/book.md#%EC%B1%85
        """
        url = "https://openapi.naver.com/v1/search/book.json"
        params = {
            "query": query
        }
        params.update(kwargs)
        res = requests.get(url, headers=self.headers, params=params)
        if res.status_code == 200:
            return pd.DataFrame(res.json()['items'])
        else:
            return res

    def search_encyc(self, query, **kwargs):
        """
        검색 백과사전

        Parameters
        ----------
        query : string
            검색어
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        DataFrame
            검색 결과

        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/search/encyclopedia/encyclopedia.md
        """
        url = "https://openapi.naver.com/v1/search/encyc.json"
        params = {
            "query": query
        }
        params.update(kwargs)
        res = requests.get(url, headers=self.headers, params=params)
        if res.status_code == 200:
            return pd.DataFrame(res.json()['items'])
        else:
            return res

    def search_movie(self, query, **kwargs):
        """
        검색 영화

        Parameters
        ----------
        query : string
            검색어
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        DataFrame
            검색 결과

        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/search/movie/movie.md
        """
        url = "https://openapi.naver.com/v1/search/movie.json"
        params = {
            "query": query
        }
        params.update(kwargs)
        res = requests.get(url, headers=self.headers, params=params)
        if res.status_code == 200:
            return pd.DataFrame(res.json()['items'])
        else:
            return res

    def search_cafearticle(self, query, **kwargs):
        """
        검색 카페글

        Parameters
        ----------
        query : string
            검색어
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        DataFrame
            검색 결과

        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/search/cafearticle/cafearticle.md
        """
        url = "https://openapi.naver.com/v1/search/cafearticle.json"
        params = {
            "query": query
        }
        params.update(kwargs)
        res = requests.get(url, headers=self.headers, params=params)
        if res.status_code == 200:
            return pd.DataFrame(res.json()['items'])
        else:
            return res

    def search_kin(self, query, **kwargs):
        """
        검색 지식인

        Parameters
        ----------
        query : string
            검색어
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        DataFrame
            검색 결과

        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/search/kin/kin.md
        """
        url = "https://openapi.naver.com/v1/search/kin.json"
        params = {
            "query": query
        }
        params.update(kwargs)
        res = requests.get(url, headers=self.headers, params=params)
        if res.status_code == 200:
            return pd.DataFrame(res.json()['items'])
        else:
            return res

    def search_webkr(self, query, **kwargs):
        """
        검색 웹문서

        Parameters
        ----------
        query : string
            검색어
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        DataFrame
            검색 결과

        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/search/web/web.md
        """
        url = "https://openapi.naver.com/v1/search/webkr.json"
        params = {
            "query": query
        }
        params.update(kwargs)
        res = requests.get(url, headers=self.headers, params=params)
        if res.status_code == 200:
            return pd.DataFrame(res.json()['items'])
        else:
            return res

    def search_image(self, query, **kwargs):
        """
        검색 이미지

        Parameters
        ----------
        query : string
            검색어
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        DataFrame
            검색 결과

        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/search/image/image.md
        """
        url = "https://openapi.naver.com/v1/search/image"
        params = {
            "query": query
        }
        params.update(kwargs)
        res = requests.get(url, headers=self.headers, params=params)
        if res.status_code == 200:
            return pd.DataFrame(res.json()['items'])
        else:
            return res

    def search_local(self, query, **kwargs):
        """
        검색 지역

        Parameters
        ----------
        query : string
            검색어
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        DataFrame
            검색 결과

        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/search/local/local.md
        """
        url = "https://openapi.naver.com/v1/search/local.json"
        params = {
            "query": query
        }
        params.update(kwargs)
        res = requests.get(url, headers=self.headers, params=params)
        if res.status_code == 200:
            return pd.DataFrame(res.json()['items'])
        else:
            return res

    def search_shop(self, query, **kwargs):
        """
        검색 쇼핑

        Parameters
        ----------
        query : string
            검색어
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        DataFrame
            검색 결과

        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/search/shopping/shopping.md
        """
        url = "https://openapi.naver.com/v1/search/shop.json"
        params = {
            "query": query
        }
        params.update(kwargs)
        res = requests.get(url, headers=self.headers, params=params)
        if res.status_code == 200:
            return pd.DataFrame(res.json()['items'])
        else:
            return res

    def search_doc(self, query, **kwargs):
        """
        검색 전문자료

        Parameters
        ----------
        query : string
            검색어
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        DataFrame
            검색 결과

        - API 레퍼런스: https://developers.naver.com/docs/serviceapi/search/doc/doc.md
        """
        url = "https://openapi.naver.com/v1/search/doc.json"
        params = {
            "query": query
        }
        params.update(kwargs)
        res = requests.get(url, headers=self.headers, params=params)
        if res.status_code == 200:
            return pd.DataFrame(res.json()['items'])
        else:
            return res


class NaverCloudPlatform:
    """
    네이버 클라우드 플랫폼 OPEN API 클래스

    Parameters
    ----------
    client_id : string
        네이버 클라우드 플랫폼에서 발급받은 클라이언트 ID
    client_secret : string
        네이버 클라우드 플랫폼에서 발급받은 클라이언트 SECRET
    """

    def __init__(self, client_id, client_secret):
        self.headers = {
            "X-NCP-APIGW-API-KEY-ID": client_id,
            "X-NCP-APIGW-API-KEY": client_secret,
        }

    def geocoding(self, query, **kwargs):
        """
        지오코딩 API

        Parameters
        ----------
        query : string
            검색어
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        dict
            검색 결과

        - API 레퍼런스: https://api.ncloud-docs.com/docs/ai-naver-mapsgeocoding
        """
        url = f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
        params = {
            "query": query
        }
        params.update(kwargs)
        res = requests.get(url, headers=self.headers, params=params)
        if res.status_code == 200:
            return res.json()
        else:
            return res

    def reverse_geocoding(self, coords, **kwargs):
        """
        리버스 지오코딩 API

        Parameters
        ----------
        coords : string
            좌표
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        dict
            검색 결과

        - API 레퍼런스: https://api.ncloud-docs.com/docs/ai-naver-mapsreversegeocoding
        """
        params = {
            "coords": coords,
            "output": "json",
            "orders": "addr",
        }
        params.update(kwargs)
        url = f"https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc"
        res = requests.get(url, headers=self.headers, params=params)
        if res.status_code == 200:
            return res.json()
        else:
            return res

    def directions5(self, start, goal, **kwargs):
        """
        Directions5 API

        Parameters
        ----------
        start : string
            출발지 좌표
        goal : string
            도착지 좌표
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        dict
            검색 결과

        - API 레퍼런스: https://api.ncloud-docs.com/docs/ai-naver-mapsdirections
        """
        url = f"https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving"
        params = {
            "start": start,
            "goal": goal,
        }
        params.update(kwargs)
        res = requests.get(url, headers=self.headers, params=params)
        if res.status_code == 200:
            return res.json()
        else:
            return res

    def directions15(self, start, goal, **kwargs):
        """
        Directions15 API

        Parameters
        ----------
        start : string
            출발지 좌표
        goal : string
            도착지 좌표
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        dict
            검색 결과

        - API 레퍼런스: https://api.ncloud-docs.com/docs/ai-naver-mapsdirections15
        """
        url = f"https://naveropenapi.apigw.ntruss.com/map-direction-15/v1/driving"
        params = {
            "start": start,
            "goal": goal,
        }
        params.update(kwargs)
        res = requests.get(url, headers=self.headers, params=params)
        if res.status_code == 200:
            return res.json()
        else:
            return res

    def clova_summary(self,
                      content=None,
                      title=None,
                      language="ko",
                      model="general",
                      tone=0,
                      summaryCount=3,
                      ):
        """
        Clova Summary API

        Parameters
        ----------
        content : string, REQUIRED
            요약할 내용
        title : string, OPTIONAL
            요약할 제목
        language : string, REQUIRED (ko: 한국어, ja: 일본어) (미지정 시 기본 값: ko)
            언어
        model : string, OPTIONAL
            모델 (general: 일반 문서 요약, news: 뉴스 요약) (미지정 시 기본 값: general)
        tone : int, OPTIONAL
            톤 (0: 원문의 어투를 유지, 1: 해요체, 2: 정중체, 3: 명사형 종결체) (미지정 시 기본 값: 0)
        summaryCount : int, OPTIONAL
            요약문 개수 (미지정 시 기본 값: 3)
        """
        url = "https://naveropenapi.apigw.ntruss.com/text-summary/v1/summarize"
        params = {
            "document": {
                "content": content,
                "title": title,
            },
            "option": {
                "language": language,
                "model": model,
                "tone": tone,
                "summaryCount": summaryCount,
            },
        }
        headers = self.headers.copy()
        headers.update({
            "Content-Type": "application/json",
        })
        res = requests.post(url, headers=headers, json=params)
        if res.status_code == 200:
            return res.json()
        else:
            return res


class Map:
    """
    네이버 지도 API 클래스
    """

    def __init__(self):
        pass

    def search(self, query, **kwargs):
        """
        네이버 지도 검색

        Parameters
        ----------
        query : string
            검색어
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        dict
            검색 결과
        """
        url = "https://map.naver.com/v5/api/search"
        headers = {
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }
        params = {
            "query": query,
            "type": "all",
            "lang": "ko",
        }
        params.update(kwargs)
        res = requests.get(url, headers=headers, params=params)
        return res.json()

    def sites_summary(self, site_id, **kwargs):
        """
        네이버 지도 장소 요약

        Parameters
        ----------
        site_id : string
            장소 ID
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        dict
            검색 결과
        """
        url = f"https://map.naver.com/v5/api/sites/summary/{site_id}"
        headers = {
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }
        params = {
            "lang": "ko",
        }
        params.update(kwargs)
        res = requests.get(url, headers=headers, params=params)
        return res.json()

    def transit_directions_point_to_point(self, start, goal, **kwargs):
        """
        네이버 지도 길찾기 대중교통 API

        Parameters
        ----------
        start : string
            출발지 좌표
        goal : string
            도착지 좌표
        kwargs : dict
            그 외 파라미터

        Returns
        -------
        dict
            검색 결과
        """
        url = "https://map.naver.com/v5/api/transit/directions/point-to-point"
        params = {
            "start": start,
            "goal": goal,
            "crs": "EPSG:4326",
            "mode": "TIME",
            "lang": "ko",
            "includeDetailOperation": "true",
        }
        params.update(kwargs)
        res = requests.get(url, params=params)
        return res.json()
