import pandas as pd

# data1 파일을 로드합니다.
data = pd.read_csv('국가R&D연구보고서_train.csv', usecols=[
    'PublicationAgency', 'ResultTitleKR', 'PublicationCountry',
    'ProjectNumber', 'ProjectTitle', 'ManagerName'
])

# 중복 행 및 결측치를 제거합니다.
data = data.drop_duplicates()
data = data.dropna()

# 모든 행의 문자열을 합치고, 새로운 열을 만듭니다.
data['MergedText'] = data.apply(lambda row: ' '.join(row.drop('PublicationAgency').astype(str)), axis=1)

# data2 파일을 로드합니다.
data2 = pd.read_csv('국가R&D성과_train_처리완료.csv')

# 중복 행을 제거합니다.
data2 = data2.drop_duplicates()

# 모든 행의 문자열을 합치고, 새로운 열을 만듭니다.
data2['MergedText'] = data2.apply(lambda row: ' '.join(row.drop('PerformAgent').astype(str)), axis=1)

# data와 data2를 'PublicationAgency' 기준으로 병합합니다.
merged_data = pd.merge(data, data2, left_on='PublicationAgency', right_on='PerformAgent', how='inner')

# 불필요한 열을 제거합니다.
merged_data = merged_data[['PublicationAgency', 'MergedText_x', 'MergedText_y']]

# MergedText_x와 MergedText_y를 합칩니다.
merged_data['MergedText'] =  merged_data['MergedText_x'] + merged_data['MergedText_y']
merged_data = merged_data[['PublicationAgency', 'MergedText']]

merged_data = merged_data.drop_duplicates()

# 결과를 출력합니다.
print(merged_data.shape)

# 결과를 CSV 파일로 저장합니다.
merged_data.to_csv('합쳐진_데이터.csv', index=False)
