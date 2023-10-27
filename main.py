from read_data import preprocess
from save_recommend import save_bigquery
from recommend import chatGPT

def main():
    # 추천에 사용될 재료 추출
    ingredients, current_date = preprocess()
    # print(ingredients, current_date)

    day = current_date
    food_name, gredients, add_gredients =  chatGPT(ingredients).split('/')
    # print(day, food_name, gredients, add_gredients)

    save_bigquery(day, food_name, gredients, add_gredients)

main()