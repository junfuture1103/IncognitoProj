import pandas as pd

# 데이터를 로드합니다. 데이터 파일의 경로를 적절하게 지정해야 합니다.
db_category = input('원하는 카테고리를 입력해주세요 : \n \
                     - 경영진정보 \n \
                     - 기업정보요약 \n \
                     - 디자인권정보 \n \
                     - 상표권정보 \n \
                     - 실용신안정보 \n \
                     - 온라인뉴스 \n \
                     - 취업포탈리뷰 \n \
                     - 특허정보상세 \n \
                     - 패밀리특허정보 \n ')

data = pd.read_csv(db_category+'_train_처리완료.csv')

description = {
    '경영진정보': '원하는 경영진 카테고리를 입력해주세요: (mgrNm)',
    '기업정보요약': '원하는 기업 카테고리를 입력해주세요 (건물 건설업 / 컴퓨터 프로그래밍 서비스업 / 경영컨설팅업): ',
    '디자인권정보': '원하는 디자인권 카테고리를 입력해주세요: (applicantName)',
    '상표권정보': '원하는 상표권 카테고리를 입력해주세요: (applicantName)',
    '실용신안정보': '원하는 실용신안 카테고리를 입력해주세요: (applicantName)',
    '온라인뉴스': '원하는 뉴스회사 카테고리를 입력해주세요: (PressName)',
    '취업포탈리뷰': '원하는 취업포탈리뷰 카테고리를 입력해주세요: (Job)',
    '특허정보상세': '원하는 특허정보상세 카테고리를 입력해주세요: (patentTitle)',
    '패밀리특허정보': '원하는 패밀리특허정보 카테고리를 입력해주세요: (publicationNumber)',
}

category_key = {
    '경영진정보': 'mgrNm',
    '기업정보요약': 'indNm',
    '디자인권정보': 'applicantName',
    '상표권정보': 'applicantName',
    '실용신안정보': 'applicantName',
    '온라인뉴스': 'PressName',
    '취업포탈리뷰': 'Job',
    '특허정보상세': 'patentTitle',
    '패밀리특허정보': 'publicationNumber',
}

input_category = input('카테고리를 입력하세요: 예시'+description[db_category])



# 입력한 카테고리에 해당하는 행 전체를 출력합니다.
matching_rows = data[data[category_key[db_category]] == input_category]

if not matching_rows.empty:
    print(f"입력한 카테고리 '{input_category}'에 해당하는 행 전체:")
    print(matching_rows)
else:
    print(f"'{input_category}' 카테고리에 해당하는 행을 찾을 수 없습니다.")
