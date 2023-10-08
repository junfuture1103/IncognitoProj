import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, classification_report

# 데이터를 불러옵니다. 데이터 파일 경로 및 이름을 확인하고 수정하세요.
data = pd.read_csv('재무안정성_train_처리완료.csv')

# 범주형 열을 원-핫 인코딩합니다.
data = pd.get_dummies(data, columns=['cmpCd', 'cmpScl', 'cmpNm', 'accDate', 'grdDesc'])

# 예측에 필요한 열을 선택합니다.
X = data.drop(columns=['criGrd', 'BusinessNum'])  # 'criGrd' 열을 제외한 모든 열
y = data['criGrd']  # 예측할 열인 'criGrd'

# 데이터를 학습용과 테스트용으로 나눕니다.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=42)

# 랜덤 포레스트 분류기를 초기화하고 학습시킵니다.
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# 테스트 데이터로 예측을 수행합니다.
y_pred = clf.predict(X_test)

# 예측 결과를 평가합니다.
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

report = classification_report(y_test, y_pred, target_names=y.unique(), output_dict=True)

print(f'정확도: {accuracy}')
print(f'정밀도: {precision}')
print(f'재현율: {recall}')
print(f'F1 Score: {f1}')
# print(f'ROC AUC: {roc_auc}')
print(f"Classification Report:\n{classification_report(y_test, y_pred, target_names=y.unique())}")
