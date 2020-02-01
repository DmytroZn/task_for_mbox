# 1.1 Считать с файла mbox.txt письма и вывести их в консоль в формате:
# from (date): subject

with open('mbox.txt', 'r') as f:
    list_of_f_from = []
    for f_str in f.readlines():
        if 'Date: ' in f_str:
            f_date = f_str.split('Date: ')[1][:-1]
        elif 'From: ' in f_str:
            f_from = f_str.split(' ')[1][:-1]  
        elif 'Subject: ' in f_str:
            f_subj = f_str.split('Subject: ')[1]  
            list_of_f_from.append(f_from)
            print(f'{f_from} ({f_date}): {f_subj}')

# 1.2 Затем посчитать количество писем от каждого отправителя 
# и вывести в консоль в формате:
# from: quantity
set_of_f_from = set(list_of_f_from)
for i in set_of_f_from:
    print(f'{i}: {list_of_f_from.count(i)}')
