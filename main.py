from read_data import preprocess
from save_recommend import save_bigquery
from recommend import chatGPT

def main():
    # 추천에 사용될 재료 추출
    my_ingredients, current_date = preprocess()
    print(my_ingredients, current_date)

    day = current_date
    food_name, ingredients, add_ingredients =  chatGPT(my_ingredients).split('/')
    print(day, food_name, ingredients, add_ingredients)

    save_bigquery(day, food_name, ingredients, add_ingredients)

main()