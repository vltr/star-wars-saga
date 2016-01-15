# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sys
import star_wars as sw


class LaunchYourselfIntoTheVoid(Exception):
    def __init__(self, can_still_be_rescued=False, dont_ask_how=False,
                 *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.can_still_be_rescued = can_still_be_rescued
        self.dont_ask_how = dont_ask_how
        self.who_jumped = kwargs.get('who_jumped', None)


def main():
    lando_calrissian = sw.Character(side=None, aka=['Lando',
                                                    'Lando Calrissian'])
    luke = sw.Character(side=sw.LIGHT, aka=['Luke', 'Skywalker'])
    vader = sw.Character(side=sw.DARK, aka=['Darth Vader'])

    vader.threatens(
        who=lando_calrissian,
        callback=lambda: lando_calrissian.set_side(sw.DARK))

    sw.plot(lando_calrissian.betrays(side=sw.LIGHT))

    try:
        fight = sw.LightSaberFight(luke, vader)

        while fight.is_not_over() or luke.body.has_both_arms():
            fight.strike(vader, on=luke)
            fight.set_defense(luke)
            fight.strike(luke, on=vader)
            fight.set_defense(vader)
        try:
            vader.talk(sw._('LUKE_I_AM_YOUR_FATHER'))
            luke.talk(sw._('NOOOOOOOOOOOOOOOOOOOOOOOO'))
            luke.jump()
        except LaunchYourselfIntoTheVoid as lyitv:
            sw.plot(lando_calrissian.regret(
                callback=lambda: lando_calrissian.set_side(sw.LIGHT)))
            if lyitv.can_still_be_rescued and \
                    lyitv.who_jumped is not None and \
                    isinstance(lyitv.who_jumped, sw.Character) and \
                    lyitv.who_jumped.aka.contains('Luke'):

                    sw.plot(lando_calrissian.rescue(lyitv.who_jumped))
                    if lyitv.dont_ask_how:
                        sw.plot.next_movie(ep=6)

        sys.stderr.write(sw._('IN_THIS_EPISODE_SUCH_THING_HAPPENS_NOT',
                              language=sw.const.YODA))
        sys.exit(1)
    except sw.SameSideException:
        sys.stderr.write('there should be at least one character at each '
                         'side of the force for a proper lightsaber fight')

if __name__ == '__main__':
    main()

