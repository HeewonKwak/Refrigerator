from google.cloud import bigquery
from google.oauth2 import service_account

def save_bigquery(day, food_name, ingredients, add_ingredients):
    credentials = service_account.Credentials.from_service_account_file('bigquery.json')

    # GCP 클라이언트 객체 생성
    client = bigquery.Client(credentials = credentials, 
                            project = credentials.project_id)

    table_id = '{}.refrigerator.gptlog'.format(credentials.project_id)
    table = client.create_table(table_id, exists_ok=True)
    rows = [
        (str(day), food_name, ingredients, add_ingredients)
    ]
    errors = client.insert_rows(table, rows)
    print(errors)   # error가 없으면 출력 없음
