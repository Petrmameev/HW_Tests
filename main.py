def from_russia(visits):
    final_list = []
    for visit in visits:
        for country in visit.values():
            if 'Россия' in country:
                final_list.append(visit)
    return final_list


def unique_values(dict_):
    values_ = list(set(sum(dict_.values(), [])))
    return values_


def max_volume(example):
    for el in example.keys():
        if stats[el] == max(example.values()):
            return el


geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


if __name__ == '__main__':
    print(from_russia(geo_logs))
    print(unique_values(ids))
    print(max_volume(stats))