from operator import index
from turtle import right
from xml.etree.ElementInclude import include
import pandas as pd

adv1_df = pd.read_csv('advertising_1.csv', index_col='Number')
adv2_df = pd.read_csv('advertising_2.csv', index_col='Number')
adv12_df = adv1_df.append(adv2_df)
adv3_df = pd.read_csv('advertising_3.csv', index_col = 'Number')
adv123_df = pd.concat([adv12_df, adv3_df], axis = 0)
success_adv_df = adv123_df.loc[lambda adv123_df: adv123_df['Clicked on Ad'] == 1]

#12
users_df = pd.read_csv('users.csv')
print(users_df)
print(users_df.describe(include = 'all'))

#13
# 1. Возраст самого молодого пользователя сайта: 19 
# 2. Максимальный средний доход в месте жительства пользователя сайта: 79484.800000
# 3. Средний возраст пользователя сайта: 36.073256
# 4. Количество заполненных значений для колонки, содержащей информацию о том, является пользователь мужчиной или нет: 868
# 5. Минимальный номер пользователя: 5

#14
print(success_adv_df)
success_adv_df = success_adv_df.reset_index()
success_full_df = pd.merge(success_adv_df, users_df, on = 'Number')
success_full_df = success_full_df.set_index('Number')
print(success_full_df)

#15
print(success_full_df.describe(include=[object]))

#16
country = success_full_df['Country']
country = list(country)
for i in country:
    print(i, ":", country.count(i))
    for j in country:
        if i == j:
            country.remove(i)




#17
print(success_full_df.loc[lambda success_full_df: success_full_df['Country'] == 'Ethiopia'])

#18
filtered_df = success_full_df.loc[(success_full_df['Country'] == 'Ethiopia') & (success_full_df['Age'] < 30) & (success_full_df['Daily Internet Usage']>120)]
print(filtered_df)

#19
filtered_df2 = filtered_df.loc[(filtered_df['Daily Time Spent on Site'].isnull()) | (filtered_df['Daily Time Spent on Site']>55)]
print(filtered_df2)