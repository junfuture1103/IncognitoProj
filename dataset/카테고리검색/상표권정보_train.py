import pandas as pd

# Create a DataFrame with the specified column headers
data = pd.read_csv('상표권정보_train.csv', usecols=[
    'BusinessNum', 'agentName', 'applicantName', 'applicationDate',
    'applicationNumber', 'classificationCode', 'registrationNumber', 'title'
])

# Now, 'data' is an empty DataFrame with the specified columns.

# 중복 행을 제거합니다.
data = data.drop_duplicates(subset=data.columns.difference(['BusinessNum']))
data = data.drop_duplicates(subset=['BusinessNum'])

# 결과를 출력합니다.
print(data.shape)

# 중복이 제거된 데이터를 CSV 파일로 저장합니다.
data.to_csv('상표권정보_train_처리완료.csv', index=False)
