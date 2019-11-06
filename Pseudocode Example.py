'''
Tank v Tank Game PSEUDOCODE VERSION
By Anmol Kapoor
'''

class tank:
    method initialize
        initialize tank with image
        player can select color
        angle = 0 degrees (right)
        power = 0
        location_x = 50 pixels from left window side
    method increase_angle():
        angle += 1 degree
    method decrease_angle():
        angle -= 1 degree
    method increase_power():
        power += 1 power unit
    method decrease_power():
        power -= 1 power unit
    method fire():
        bullet1 = bullet()
        bullet1.takeoff()

class bullet:
    method initialize
        tag with which tank this belongs to
    method takeoff():
        math and physics intermission
        if any tank object hit:
            delete that tank object

player = tank(green)
cpu = tank(blue)
while True:
    while True:
        if player presses right arrow key:
            player.increase_angle()
        if player presses left arrow key:
            player.decrease_angle()
        if player presses down arrow key:
            player.decrease_power()
        if player presses up arrow key:
            player.increase_power()
        if player presses space key:
            player.fire()
            break
    if cpu is dead, open popup window that says "You have won!"

    cpu pick random angle and random power
    cpu.fire()
    if player = dead, open popup window that says "You have lost!"
