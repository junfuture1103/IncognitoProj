### 실행방법
```
python3 create_csv.py
python3 make_result.py
```

먼저 create_csv.py를 실행하여 예시 데이터 셋을 제작합니다.<br>
여기서 예시 데이터 셋이란 유저들이 플랫폼을 사용하며 자연스럽게 입력할 데이터 예시를 뜻합니다. 
<br>
<br>
이후 make_result.py를 실행하여 원하는 키워드를 검색하고 해당 키워드와 유사한 사용자 혹은 회사의 이름을 추천해줍니다. 이때 키워드와 유사한 내용을 가지고 있는 회사 / 사용자의 이름과 요약정보, 채용공고를 함께 보여줍니다.
<br>
<br>
본 코드에서는 테스트를 위해 유저의 이름 / 나이 / 거주지 / 관심기업 / 본인설명등의 데이터를 자동생성(추후 유저가 입력할 것을 가정)합니다.

### 실행결과

```
PS C:\Users\jun\Documents\GitHub\IncognitoProj\script> & C:/Users/jun/AppData/Local/Programs/Python/Python310/python.exe c:/Users/jun/Documents/GitHub/IncognitoProj/script/make_result.py
overview 열의 결측값의 수: 0
원하시는 키워드를 입력해주세요 (예시: 기획 마케팅 및 보안): 기획
c:\Users\jun\Documents\GitHub\IncognitoProj\script\make_result.py:18: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
  data = data.append(new_data, ignore_index=True)
TF-IDF 행렬의 크기(shape) : (1001, 144)
코사인 유사도 연산 결과 : (1001, 1001)
[(194, 0.18267326584362725), (273, 0.16870487167850803), (936, 0.16763751548708938), (908, 0.16522406790565516), (513, 0.1638397304712536), (720, 0.16311898625802976), (368, 0.16149247636222355), (472, 0.15959492490125557), (491, 0.15931807120379826), (311, 0.1576353278031048)]
[194    한홀딩스(회사)
273         최선우
936         임미영
908         한선우
513         정수진
720         정지영
368         강영채
472         김수진
491         이영희
311         임수진
Name: title, dtype: object, 194    앱디자인 기획 클라우드 컴퓨팅 광고기획 애니메이션 진지한 염세적인 우호적인 의존적인...
273    개발 앱디자인 기획 빅데이터 디자인 북디자인 pm 패키징 전시기획 d2c 애니메이션...
936    UX디자인 설계 UI디자인 딥 러닝 기획 클라우드 컴퓨팅 앱디자인 사무보조 신제품 ...
908    국어국문 UX디자인 UI디자인 클라우드 컴퓨팅 앱디자인 디자인 빅데이터 설계 자연어...
513    로봇 공학 자연어 처리 기획 보안 머신 러닝 디자인 딥 러닝 개발 CAD 책임감 있...
720    클라우드 컴퓨팅 기획 개발 딥 러닝 UX디자인 국어국문 디자인 설계 빅데이터 앱디자...
368    로봇 공학 머신 러닝 UI디자인 기획 개발 디자인 국어국문 보안 설계 앱디자인 빅데...
472    설계 빅데이터 개발 로봇 공학 UX디자인 보안 기획 전시기획 가구디자인 총무 채무관...
491    설계 보안 데이터 분석 국어국문 로봇 공학 UI디자인 딥 러닝 머신 러닝 자연어 처...
311    기획 머신 러닝 빅데이터 개발 b2b 현실적 염세적인 대립적 충실한 개방적 사회적 ...
Name: overview, dtype: object, 194     http://4qC8MLV6sx.gov
273     http://1evPy7uzUY.org
936     http://BSRNFeGGfn.org
908     http://ph8v6b9h2B.biz
513     http://YvNwZr96GQ.biz
720     http://VaL7b6b3Qa.net
368    http://muSy8P8am2.info
472     http://AdGaIUIHxK.net
491     http://85r3vkflQU.edu
311     http://Z777vzIWf3.edu
Name: 채용공고, dtype: object]
```