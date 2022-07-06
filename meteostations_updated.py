from data.kuzaikino_nurlat import kuzaikino_nurlat
import pandas

''' We convert Dict to Excel documents'''
TITLES = ['Наименование метеостанции', 'Влажность воздуха',
     'Атмосферное давление', 'Осадки',
     'Интенсивность осадков', 'Порыв ветра', 
     'Направление ветра', 'Скорость ветра', 
     'Точка росы', 'Температура воздуха', 'Коэффицент сцепления',
      'Температура дорожного покрытия', 'Облачность', 
      'Концентрация реагентов', 'Точка замерзания', 'Дата измерения']

def to_dict(data):
    result = dict()
    for element in data['data']:
        for key in element.keys():
            if key not in ("meteo_id", "source"):
                result[key] = result.get(key, []) + [element[key]]
    return result



def set_roof(data):
    changed_data = dict()
    for new_title, old_title in zip(TITLES, data.keys()):
        changed_data[new_title] = data[old_title]
    return changed_data


result = to_dict(kuzaikino_nurlat)
result = set_roof(result)
pandas.DataFrame(result).drop_duplicates().to_excel("kuzaikina_nurlat.xlsx", index=False)
                    
