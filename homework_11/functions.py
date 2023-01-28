import json


def load_candidates_from_json():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_all():
    return load_candidates_from_json()


def get_candidate(candidate_id):
    for candidate in load_candidates_from_json():
        if candidate_id == candidate['id']:
            return candidate
    return 'Такого кандидата нет в списке.'


def get_candidate_by_name(candidate_name):
    for candidate in load_candidates_from_json():
        if candidate_name.lower() in candidate['name'].lower().split(' '):
            return candidate
    return 'Такого кандидата нет в списке.'


def get_candidate_by_skill(skill_name):

    for candidate in load_candidates_from_json():
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            return candidate

    return 'Такого кандидата нет в списке.'


print(load_candidates_from_json())
print(get_candidate(1))
print(get_candidate_by_name('adela'))
print(get_candidate_by_skill('go'))
