import pandas as pd

# 원본 데이터를 불러옵니다.
original_data = pd.read_csv('재무제표정보_train.csv')

# 원하는 항목을 정렬하기 위한 리스트
desired_items = [
    '노무비', '당기순이익(손실)', '당좌부채(당좌차월)', '당좌자산', '대손상각비', '매출 증가율', '매출액', '매출원가',
    '매출채권', '매출총이익', '법인세비용', '부채총계', '비유동부채', '수출액1', '수출액2', '수출액3', '수출액4',
    '수출액5', '영업외비용', '영업이익', '원재료', '유동부채', '유동비율', '유동자산', '유형자산 증가율', '이익잉여금',
    '이자비용', '인건비', '자기자본', '자본잉여금', '자본총계', '자산총계', '재고자산', '제조경비', '제조원가',
    '차입금', '총자산', '총자산 증가율', '투자자산', '판매비와관리비'
]

# 원하는 항목을 추출하여 새로운 데이터프레임 생성
filtered_data = original_data[original_data['accNm'].isin(desired_items)]

# 피벗 테이블로 데이터 변환
pivot_data = filtered_data.pivot_table(index=['BusinessNum', 'stYear'], columns='accNm', values='acctAmt', aggfunc='first')

# 인덱스 초기화
pivot_data.reset_index(inplace=True)

# NaN 값 0으로 채우기
pivot_data.fillna(0, inplace=True)

# 결과 데이터프레임을 CSV 파일로 저장
pivot_data.to_csv('재무제표정보_train_처리완료.csv', index=False)
