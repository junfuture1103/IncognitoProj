import pandas as pd

# 데이터를 로드합니다. 데이터 파일의 경로를 적절하게 지정해야 합니다.
data = pd.read_csv('국가R&D성과_train.csv', usecols=[
    'BusinessNum','SitId', 'ProjectName', 'ProjectCode', 'EquipId', 'EquipNo', 'Year', 'ProjectYear', 'MinistryCode', 'MinistryName',
    'BudgetProjectNo', 'BudgetName', 'PerformAgentCode', 'PerformAgent', '6TCode', '6TName', 'TechnologyRoadMapCode',
    'TechnologyRoadMapName', 'ScienceClassCode1', 'ScienceClassName1', 'ScienceClassCode2', 'ScienceClassName2',
    'ScienceClassCode3', 'ScienceClassName3'
])

# 중복 행을 제거합니다.
data = data.drop_duplicates()

# 'BudgetName' 열의 결측값을 먼저 제거합니다.
data = data.dropna(subset=['BudgetName'])
data = data.dropna(subset=['PerformAgent'])

# 'BudgetName' 열에서 '보안' 문자열이 포함된 행을 필터링하여 제거합니다.
data = data[~data['BudgetName'].str.contains('보안')]
data = data.drop_duplicates(subset=['ProjectName'], keep='first')

# 모든 행의 문자열을 합치고, 새로운 열을 만듭니다.
data['MergedText'] = data.apply(lambda row: ' '.join(row.drop(['BusinessNum','PerformAgent']).astype(str)), axis=1)

# PublicationAgency 열만 남기고 다른 열을 삭제합니다.
data = data[['BusinessNum','PerformAgent', 'MergedText']]

# 결과를 출력합니다.
print(data.shape)

# 중복이 제거된 데이터를 CSV 파일로 저장합니다.
data.to_csv('국가R&D성과_train_처리완료.csv', index=False)
