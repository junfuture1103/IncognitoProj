import pandas as pd

# 데이터를 로드하면서 'BusinessNum' 열을 문자열로 강제 형변환합니다.
data1 = pd.read_csv('국가R&D성과_train_처리완료.csv', dtype={'BusinessNum': str})
data2 = pd.read_csv('국가R&D과제_train_처리완료.csv', dtype={'BusinessNum': str})
data3 = pd.read_csv('국가R&D연구보고서_train_처리완료.csv', dtype={'BusinessNum': str})
data4 = pd.read_csv('취업포탈리뷰_train_처리완료.csv', dtype={'BusinessNum': str})
data5 = pd.read_csv('기업정보요약_train_처리완료.csv', dtype={'BusinessNum': str})

data_list = [data1,data2,data3,data4,data5]
# data_finance의 'BusinessNum' 열에 있는 고유한 값들을 가져옵니다.

unique_business_nums = data2['BusinessNum'].unique()

for tmp_data in data_list:
    # data_jamu에서 'BusinessNum'이 unique_business_nums에 있는 행만 남기고 나머지는 삭제합니다.
    data_jamu_filtered = tmp_data[tmp_data['BusinessNum'].isin(unique_business_nums)]

    # 'BusinessNum'을 기준으로 두 데이터 프레임을 병합합니다.
    merged_data = data_jamu_filtered.merge(tmp_data, on='BusinessNum', how='inner')