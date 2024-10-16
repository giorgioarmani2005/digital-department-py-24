# TODO Найдите количество книг, которое можно разместить на дискете
capacity = 1.44 * 1024 * 1024
counter_page = 100
counter_line = 50
counter_symb_on_line = 25
counter_memory_symb = 4

print("Количество книг, помещающихся на дискету:", int(capacity/(counter_line*counter_page*counter_symb_on_line * counter_memory_symb)))
