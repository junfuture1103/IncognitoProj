import pandas as pd

# 데이터를 로드합니다. 데이터 파일의 경로를 적절하게 지정해야 합니다.
data = pd.read_csv('경영진정보_train.csv', usecols=['cmpCd', 'mgrNm', 'pstnCd', 'pstnCdNm', 'chrgTaskNm', 'rgstStat', 'rgstStatNm', 'mgrEnm', 'brthDate', 'zip', 'adr', 'dtlAdr', 'eduCont', 'crrCont'])

# 'crrCont' 컬럼이 NaN 값을 가진 행을 제거합니다.
data = data.dropna(subset=['crrCont'])

# 중복 행을 제거합니다.
data = data.drop_duplicates()

# 모든 칼럼에 대해 NaN을 빈 문자열('')로 대체합니다.
for col in data.columns:
    data[col] = data[col].astype(str).fillna('')
    data[col] = data[col].replace('nan', '')

# 각 열의 데이터를 공백으로 합칩니다.
data['경영진 정보'] = data['pstnCdNm'] + ' ' + data['chrgTaskNm'] + ' ' + data['rgstStat'] + ' ' + data['rgstStatNm'] + ' ' + data['mgrEnm'] + ' ' + data['brthDate'] + ' ' + data['zip'] + ' ' + data['adr'] + ' ' + data['dtlAdr'] + ' ' + data['eduCont'] + ' ' + data['crrCont']

# 'cmpCd', 'mgrNm', 'pstnCd', '경영진 정보' 열만 선택합니다.
data = data[['cmpCd', 'mgrNm', 'pstnCd', '경영진 정보']]

# 결과를 출력합니다.
print(data.shape)

# 중복이 제거된 데이터를 CSV 파일로 저장합니다.
data.to_csv('경영진정보_train_처리완료.csv', index=False)  # '처리된_데이터.csv'는 저장할 파일의 이름입니다.
