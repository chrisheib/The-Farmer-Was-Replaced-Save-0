def do_unlocks(): 
    if check_upgrade(Unlocks.Grass, 8) == False:
        return
    if check_upgrade(Unlocks.Expand) == False:
        return
    if check_upgrade(Unlocks.Speed, 11) == False:
        return
    if check_unlock(Unlocks.Plant) == False:
        return
    if check_upgrade(Unlocks.Carrots, 8) == False:
        return
    if check_upgrade(Unlocks.Trees, 8) == False:
        return
    if check_upgrade(Unlocks.Sunflowers) == False:
        return
    if check_upgrade(Unlocks.Pumpkins, 8) == False:
        return
    if check_unlock(Unlocks.Fertilizer) == False:
        return
    if check_upgrade(Unlocks.Mazes) == False:
        return
    if check_upgrade(Unlocks.Cactus) == False:
        return
    if check_upgrade(Unlocks.Dinosaurs) == False:
        return
    # check_unlock(Unlocks.Polyculture)
    check_unlock_end()

def check_unlock(u):
    if num_unlocked(u) > 0:
        return True
    # quick_print(u)
    # quick_print(num_unlocked(u))
    c = get_cost(u)
    # quick_print(c)
    can_buy = True
    for i in c:
        can_buy = can_buy and num_items(i) >= c[i]
    if can_buy:
        unlock(u)
        quick_print(u, "unlocked!")

def check_unlock_end():
    if num_unlocked(Unlocks.Leaderboard) > 0:
        return
    # quick_print(u)
    # quick_print(num_unlocked(u))
    c = get_cost(Unlocks.Leaderboard)
    # quick_print(c)
    can_buy = True
    for i in c:
        can_buy = can_buy and num_items(i) >= c[i]
    if can_buy:
        unlock(Unlocks.Leaderboard)
        quick_print(Unlocks.Leaderboard, "unlocked!")
        timed_reset()

def check_upgrade(u, max=100):
    # quick_print(u)
    # quick_print(num_unlocked(u))
    c = get_cost(u)
    if c == None:
        return True
    num = num_unlocked(u)
    if num >= max:
        return True
    # quick_print(c)
    can_buy = True
    for i in c:
        can_buy = can_buy and num_items(i) >= c[i]
    if can_buy:
        unlock(u)
        # quick_print(u)
        num += 1
        quick_print(u, "Level", num, "unlocked!")
        # quick_print("unlocked!")
    else:
        if num < 1:
            return False
    return True
    