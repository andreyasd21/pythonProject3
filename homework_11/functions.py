import json


def load_candidates_from_json():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_all():
    return load_candidates_from_json()


def get_candidate_by_pk(pk):
    for candidate in load_candidates_from_json():
        if pk == candidate['id']:
            return candidate
    return 'Такого кандидата нет в списке.'


def get_candidate_by_name(candidate_name):
    result = []
    for candidate in load_candidates_from_json():
        if candidate_name in candidate['name'].lower():
            result.append(candidate)
    return result


def get_candidate_by_skill(skill_name):
    result = []
    for candidate in load_candidates_from_json():
        if skill_name in candidate['skills'].lower():
            result.append(candidate)
    return result


print(get_candidate_by_skill('py'))