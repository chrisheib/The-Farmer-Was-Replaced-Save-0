# clear()
# quick_print(get_op_count())
# do_unlocks()
# quick_print(get_op_count())

timed_reset()
# reset()

# quick_print(get_cost(Unlocks.Dinosaurs))

while 1:
    # set_execution_speed(0.2)
    do_unlocks()
    do_farm()
    do_unlocks()
    buy_tanks()
    do_unlocks()
    do_farm_power()
    do_unlocks()
    do_max_pumpkins()
    do_unlocks()
    do_treasure()
    do_unlocks()
    do_cacti()
    do_unlocks()
    do_dinos()

    
# TODO: alles_ernten fn
# TODO: cost calculation
# TODO: space filler / snake planter

def do_farm():
    set_farm_size(0)
    move_home()

    while num_items(Items.Carrot) < get_amounts(): 
        if num_unlocked(Items.Carrot) == 1:
            buy_until_target(Items.Carrot_Seed, 150)
        # do_trade()
        # if num_items(Items.Cactus_Seed) >= 5:
        #     do_cactus_cols_simple()
        # else:
        #     decide_growth()
        #     decide_growth()
        #     decide_growth()

        decide_growth()
        while get_pos_x() > 0:
            decide_growth()
        
        do_unlocks()

def decide_growth():
    # if num_items(Items.Carrot) < 5000:
    #     return
    if num_items(Items.Hay) < get_amounts():
        do_grass_col()
        return
    if num_items(Items.Wood) < get_amounts():
        do_wood_col()
        return
    do_carrot_col()
    # if num_items(Items.Pumpkin) < 2000:
    #     do_pumpkin_col()
    #     return
    # if num_items(Items.Cactus) < 2000:
    #     do_pumpkin_col()
    #     return
    # do_grass_col()
    #do_pumpkin_col()

def get_amounts():
    if num_unlocked(Unlocks.Trees) < 1:
        return 300
    if num_unlocked(Unlocks.Pumpkins) < 1:
        return 1200
    if num_unlocked(Unlocks.Dinosaurs) < 1:
        return 5000
    if num_unlocked(Unlocks.Leaderboard) < 1:
        return 15000
    # return 15000
    return 200000