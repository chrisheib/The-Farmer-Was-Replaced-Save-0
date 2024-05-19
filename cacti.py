def do_cacti():
    if num_unlocked(Items.Cactus) < 1:
        return
    set_farm_size(0)
    
    while 1:
        if buy_until_target(Items.Cactus_Seed, 5) == False:
            return
        
        if num_items(Items.Cactus) > 5000:
            return 
        move_home()
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

    
def check_swap_cactus_correct():
    me = measure()
    if me > measure(North): 
        swap(North)
        return False
    if me > measure(East):
        swap(East)
        return False
    if me < measure(South): 
        swap(South)
        return False
    if me < measure(West):
        swap(West)
        return False
    return True