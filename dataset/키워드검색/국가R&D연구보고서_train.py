import pandas as pd

# 데이터를 로드합니다. 데이터 파일의 경로를 적절하게 지정해야 합니다.
data = pd.read_csv('국가R&D연구보고서_train.csv', usecols=[
    'BusinessNum','PublicationAgency', 'ResultTitleKR', 'PublicationCountry',
    'ProjectNumber', 'ProjectTitle', 'ManagerName'
])

# 중복 행을 제거합니다.
data = data.drop_duplicates()
data = data.dropna()

# 모든 행의 문자열을 합치고, 새로운 열을 만듭니다.
data['MergedText'] = data.apply(lambda row: ' '.join(row.drop(['BusinessNum','PublicationAgency']).astype(str)), axis=1)

# PublicationAgency 열만 남기고 다른 열을 삭제합니다.
data = data[['BusinessNum','PublicationAgency', 'MergedText']]

# 결과를 출력합니다.
print(data.shape)

# 중복이 제거된 데이터를 CSV 파일로 저장합니다.
data.to_csv('국가R&D연구보고서_train_처리완료.csv', index=False)
