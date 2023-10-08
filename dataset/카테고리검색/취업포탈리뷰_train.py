import pandas as pd

# 데이터를 로드합니다. 데이터 파일의 경로를 적절하게 지정해야 합니다.
data = pd.read_csv('취업포탈리뷰_train.csv', usecols=[
    'BusinessNum', 'Job', 'EmployeeStatus', 'ReviewDate', 'TotScore', 'PromotionScore', 'WelfareScore', 'BalanceScore',
    'CultureScore', 'ExecutiveScore', 'ReviewTitle', 'Advantage', 'Disadvantage', 'ForExecutive', 'GrowthYN', 'RecommendYN'
])

# 중복 행을 제거합니다.
data = data.drop_duplicates(subset=data.columns.difference(['BusinessNum']))
data = data.drop_duplicates(subset=['BusinessNum'])

# 결과를 출력합니다.
print(data.shape)

# 중복이 제거된 데이터를 CSV 파일로 저장합니다.
data.to_csv('취업포탈리뷰_train_처리완료.csv', index=False)
