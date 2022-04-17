def import_candidates():
    import json

    with open("candidates.json", "r", encoding="UTF-8") as file:
        candidates = json.load(file)

    return candidates


def withdraws_all_candidates():
    """
    Выводит кандитатов в формате:
      Имя кандидата -
      Позиция кандидата -
      Навыки кандидата -
        """
    candidates = import_candidates()

    for candidate in candidates:
        # print("Имя кандидата -", candidate["name"])
        # print("Позиция кандидата -", candidate["position"])
        # print("Навыки кандидата -", candidate["skills"])
        # print()
        return candidate


print(withdraws_all_candidates())
