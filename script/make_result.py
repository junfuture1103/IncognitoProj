import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv('user_info_data.csv', low_memory=False)

# overview 열에 존재하는 모든 결측값을 전부 카운트하여 출력
print('overview 열의 결측값의 수:',data['overview'].isnull().sum())

# 결측값을 빈 값으로 대체
data['overview'] = data['overview'].fillna('')
# 새로운 데이터 추가 (마지막 행에 추가)
input_data = input("원하시는 키워드를 입력해주세요 (예시: 기획 마케팅 및 보안): ")

new_data = {'title': input_data, 'overview': input_data}

# 새로운 데이터를 마지막 행에 추가
data = data.append(new_data, ignore_index=True)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['overview'])
print('TF-IDF 행렬의 크기(shape) :',tfidf_matrix.shape)

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
print('코사인 유사도 연산 결과 :', cosine_sim.shape)

title_to_index = dict(zip(data['title'], data.index))

# 각 행의 코사인 유사도를 행에 추가
for idx, movie_title in enumerate(data['title']):
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # 상위 10개의 유사도

    # 유사도 값을 가져와서 데이터프레임에 추가
    similarity_values = [score[1] for score in sim_scores]
    data.at[idx, 'cosine_similarity'] = ','.join(map(str, similarity_values))

def get_recommendations(title, cosine_sim=cosine_sim):
    # 선택한 채용정보의 이름으로부터 해당 채용정보의 인덱스를 받아온다.
    idx = title_to_index[title]

    # 해당 채용정보와 모든 메세지와의 유사도를 가져온다.
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 유사도에 따라 채용정보들을 정렬한다.
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # 가장 유사한 10개의 채용정보를 받아온다.
    sim_scores = sim_scores[1:11]
    print(sim_scores)

    # 가장 유사한 10개의 채용정보의 인덱스를 얻는다.
    movie_indices = [idx[0] for idx in sim_scores]

    # 가장 유사한 10개의 채용정보의 이름을 리턴한다.
    return data['title'].iloc[movie_indices], data['overview'].iloc[movie_indices] , data['채용공고'].iloc[movie_indices]

# 원하는 검색어
print(get_recommendations(input_data))

# 결과를 CSV 파일로 저장
data.to_csv('result.csv', index=False)