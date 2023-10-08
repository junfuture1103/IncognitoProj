import pandas as pd
import random

# 미리 정의된 성 리스트와 이름 리스트
surnames = ["김", "이", "박", "최", "정", "강", "조", "윤", "임", "한"]
given_names = ["철수", "영희", "민수", "지영", "선우", "미영", "태준", "혜진", "성호", "윤미", "종현", "수진", "영채", "전자(회사)", "물산(회사)", "홀딩스(회사)", "주식회사"]

# 다양한 관심사와 특징 리스트 정의
interests = ["국어국문","개발","디자인","UX디자인","UI디자인","앱디자인","기획","설계","보안","데이터 분석", "머신 러닝", "딥 러닝", "자연어 처리", "클라우드 컴퓨팅", "빅데이터", "로봇 공학"]
personalities = ["외향적", "내향적", "친절한", "타국적", "창의적", "분석적", "사회적", "적극적", "집중", "개방적", "도전적", "창의적", "모험적", "감정적", "이성적", "계획적", "즉흥적", "신경질적", "독단적", "교활한", "오만한", "겸손한", "영악한", "지루한", "진지한", "유쾌한", "친절한", "음흉한", "음탕한", "방탕한", "음란한"]
personalities2 = ["진지한", "사실적", "현실적", "책임감 있는", "업무 지향적", "대립적", "성실한", "조화로운", "독립적인", "의존적인", "느긋한", "예민한", "헌신적인", "충실한", "자제력 있는", "행동 지향적인", "우호적인", "충동적인", "낙관적인", "염세적인", "활기찬", "열정적인", "조직적인"]
salary_ranges = ["연봉 3000~5000", "연봉 5000~7000", "연봉 7000 이상", "연봉 2000 미만", "연봉 1억이상"]
company_sizes = ["대기업", "중소기업", "스타트업", "공공기관", "교육기관", "금융기관", "중견기업", "강소기업"]
interests2 = ["홍보", "신제품", "판매전략", "pm", "패키징", "정밀분석", "생산공정", "설비개선", "채무관리", "신유통채널", "d2c", "b2b", "마케팅", "콘텐츠마케팅", "퍼포먼스마케팅", "경영전략", "경영관리", "인사", "교육", "노무", "재경", "총무", "CAD", "설비도면", "PLC", "판매", "아웃바운드", "인바운드", "세무", "사무보조", "문서작성", "광고기획", "브랜드매니저", "시장분석", "온라인마케팅", "PR", "전시기획", "컨벤션", "애니메이션", "캐릭터", "모션그래픽", "카탈로그편집", "북디자인", "일러스트", "가구디자인", "연출", "PD", "방송송출", "광고제작", "카피", "IMC", "포지셔닝", "쇼호스트", "리포터"]
import random
import string

def generate_random_url():
    # 랜덤한 문자열 생성 (길이는 예시로 5로 설정)
    random_string1 = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    random_string2 = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    
    # 랜덤한 도메인 생성 (10개 이상의 도메인 추가)
    domains = [".com", ".xyz", ".co.kr", ".net", ".org", ".io", ".info", ".biz", ".gov", ".edu"]
    random_domain = random.choice(domains)
    
    # URL 조합
    url = "http://" + random_string1 + random_string2 + random_domain
    
    return url


# 임의의 사용자 정보와 관련된 문장 생성
def generate_user_data():
    user_info = {
        "관심사": random.sample(interests, random.randint(1, len(interests))),
        "관심사2": random.sample(interests2, random.randint(1, len(interests2))),
        "특징": random.sample(personalities, random.randint(1, len(personalities))),
        "특징2": random.sample(personalities2, random.randint(1, len(personalities2))),
        "연봉": random.choice(salary_ranges),
        "재직중인기업규모": random.choice(company_sizes)
    }

    return " ".join(user_info["관심사"] +user_info["관심사2"] + user_info["특징2"] +user_info["특징"] + [user_info["연봉"], user_info["재직중인기업규모"]])

# 데이터 생성 및 CSV 파일로 저장
data = []
for _ in range(1000):  # 1000개의 데이터 포인트 생성
    surname = random.choice(surnames)  # 랜덤으로 성 선택
    given_name = random.choice(given_names)  # 랜덤으로 이름 선택
    full_name = surname + given_name  # 성과 이름 조합
    age = random.randint(20, 60)
    experience = random.randint(0, 40)
    location = random.choice(["서울", "대전", "부산", "인천", "대구", "광주"])
    company_message = random.choice(company_sizes)

    user_data = generate_user_data()
    notice_url = generate_random_url()

    data.append([full_name, age, experience, location, company_message, user_data, notice_url])

# 데이터프레임 생성 및 CSV 파일로 저장
df = pd.DataFrame(data, columns=["title", "나이", "경력", "거주지", "관심회사형태", "overview", "채용공고"])
df.to_csv("user_info_data.csv", index=False)
print('완료')