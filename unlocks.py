def do_unlocks(): 
    check_unlock(Unlocks.Fertilizer)
    check_upgrade(Unlocks.Speed)
    check_upgrade(Unlocks.Grass)
    check_unlock(Unlocks.Plant)
    check_upgrade(Unlocks.Expand)
    check_upgrade(Unlocks.Carrots)
    check_upgrade(Unlocks.Trees)
    check_upgrade(Unlocks.Sunflowers)
    check_upgrade(Unlocks.Pumpkins)
    check_upgrade(Unlocks.Mazes)
    check_upgrade(Unlocks.Cactus)
    check_upgrade(Unlocks.Dinosaurs)
    check_unlock(Unlocks.Polyculture)
    check_unlock_end()

def check_unlock(u):
    if num_unlocked(u) > 0:
        return
    # quick_print(u)
    # quick_print(num_unlocked(u))
    c = get_cost(u)
    # quick_print(c)
    can_buy = True
    for i in c:
        can_buy = can_buy and num_items(i) >= c[i]
    if can_buy:
        unlock(u)
        quick_print(u)
        quick_print("unlocked!")

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
        quick_print(Unlocks.Leaderboard)
        quick_print("unlocked!")
        timed_reset()

def check_upgrade(u):
    # quick_print(u)
    # quick_print(num_unlocked(u))
    c = get_cost(u)
    if c == None:
        return
    # quick_print(c)
    can_buy = True
    for i in c:
        can_buy = can_buy and num_items(i) >= c[i]
    if can_buy:
        unlock(u)
        quick_print(u)
        quick_print("unlocked!")