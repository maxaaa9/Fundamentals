def cast_spell(name, stats, mp, spell):
    if stats[1] < mp:
        print(f"{name} does not have enough MP to cast {spell}!")
    else:
        print(f"{name} has successfully cast {spell} and now has {stats[1] - mp} MP!")
        stats[1] -= mp
    return stats[1]


def take_damage(name, stats, dmg, attacker_name):
    if stats[0] <= dmg:
        print(f"{name} has been killed by {attacker_name}!")
        return "Killed"
    print(f"{name} was hit for {dmg} HP by {attacker_name} and now has {stats[0] - dmg} HP left!")
    stats[0] -= dmg
    return stats[0]


def recharge(name, stats, re_amount):
    if stats[1] + re_amount >= 200:
        re_amount = 200 - stats[1]
        stats[1] = 200
    else:
        stats[1] += re_amount
    print(f"{name} recharged for {re_amount} MP!")
    return stats[1]


def heal(name, stats, heal):
    if stats[0] + heal >= 100:
        heal = 100 - stats[0]
        stats[0] = 100
    else:
        stats[0] += heal
    print(f"{name} healed for {heal} HP!")
    return stats[0]


number_of_heroes = int(input())

heroes_stats = {}
for add in range(number_of_heroes):
    hero_stats = input().split()
    hero_name = hero_stats[0]
    hero_hp = int(hero_stats[1])
    if hero_hp > 100:
        hero_hp = 100
    hero_mp = int(hero_stats[2])
    if hero_mp > 200:
        hero_mp = 200
    if hero_name not in heroes_stats.keys():
        heroes_stats[hero_name] = [hero_hp, hero_mp]

while True:
    command = input().split(" - ")
    if command[0] == "End":
        break
    hero_select = command[1]
    if hero_select in heroes_stats.keys():
        if command[0] == "CastSpell":
            needed_mp = int(command[2])
            spell_name = command[3]
            heroes_stats[hero_select][1] = cast_spell(hero_select, heroes_stats[hero_select], needed_mp, spell_name)

        elif command[0] == "TakeDamage":
            damage = int(command[2])
            attacker = command[3]
            heroes_stats[hero_select][0] = take_damage(hero_select, heroes_stats[hero_select], damage, attacker)
            if heroes_stats[hero_select][0] == "Killed":
                heroes_stats.pop(hero_select)
        elif command[0] == "Recharge":
            amount = int(command[2])
            heroes_stats[hero_select][1] = recharge(hero_select, heroes_stats[hero_select], amount)
        elif command[0] == "Heal":
            heal_amount = int(command[2])
            heroes_stats[hero_select][0] = heal(hero_select, heroes_stats[hero_select], heal_amount)

for heroes_name, hp_mp in heroes_stats.items():
    print(heroes_name)
    print(f"    HP: {hp_mp[0]}")
    print(f"    MP: {hp_mp[1]}")
