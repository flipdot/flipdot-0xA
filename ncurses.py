#!/usr/bin/env python3
# import urwid
#
# txt = urwid.Text(u"Hello World")
# fill = urwid.Filler(txt, 'top')
# loop = urwid.MainLoop(fill)
# loop.run()

## import urwid
##
## def show_or_exit(key):
##     if key in ('q', 'Q'):
##         raise urwid.ExitMainLoop()
##     txt.set_text(repr(key))
##
## txt = urwid.Text(u"Hello World")
## fill = urwid.Filler(txt, 'top')
## loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)
## loop.run()

### import urwid
###
### def exit_on_q(key):
###     if key in ('q', 'Q'):
###         raise urwid.ExitMainLoop()
###
### palette = [
###     ('banner', '', '', '', '#ffa', '#60d'),
###     ('streak', '', '', '', 'g50', '#60a'),
###     ('inside', '', '', '', 'g38', '#808'),
###     ('outside', '', '', '', 'g27', '#a06'),
###     ('bg', '', '', '', 'g7', '#d06'),]
###
### placeholder = urwid.SolidFill()
### loop = urwid.MainLoop(placeholder, palette, unhandled_input=exit_on_q)
### loop.screen.set_terminal_properties(colors=256)
### loop.widget = urwid.AttrMap(placeholder, 'bg')
### loop.widget.original_widget = urwid.Filler(urwid.Pile([]))
###
### div = urwid.Divider()
### outside = urwid.AttrMap(div, 'outside')
### inside = urwid.AttrMap(div, 'inside')
### txt = urwid.Text(('banner', u" Hello World "), align='center')
### streak = urwid.AttrMap(txt, 'streak')
### pile = loop.widget.base_widget # .base_widget skips the decorations
### for item in [outside, inside, streak, inside, outside]:
###     pile.contents.append((item, pile.options()))
###
### loop.run()

import urwid

palette = [('I say', 'default,bold', 'default', 'bold'),]
ask = urwid.Edit(('I say', u"What is your name?\n"))
reply = urwid.Text(u"")
button = urwid.Button(u'Exit')
div = urwid.Divider()
pile = urwid.Pile([ask, div, reply, div, button])
top = urwid.Filler(pile, valign='top')

def on_ask_change(edit, new_edit_text):
    reply.set_text(('I say', u"Nice to meet you, %s" % new_edit_text))

def on_exit_clicked(button):
    raise urwid.ExitMainLoop()

urwid.connect_signal(ask, 'change', on_ask_change)
urwid.connect_signal(button, 'click', on_exit_clicked)

urwid.MainLoop(top, palette).run()
