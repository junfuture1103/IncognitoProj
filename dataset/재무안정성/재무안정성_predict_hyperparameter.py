import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.preprocessing import LabelEncoder

# 데이터를 불러옵니다. 데이터 파일 경로 및 이름을 확인하고 수정하세요.
data = pd.read_csv('재무안정성_train_처리완료.csv')

# 범주형 열을 원-핫 인코딩합니다.
data = pd.get_dummies(data, columns=['cmpCd', 'cmpScl', 'accDate'])

X = data.drop(columns=['criGrd', 'grdDesc', 'BusinessNum'])  # 'criGrd' 열을 제외한 모든 열
y = data['criGrd']  # 예측할 열인 'criGrd'

# 데이터를 학습용과 테스트용으로 나눕니다.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=42)

# 결과를 저장할 파일 'result3.txt'를 열고 준비합니다.
with open('result3.txt', 'w', encoding='utf-8') as result_file:
    # 튜닝할 하이퍼 파라미터 그리드를 정의합니다.
    param_grid = {
        'n_estimators': [50, 100],
        'learning_rate': [0.01, 0.1],
        'max_depth': [3, 4],
        'min_samples_split': [2, 3],
        'min_samples_leaf': [1, 2]
    }

    results = {}  # 결과를 저장할 딕셔너리

    for n_estimators in param_grid['n_estimators']:
        for learning_rate in param_grid['learning_rate']:
            for max_depth in param_grid['max_depth']:
                for min_samples_split in param_grid['min_samples_split']:
                    for min_samples_leaf in param_grid['min_samples_leaf']:
                        # Gradient Boost 모델을 초기화합니다.
                        model = GradientBoostingClassifier(
                            n_estimators=n_estimators,
                            learning_rate=learning_rate,
                            max_depth=max_depth,
                            min_samples_split=min_samples_split,
                            min_samples_leaf=min_samples_leaf,
                            random_state=42
                        )

                        # 모델을 학습하고 예측 결과를 저장합니다.
                        print('학습시작')
                        model.fit(X_train, y_train)
                        y_pred = model.predict(X_test)

                        accuracy = accuracy_score(y_test, y_pred)
                        precision = precision_score(y_test, y_pred, average='weighted')
                        recall = recall_score(y_test, y_pred, average='weighted')
                        f1 = f1_score(y_test, y_pred, average='weighted')

                        results[(n_estimators, learning_rate, max_depth, min_samples_split, min_samples_leaf)] = {
                            'accuracy': accuracy,
                            'precision': precision,
                            'recall': recall,
                            'f1': f1
                        }
                        print('학습끝')

    # 최적의 파라미터와 결과를 출력하고 파일에 저장합니다.
    best_params = max(results, key=lambda x: results[x]['accuracy'])
    result_file.write("최적 하이퍼 파라미터:\n")
    result_file.write(str(best_params) + "\n")
    result_file.write("최적 모델 결과:\n")
    result_file.write(str(results[best_params]) + "\n")

    # 모든 결과를 파일에 저장합니다.
    for params, scores in results.items():
        result_file.write(f"하이퍼 파라미터: {params}\n")
        result_file.write(f"정확도: {scores['accuracy']}\n")
        result_file.write(f"정밀도: {scores['precision']}\n")
        result_file.write(f"재현율: {scores['recall']}\n")
        result_file.write(f"F1 Score: {scores['f1']}\n\n")
