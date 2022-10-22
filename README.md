<div align="center">

<b>네이버 데이터 조회를 위한 오픈소스 로우코드 파이썬 라이브러리</b><br>
<b>🚀`pip install PyNaver --upgrade`</b>

[![PyPI Latest Release](https://img.shields.io/pypi/v/pynaver.svg)](https://pypi.org/project/pynaver/)
[![License](https://img.shields.io/pypi/l/ansicolortags.svg)](https://img.shields.io/pypi/l/ansicolortags.svg)
[![Python](https://img.shields.io/badge/Official-Docs-tomato)](https://wooiljeong.github.io/PyNaver/)
![](https://img.shields.io/badge/API-NAVER-green.svg)  
[![오픈채팅](https://img.shields.io/badge/오픈채팅-Q&A-yellow?logo=KakaoTalk)](https://open.kakao.com/o/gh1N1kJe)

<br>

<div align="left">


## PyNaver

PyNaver는 [naver developers](https://developers.naver.com/), [naver cloud platform](https://www.ncloud.com/)에서 제공하는 오픈 API를 이용할 수 있는 Python Client 입니다. PyNaver를 정상적으로 이용하기 위해서는 naver developers와 naver cloud platform의 애플리케이션 정보(Client ID, Client Secret)가 필요합니다.

<br>

## 설치 방법

- Windows: CMD(명령 프롬프트)를 열어 아래 Shell 명령어를 입력
- Mac: Terminal(터미널)을 열어 아래 Shell 명령어를 입력

```bash
pip install PyNaver
```

<br>

## 사용 방법

더 많은 정보는 [하단](#참고)의 **튜토리얼**을 참고하면 됩니다.

### (예시) 통합 검색어 트렌드 API
```python
from PyNaver import Naver

# 애플리케이션 인증 정보
client_id = ""
client_secret = ""

# 네이버 API 인스턴스 생성
naver = Naver(client_id, client_secret)

# 파라미터
startDate = "2022-01-01"
endDate = "2022-08-31"
timeUnit = "date"
keywordGroups = [
    {
        "groupName": "미국",
        "keywords": ["나스닥","NASDAQ","S&P500"]
    },

    {
        "groupName": "한국",
        "keywords": ["코스피","코스닥"]
    },
]

# 실행
df = naver.datalab_search(startDate=startDate,
                          endDate=endDate,
                          timeUnit=timeUnit,
                          keywordGroups=keywordGroups)
```


### (예시) 지오코딩 API

```python
from PyNaver import NaverCloudPlatform

# 애플리케이션 인증 정보
client_id = ""
client_secret = ""

# 네이버 클라우드 플랫폼 API 인스턴스 생성
ncp = NaverCloudPlatform(client_id, client_secret)

# 주소
query = "서초동 1303-22"

# 실행
res = ncp.geocoding(query)
```

<br>

## 참고

- **튜토리얼**  
    - [(블로그) PyNaver - 파이썬 네이버 API 라이브러리](https://wooiljeong.github.io/python/pynaver/)

- **공식문서**
  - [Docs](https://wooiljeong.github.io/PyNaver/)

- **문의**  
  - **이메일**: wooil@kakao.com  
  - **카카오톡 오픈채팅방**: [접속 링크](https://open.kakao.com/o/gh1N1kJe)

<br>

## 기여자

<a href="https://github.com/wooiljeong/publicdatareader/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=wooiljeong/publicdatareader" />
</a>

<br>

<div align=center>

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FWooilJeong%2FPyNaver&count_bg=%2300CBFF&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

</div>
