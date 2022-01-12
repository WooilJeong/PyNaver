# PyNaver

![](https://img.shields.io/badge/python-3.8-blue.svg)
![](https://img.shields.io/badge/pandas-1.3.5-red.svg)
![](https://img.shields.io/badge/api-naver-green.svg)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FWooilJeong%2FPyNaver&count_bg=%2300CBFF&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
[![Linkedin Badge](https://img.shields.io/badge/-WooilJeong-blue?style=plastic&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/wooil/)](https://www.linkedin.com/in/wooil/) 

## 소개

PyNaver는 [naver developers](https://developers.naver.com/)에서 제공하는 오픈 API를 이용할 수 있는 Python Client 입니다. PyNaver를 정상적으로 이용하기 위해서는 naver developers 애플리케이션 정보(Client ID, Client Secret)가 필요합니다.

## 설치

```bash
pip install PyNaver
```

## 예제

```python
from PyNaver import Datalab
from config import Config

config = Config()
```


```python
# 네이버 데이터랩 API 클라이언트 ID, SECRET
client_id = config.OPEN_API['naver']['client_id']
client_secret = config.OPEN_API['naver']['client_secret']
```


```python
# 네이버 데이터랩 API 세션 정의
DL = Datalab(client_id, client_secret)
```


```python
# 검색어 그룹 세트 정의하기
keyword_group_set = {
    'keyword_group_1': {'groupName': "애플", 'keywords': ["애플","Apple","AAPL"]},
    'keyword_group_2': {'groupName': "아마존", 'keywords': ["아마존","Amazon","AMZN"]},
    'keyword_group_3': {'groupName': "구글", 'keywords': ["구글","Google","GOOGL"]},
    'keyword_group_4': {'groupName': "테슬라", 'keywords': ["테슬라","Tesla","TSLA"]},
    'keyword_group_5': {'groupName': "페이스북", 'keywords': ["페이스북","Facebook","FB"]}
}
```


```python
# 요청 파라미터 설정
startDate = "2021-01-01"
endDate = "2021-12-31"
timeUnit = 'date'
device = ''
ages = []
gender = ''

# 검색어 그룹 세트 등록하기
DL.add_keyword_groups(keyword_group_set['keyword_group_1'])
DL.add_keyword_groups(keyword_group_set['keyword_group_2'])
DL.add_keyword_groups(keyword_group_set['keyword_group_3'])
DL.add_keyword_groups(keyword_group_set['keyword_group_4'])
DL.add_keyword_groups(keyword_group_set['keyword_group_5'])

# 결과 데이터를 DataFrame으로 조회하기
df = DL.get_data(startDate, endDate, timeUnit, device, ages, gender)
df
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>날짜</th>
      <th>애플</th>
      <th>아마존</th>
      <th>구글</th>
      <th>테슬라</th>
      <th>페이스북</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2021-01-01</td>
      <td>10.22685</td>
      <td>2.71217</td>
      <td>81.27609</td>
      <td>6.30002</td>
      <td>38.51378</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2021-01-02</td>
      <td>10.28149</td>
      <td>3.14536</td>
      <td>85.91210</td>
      <td>5.64883</td>
      <td>34.69233</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2021-01-03</td>
      <td>10.23001</td>
      <td>3.13477</td>
      <td>91.73209</td>
      <td>6.96682</td>
      <td>34.85066</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2021-01-04</td>
      <td>13.48651</td>
      <td>3.64769</td>
      <td>97.28281</td>
      <td>9.36343</td>
      <td>36.27848</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2021-01-05</td>
      <td>15.03680</td>
      <td>3.70047</td>
      <td>97.39134</td>
      <td>12.24063</td>
      <td>35.20878</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>360</th>
      <td>2021-12-27</td>
      <td>7.39872</td>
      <td>2.34624</td>
      <td>81.16979</td>
      <td>4.71256</td>
      <td>21.63808</td>
    </tr>
    <tr>
      <th>361</th>
      <td>2021-12-28</td>
      <td>8.32198</td>
      <td>2.56219</td>
      <td>80.33258</td>
      <td>6.80532</td>
      <td>21.85681</td>
    </tr>
    <tr>
      <th>362</th>
      <td>2021-12-29</td>
      <td>8.02667</td>
      <td>2.82813</td>
      <td>80.21513</td>
      <td>6.52192</td>
      <td>21.60685</td>
    </tr>
    <tr>
      <th>363</th>
      <td>2021-12-30</td>
      <td>7.69216</td>
      <td>2.42225</td>
      <td>77.53213</td>
      <td>5.97313</td>
      <td>21.34798</td>
    </tr>
    <tr>
      <th>364</th>
      <td>2021-12-31</td>
      <td>6.75645</td>
      <td>2.10874</td>
      <td>71.91340</td>
      <td>5.12922</td>
      <td>21.17217</td>
    </tr>
  </tbody>
</table>
<p>365 rows × 6 columns</p>
</div>


