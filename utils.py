def import_candidates(file):
    import json

    with open(file, "r", encoding="UTF-8") as file:
        candidates = json.load(file)

    return candidates


def withdraws_candidates(candidates):
    """
    Выводит кандитатов в формате:
      Имя кандидата -
      Позиция кандидата -
      Навыки кандидата -
        """

    result = "<pre>\n"

    for candidate in candidates:
        result += (
            f"Имя кандидата - {candidate['name']}\n"
            f"Позиция кандидата - {candidate['position']}\n"
            f"Навыки кандидата - {candidate['skills']}\n\n"
        )

    result += "</pre>"

    return result


def search_candidate_id(candidates, uid):
    """

    """
    for candidate in candidates:
        if candidate["id"] == uid:
            return [candidate]


def search_skills(candidates, skill):
    candidates_with_skill = []

    for candidate in candidates:
        candidate_skills = candidate["skills"].lower().split(", ")
        for candidate_skill in candidate_skills:
            if candidate_skill == skill.lower():
                candidates_with_skill.append(candidate)
                break

    return candidates_with_skill
