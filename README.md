# ODS-to-CSV

LibreOffice .ods 스프레드시트 파일을 읽어 모든 시트를 일괄적으로
`{파일 이름}-{시트 이름}.csv` 형식으로 추출해 줍니다.

## 사용법

Python3.12에서 작성했습니다.

설치

```
git clone https://github.com/chwnam/ods-to-csv.git
cd ods-to-csv
python3 -m venv ./.venv
source ./.venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

사용하기 


```
# ~/.bash_aliases

alias ods-to-csv='/path/to/ods-to-csv/.venv/bin/python /path/to/ods-to-csv/convert.py'
```
