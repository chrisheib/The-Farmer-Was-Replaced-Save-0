def do_treasure():
    if num_unlocked(Items.Fertilizer) < 1:
        return
    
    clear()
    set_farm_size(0)
    while True:
        if buy_until_target(Items.Fertilizer, 50) == False:
            return
        
        if num_items(Items.Gold) > get_amounts():
            return 
        
        ensure_tilled()
        ensure_watered()
        plant(Entities.Bush)
        while get_entity_type() != Entities.Treasure and get_entity_type() != Entities.Hedge:
            try_fertilize()
            if num_items(Items.Fertilizer) == 0:
                if buy_until_target(Items.Fertilizer, 50) == False:
                    return

        # do_a_flip()
        follow_left_wall()
    # set_farm_size(0)


def follow_left_wall():
    direction = North
    while get_entity_type() != Entities.Treasure:

        if direction == North:
            if False:
                pass
            elif move(West):
                direction = West
            elif move(North):
                direction = North
            elif move(East):
                direction = East
            elif move(South):
                direction = South

        elif direction == East:
            if False:
                pass
            elif move(North):
                direction = North
            elif move(East):
                direction = East
            elif move(South):
                direction = South
            elif move(West):
                direction = West

        elif direction == South:
            if False:
                pass
            elif move(East):
                direction = East
            elif move(South):
                direction = South
            elif move(West):
                direction = West
            elif move(North):
                direction = North

        elif direction == West:
            if False:
                pass
            elif move(South):
                direction = South
            elif move(West):
                direction = West
            elif move(North):
                direction = North
            elif move(East):
                direction = East
    harvest()