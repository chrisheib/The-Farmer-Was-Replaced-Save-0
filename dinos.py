def do_dinos():
    if num_unlocked(Items.Egg) < 1:
        return
    if num_unlocked(Unlocks.Leaderboard) > 0:
        return
    
    set_farm_size(4)
    
    while 1:
        if buy_until_target(Items.Egg, 16) == False:
            return
    
        for x in range(get_world_size()):
            for y in range(get_world_size()):
                use_item(Items.Egg)
                move(North)
            move(East)

        for x in range(get_world_size()):
            for y in range(get_world_size()):
                if can_harvest():
                    harvest()
                move(North)
            move(East)
    
