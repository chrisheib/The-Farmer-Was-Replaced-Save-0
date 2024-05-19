clear()

# quick_print(get_cost(Unlocks.Dinosaurs))

while 1:
    # set_execution_speed(0.2)
    do_trade()
    do_farm_power()
    # do_treasure()
    do_farm()
    do_max_pumpkins()
    do_cacti()
    do_dinos()

    
# TODO: alles_ernten fn
# TODO: cost calculation
# TODO: space filler / snake planter

def do_farm():
    set_farm_size(0)
    move_home()

    for i in range(10): 
        do_trade()
        # if num_items(Items.Cactus_Seed) >= 5:
        #     do_cactus_cols_simple()
        # else:
        #     decide_growth()
        #     decide_growth()
        #     decide_growth()

        decide_growth()
        while get_pos_x() > 0:
            decide_growth()
        quick_print(i)

def decide_growth():
    # if num_items(Items.Carrot) < 5000:
    #     return
    if num_items(Items.Wood) < 5000:
        do_wood_col()
        return
    if num_items(Items.Hay) < 5000:
        do_grass_col()
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
