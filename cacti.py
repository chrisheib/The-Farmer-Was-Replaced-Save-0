def do_cacti():
    set_farm_size(3)
    
    while 1:
        if buy_until_target(Items.Cactus_Seed, 5) == False:
            return
        do_cactus_cols_simple()
        

def do_cactus_cols_simple():
    # for y in range(get_world_size()):
    move(North)
    ensure_watered()
    ensure_tilled()
    plant(Entities.Cactus)

    move(East)
    ensure_watered()
    ensure_tilled()
    plant(Entities.Cactus)

    move(South)
    ensure_watered()
    ensure_tilled()
    plant(Entities.Cactus)

    move(North)
    move(North)
    ensure_watered()
    ensure_tilled()
    plant(Entities.Cactus)

    move(East)
    move(South)
    ensure_watered()
    ensure_tilled()
    plant(Entities.Cactus)

    while can_harvest() == False:
        pass 

    move(West)

    while check_swap_cactus_correct() == False:
        pass
    harvest()

    move(East)
    move(East)
    move(South)