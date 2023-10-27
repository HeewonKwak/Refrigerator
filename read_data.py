# 냉장고의 데이터 읽어서 GPT input으로 처리 해주기

import pandas as pd
from datetime import datetime, timedelta

def preprocess():
    df = pd.read_csv('refrigerator_data.csv')\

    # 현재 날짜 계산
    current_date = datetime.now()

    # 소비일자 열을 날짜 형식으로 변환
    df['소비일자'] = pd.to_datetime(df['소비일자'])

    # 기간 및 처리 유무 행 필터링
    # within_30_days = (current_date - df['소비일자']) <= timedelta(days=30)
    # without_7_days = (current_date - df['소비일자']) >= timedelta(days=-30)
    x_condition = df['처리 유무'] == 'X'

    result = df[x_condition]

    unique_products = result["식료품명"].unique()

    return ", ".join(unique_products), current_date