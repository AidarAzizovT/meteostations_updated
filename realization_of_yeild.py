import pandas
from data.kuzaikino_nurlat import kuzaikino_nurlat
from meteostations_updated import set_roof, TITLES


def to_dict(data):
    result = dict()
    gen = generate_keys_in_children(data)
    while (k:=next(gen)) is not None:
        if k[0] not in ("element_id", "source"):
            result[k[0]] = result.get(k[0], []) + [k[1]]
    return result

def generate_keys_in_children(data):
    for element in data['data']:
        for key, value in element.items():
            yield key, value
    yield None


result = to_dict(kuzaikino_nurlat)
#result = set_roof(result)
pandas.DataFrame(result).drop_duplicates().to_excel("kuzaikino_nurlat_final2.xlsx", index=False)
