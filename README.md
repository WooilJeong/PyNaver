<div align="center">

<b>네이버 API를 사용하기 위한 오픈소스 파이썬 라이브러리</b><br>
<b>🚀`pip install PyNaver --upgrade`</b>

[![PyPI Latest Release](https://img.shields.io/pypi/v/pynaver.svg)](https://pypi.org/project/pynaver/)
[![License](https://img.shields.io/pypi/l/ansicolortags.svg)](https://img.shields.io/pypi/l/ansicolortags.svg)
[![Python](https://img.shields.io/badge/Official-Docs-tomato)](https://wooiljeong.github.io/PyNaver/)
![](https://img.shields.io/badge/API-NAVER-green.svg)  
[![오픈채팅](https://img.shields.io/badge/오픈채팅-Q&A-yellow?logo=KakaoTalk)](https://open.kakao.com/o/gh1N1kJe)

<br>

<div align="left">


## PyNaver

**PyNaver**는 [NAVER Developers](https://developers.naver.com/)와 [NAVER CLOUD PLATFORM](https://www.ncloud.com/)에서 제공하는 다양한 API를 파이썬으로 쉽게 사용할 수 있도록 해주는 라이브러리입니다. 그래서 PyNaver를 사용하면 **NAVER Developers**의 검색 API를 통해 웹문서, 이미지, 쇼핑, 전문자료 등을 검색할 수 있고, 파파고 API를 사용하면 Papago 번역, 한글인명-로마자 변환 기능을 이용할 수 있습니다. 단축 URL API를 사용하면 원래의 URL을 짧게 줄일 수 있고, **NAVER CLOUD PLATFORM**의 지오코딩 API를 이용하면 주소로 좌표 정보를 알아낼 수 있고, 리버스 지오코딩 API를 이용하면 좌표로 주소 정보를 알아낼 수 있습니다. 또한, Direction 5 및 Direction 15 API를 사용하면 출발지/목적지 정보에 따라 경로 관련 정보를 알아낼 수 있습니다.

<br>

## 설치 방법

1. 운영체제(OS)에 따라 아래 중 하나를 선택합니다.

- Windows: CMD(명령 프롬프트) 실행
- Mac: Terminal(터미널) 실행

2. 아래 Shell 명령어를 입력 후 실행합니다.

```bash
pip install PyNaver --upgrade
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
api = Naver(client_id, client_secret)

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
df = api.datalab_search(startDate, endDate, timeUnit, keywordGroups)
```


### (예시) 지오코딩 API

```python
from PyNaver import NaverCloudPlatform

# 애플리케이션 인증 정보
client_id = ""
client_secret = ""

# 네이버 클라우드 플랫폼 API 인스턴스 생성
api = NaverCloudPlatform(client_id, client_secret)

# 주소
query = "서초동 1303-22"

# 실행
res = api.geocoding(query)
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

<a href="https://github.com/wooiljeong/pynaver/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=wooiljeong/pynaver" />
</a>

<br>

<div align=center>

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FWooilJeong%2FPyNaver&count_bg=%2300CBFF&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

</div>
