# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sys
import logging
import language_typology as lang_typ
import star_wars as sw


class LogFactory(object):
    """
    Helper class to provide standard logging
    """
    logger = None

    @classmethod
    def get_logger(cls):
        """
        Returns the logger
        """
        if cls.logger is None:
            cls.logger = logging.getLogger('star_wars')
            cls.logger.setLevel(logging.DEBUG)

            formatter = logging.Formatter('%(asctime)s - %(name)s - '
                                          '%(levelname)s - %(message)s')

            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)
            ch.setFormatter(formatter)

            cls.logger.addHandler(ch)

        return cls.logger


class LaunchYourselfIntoTheVoid(Exception):
    """
    Raised during really desperate situations
    """
    def __init__(self, can_still_be_rescued=False, dont_ask_how=False,
                 *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.can_still_be_rescued = can_still_be_rescued
        self.dont_ask_how = dont_ask_how
        self.who_jumped = kwargs.get('who_jumped', None)


def main():
    log = LogFactory.get_logger()
    log.warn('Spoiler Alert!')

    lando_calrissian = sw.Character(side=None, aka=['Lando',
                                                    'Lando Calrissian'])
    luke = sw.Character(side=sw.LIGHT, aka=['Luke', 'Skywalker'])
    vader = sw.Character(side=sw.DARK, aka=['Darth Vader'])

    sw.const.YODA.language_typology = lang_typ.OSV + lang_typ.OAV

    vader.threatens(
        who=lando_calrissian,
        callback=lambda: lando_calrissian.set_side(sw.DARK))

    sw.plot(lando_calrissian.betrays(side=sw.LIGHT))

    try:
        fight = sw.LightSaberFight(luke, vader)
        fight.add_defense_techniques(all=True)

        while fight.is_not_over() or luke.body.has_both_arms():
            fight.strike(vader, on=luke)
            fight.strike(luke, on=vader)
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

        log.error(sw._('IN_THIS_EPISODE_SUCH_THING_HAPPENS_NOT',
                       linguistic_typology=sw.const.YODA))
        sys.exit(1)
    except sw.SameSideException:
        log.critical('there should be at least one character at each '
                     'side of the force for a proper lightsaber fight')
        raise

if __name__ == '__main__':
    main()
