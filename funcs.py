
def buy_tanks():
    # buy_until_target(Items.Carrot_Seed, 150)
    # buy_until_target(Items.Pumpkin_Seed, 150)
    # buy_until_target(Items.Cactus_Seed, 10) # Gold: 10
    # buy_until_target(Items.Sunflower_Seed, 150)
    # buy_until_target(Items.Fertilizer, 50)
    # buy_until_target(Items.Egg, 50)
    tanks = num_items(Items.Water_Tank) + num_items(Items.Empty_Tank)
    while tanks < get_amounts():
        if trade(Items.Empty_Tank, 100) == False:
            break

def buy_until_target(item, target_qty):
    qty = num_items(item)
    if qty < target_qty:
        if num_unlocked(Unlocks.Multi_Trade) > 1:
            if trade(item, target_qty - qty) == False:
                quick_print(get_cost(item))
                return False
        else: 
            while num_items(item) < target_qty:
                if trade(item) == False:
                    return False
    else:
        return True
    
def try_fertilize():
    if num_unlocked(Items.Fertilizer) > 0:
        use_item(Items.Fertilizer)

def ensure_tilled():
    if get_ground_type() != Grounds.Soil:
        till()

def ensure_untilled():
    if get_ground_type() == Grounds.Soil:
        till()
        
def do_grass_col():
    for y in range(get_world_size()):
        ensure_watered()
        ensure_untilled()
        if can_harvest(): 
            harvest()
        if get_world_size() > 1:
            move(North)
    if get_world_size() > 1:
        move(East)

def do_wood_col():
    if num_unlocked(Unlocks.Trees) < 1:
        do_bush_col()
    else:
        even = get_pos_x() % 2
        for y in range(get_world_size()):
            ensure_watered()
            if can_harvest(): 
                harvest()
                ensure_tilled()
                if y % 2 == even:
                    plant(Entities.Tree)

            move(North)
        move(East)

def do_bush_col():
    for y in range(get_world_size()):
        ensure_watered()
        if can_harvest(): 
            harvest()
            ensure_untilled()
            plant(Entities.Bush)
        move(North)
    move(East)

def do_pumpkin_col():
    for y in range(get_world_size()):
        ensure_watered()
        if can_harvest(): 
            harvest()
        if can_harvest():
            pass
        else:
            ensure_tilled()
            plant(Entities.Pumpkin)
        move(North)
    move(East)

def do_carrot_col():
    for y in range(get_world_size()):
        ensure_watered()
        ent = get_entity_type()
        if ent != None and ent != Entities.Carrots:
            while can_harvest() == False:
                pass
        if can_harvest(): 
            harvest()
        ensure_tilled()
        plant(Entities.Carrots)
        move(North)
    move(East)


def ensure_watered():
    water = get_water()
    # print(water)
    if water < 0.5:
        if num_items(Items.Water_Tank) > 1:
            use_item(Items.Water_Tank)

def move_to(x, y):
    while get_pos_x() > x:
        move(West)
    while get_pos_x() < x:
        move(East)
    while get_pos_y() > y:
        move(South)
    while get_pos_y() < y:
        move(North)

def move_home():
    move_to(0,0)

def insert_sorted(list, entry):
    index = 0
    for value in list:
        if entry == value:
            return
        if entry > value:
            list.insert(index, entry)
            return
        index += 1
    list.append(entry)