def do_farm_power():
    power_target = 10000
    if num_items(Items.Power) > power_target:
        return 
    clear()
    #init
    # set_execution_speed(0.5)
    set_farm_size(0)
    for x in range(get_world_size()):
        for y in range(get_world_size()):
            ensure_tilled()
            ensure_watered()
            plant(Entities.Sunflower)
            move(North)
        move(East)

    move(South)
    move(West)

    counts = {}
    petals = []

    while can_harvest() == False:
        pass

    move_home()
    # set_execution_speed(0.5)
    
    max_power = 0
    x_max = 0
    y_max = 0
    is_highest = False

    for x in range(get_world_size()):
        for y in range(get_world_size()):
            pow = measure()
            insert_sorted(petals, pow)
            if pow in counts:
                counts[pow] += 1
            else: 
                counts[pow] = 1
            #(pow)
            if pow > max_power:
                max_power = pow
                x_max = get_pos_x()
                y_max = get_pos_y()
            move(North)
        move(East)

    move_to(x_max, y_max)
    while num_items(Items.Power) < power_target:
        if num_items(Items.Fertilizer) < 30:
            if buy_until_target(Items.Fertilizer, 150) == False:
                return
        if num_items(Items.Sunflower_Seed) < 30:
            if buy_until_target(Items.Sunflower_Seed, 150) == False:
                return

        #(is_highest)
        # harvest and remove count
        if is_highest == False:
            pow = measure()
            c = counts[pow]
            if c > 1:
                counts[pow] -= 1
            else: 
                counts.pop(pow)
                petals.pop(0)
        harvest()

        # replant
        ensure_watered()
        plant(Entities.Sunflower)
        while can_harvest() == False:
            use_item(Items.Fertilizer) 

        # if highest: harvest. if not: go to highest.
        pow = measure()
        #(pow)

        if pow >= petals[0]:
            is_highest = True
            #("instaharvest")
            continue
        else:
            is_highest = False
            insert_sorted(petals, pow)
            if pow in counts:
                counts[pow] += 1
            else: 
                counts[pow] = 1
            find_highest(petals)
        
def find_highest(list):
    #("find highest")
    #(range(get_world_size()))
    #(get_pos_x())
    #(get_pos_y())
    move_home()
    for x in range(get_world_size()):
        # if get_pos_x() % 2 == 0:
        #("going up")
        for y in range(get_world_size()):
            pow = measure()
            if pow >= list[0]:
                #(pow)
                #("highest found")
                return
            move(North)
        # else:
        # #    #("going down")
        # #    #(get_pos_y())
        #     while get_pos_y() > 0:
        #         pow = measure()
        #         if pow >= list[0]:
        # #            #(pow)
        # #            #("highest found")
        #             return
        #         move(South)

        move(East)
        