def do_max_pumpkins():
    set_farm_size(0)

    while 1:
        if buy_until_target(Items.Pumpkin_Seed, get_world_size() * get_world_size() * 2) == False:
            return
        
        if num_items(Items.Pumpkin) > get_amounts():
            return 

        # plant all

        for x in range(get_world_size()):
            for y in range(get_world_size()):
                ent = get_entity_type()
                if ent != None and ent != Entities.Pumpkin:
                    while can_harvest() == False:
                        pass
                    harvest() 
                ensure_tilled()
                ensure_watered()
                plant(Entities.Pumpkin)
                move(North)
            move(East)

        ready_to_harvest = True
        candidates = []
        for x in range(get_world_size()):
            for y in range(get_world_size()):
                if get_entity_type() == None:
                    ready_to_harvest = False
                    ensure_tilled()
                    ensure_watered()
                    plant(Entities.Pumpkin)
                    c = get_pos_x(), get_pos_y()
                    candidates.append(c)
                move(North)
            move(East)

        while len(candidates) > 0:
            for c in candidates:
                x, y = c
                move_to(x, y)
                if get_entity_type() == Entities.Pumpkin:
                    if can_harvest():
                        candidates.remove(c)
                        quick_print(candidates)
                    else:
                        if len(candidates) == 1:
                            try_fertilize()
                else: 
                    ensure_tilled()
                    ensure_watered()
                    plant(Entities.Pumpkin)


        move_home()
        harvest()
