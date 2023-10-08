import pandas as pd

# 데이터를 로드하면서 'BusinessNum' 열을 문자열로 강제 형변환합니다.
data_jamu = pd.read_csv('재무제표정보_train_처리완료.csv', dtype={'BusinessNum': str})
data_finance = pd.read_csv('신용등급정보_train_처리완료.csv', dtype={'BusinessNum': str})

# data_finance의 'BusinessNum' 열에 있는 고유한 값들을 가져옵니다.
unique_business_nums = data_finance['BusinessNum'].unique()

# data_jamu에서 'BusinessNum'이 unique_business_nums에 있는 행만 남기고 나머지는 삭제합니다.
data_jamu_filtered = data_jamu[data_jamu['BusinessNum'].isin(unique_business_nums)]

# 'BusinessNum'을 기준으로 두 데이터 프레임을 병합합니다.
merged_data = data_jamu_filtered.merge(data_finance, on='BusinessNum', how='inner')

# 결과를 출력합니다.
print(merged_data)
merged_data.to_csv('재무안정성_train_처리완료.csv', index=False)

