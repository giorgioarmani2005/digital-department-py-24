# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data=[]
    with open(INPUT_FILENAME,'r', encoding='utf-8') as f:
        dictionary = csv.DictReader(f)
        for row in dictionary:
            data.append(row)

      # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME,'w',encoding='utf-8') as new_f:
        json.dump(data,new_f,indent=4,ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
