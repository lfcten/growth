def evaluateActions(actions):
    dic_support = {}
    support_unit = []
    dic_loc = {}
    dic_army = {}
    army_list = []
    for action in actions:
        action = action.split(" ")
        army_list.append(action[0])
        if action[2] == "Support":
            if action[3] not in dic_support:
                dic_support[action[3]] = []
            dic_support[action[3]].append(action[0])
            support_unit.append(action[0])
            dic_loc[action[0]] = action[1]
            if action[1] not in dic_army:
                dic_army[action[1]] = []
            dic_army[action[1]].append(action[0])
        elif action[2] == "Hold":
            dic_loc[action[0]] = action[1]
            if action[1] not in dic_army:
                dic_army[action[1]] = []
            dic_army[action[1]].append(action[0])
        elif action[2] == "Move":
            dic_loc[action[0]] = action[3]
            if action[3] not in dic_army:
                dic_army[action[3]] = []
            dic_army[action[3]].append(action[0])
    invalid = set()
    live_army = []
    for support in support_unit:
        loc = dic_loc[support]
        if len(dic_army[loc]) > 1:
            invalid.add(support)

    for key, val in dic_army.items():
        army_name, max_count, occur = "", -1, 0
        if len(val) == 1:
            live_army.append(army_name)
            continue
        for army in val:
            ans = 0
            if army in dic_support:
                for supporter in dic_support[army]:
                    if supporter not in invalid:
                        ans += 1
            if ans > max_count:
                army_name = army
                max_count = ans
                occur = 1
            elif ans == max_count:
                occur += 1
        if occur == 1:
            live_army.append(army_name)
    res = []
    for a in army_list:
        if a in live_army:
            res.append(a + " " + dic_loc[a])
        else:
            res.append(a + " [dead]")
    return res
