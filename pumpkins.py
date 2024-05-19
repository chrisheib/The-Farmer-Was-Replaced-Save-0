def do_max_pumpkins():
    set_farm_size(0)

    while 1:
        if buy_until_target(Items.Pumpkin_Seed, 500) == False:
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

        ready_to_harvest = False
        while ready_to_harvest == False:
            ready_to_harvest = True
            for x in range(get_world_size()):
                for y in range(get_world_size()):
                    if get_entity_type() == None:
                        ready_to_harvest = False
                        ensure_tilled()
                        ensure_watered()
                        plant(Entities.Pumpkin)
                    move(North)
                move(East)
        move_home()
        harvest()
