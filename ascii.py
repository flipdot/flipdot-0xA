#!/usr/bin/env python3
from asciimatics.effects import Cycle, Effect
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from random import randint, random, choice


class _FlipStar(object):
    """
    Simple class to represent a single star for the FlipStars special effect.
    """

    def __init__(self, screen, pattern):
        """
        :param screen: The Screen being used for the Scene.
        :param pattern: The pattern to loop through
        """
        self._screen = screen
        self._star_chars = pattern
        self._cycle = None
        self._old_char = None
        self._respawn()

    def _respawn(self):
        """
        Pick a random location for the star making sure it does
        not overwrite an existing piece of text.
        """
        self._cycle = randint(0, len(self._star_chars))
        (height, width) = self._screen.dimensions
        while True:
            self._x = randint(0, width - 1)
            self._y = self._screen.start_line + randint(0, height - 1)
            if self._screen.get_from(self._x, self._y)[0] == 32:
                break
        self._old_char = " "

    def update(self):
        """
        Draw the star.
        """
        if not self._screen.is_visible(self._x, self._y):
            self._respawn()

        cur_char, _, _, _ = self._screen.get_from(self._x, self._y)
        if cur_char not in (ord(self._old_char), 32):
            self._respawn()

        self._cycle += 1
        if self._cycle >= len(self._star_chars):
            self._cycle = 0

        new_char = self._star_chars[self._cycle]
        if new_char == self._old_char:
            return

        self._screen.print_at(new_char, self._x, self._y)
        self._old_char = new_char


class FlipStars(Effect):
    """
    Add random stars to the screen and make them twinkle.
    """

    def __init__(self, screen, count, pattern=".", color_pattern=[1, 2, 3, 4, 5], **kwargs):
        """
        :param screen: The Screen being used for the Scene.
        :param count: The number of starts to create.
        :param pattern: The string pattern for the stars to loop through
        Also see the common keyword arguments in :py:obj:`.Effect`.
        """
        super(FlipStars, self).__init__(screen, **kwargs)
        self._pattern = pattern
        self._max = count
        self._stars = []

    def reset(self):
        self._stars = [_FlipStar(self._screen, self._pattern) for _ in range(self._max)]

    def _update(self, frame_no):
        for star in self._stars:
            star.update()

    @property
    def stop_frame(self):
        return 0


def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("wheh", font='big'),
            int(screen.height / 2 - 8)),
        Cycle(
            screen,
            FigletText("nice!", font='big'),
            int(screen.height / 2 + 3)),
        FlipStars(screen, 70)
    ]
    screen.play([Scene(effects, 500)])

Screen.wrapper(demo)
