#!/usr/bin/env python3
import argparse
import logging
from textwrap import dedent

from pathlib import Path
from functools import wraps
from datetime import datetime
import random

import tkinter as tk
from . import MODULES_VERBOSE
from . import RootWindow, FrameUnlabelled, FrameLabelled, FrameStateful, FramePaned, Notebook, NotebookUniform, ScrolledWidget, FrameRadio
from . import Button, Checkbox, Entry, Label, LabelStateful, Listbox, Combobox, ComboboxMap, EntryMultiline, Tree, Spinbox, Radio
from . import ListboxControl, CheckboxFrame
from . import var, spec, fn
from .model import CP, BindingGlobal, Timeout, TimeoutIdle, Interval, RateLimiter, FileType, FileTypes, Justification, WindowState, GuiState
from .model import SStyle, DStyle


# Automatic Tab Completion
# Production Wrapper (keep the API)
class shtab:
    # Global Markers
    FILE = None
    DIRECTORY = None

    # API
    def add_argument_to(self, *args, **kwargs):
        pass


if __debug__:
    # Try to import the real deal
    try:
        import shtab  # type: ignore[no-redef] # noqa: F811
    except ImportError:
        pass

logger = logging.getLogger(__name__)


class LuftBaloons(FrameUnlabelled):
    layout = 'xE'

    def setup_widgets(self, howmany=16 - 3):
        assert howmany > 1
        widgets = {}
        for widx in range(howmany):
            idx = 'lb:%d' % widx
            widget = Checkbox(self, label='%02d' % widx)
            widget.trace(self.onClick_lb, idx=idx)
            widgets[idx] = widget
        # Ignore the second checkbox
        fn.state_ignore(widgets['lb:1'])
        return widgets

    def onClick_lb(self, vobj, etype, *, idx):
        pass
        # logger.debug('Clicked on "%s" @ %s:%s', idx, vobj, etype)
        # logger.debug('- State: %r', vobj.get())


class ListFrame_Inner(FrameStateful):
    wstate_single = 'e'

    def __init__(self, *args, label, **kwargs):
        super().__init__(*args, label=label, labelInner=label, **kwargs)

    def setup_widgets(self, labelInner, *, ljust=Justification.NoJustify):
        self.lbl = Label(self, label=f'Label: {labelInner}', justify=ljust)
        self.e = Entry(self, justify=ljust)  # label=f'Entry: {labelInner}'


class ListFrame_Outer_Label(FrameUnlabelled):
    layout = tk.HORIZONTAL

    def setup_widgets(self):
        self.cbL = Checkbox(self, label='').putIgnoreState()
        self.lbl = Label(self, label='Child Widgets\nare Justified',
                         anchor=CP.N, expand=True)
        self.cbR = Checkbox(self, label='').putIgnoreState()


class ListFrame_Outer(FrameStateful):
    label = 'Outer Frame'
    layout = 'R1,2,1'

    def setup_widgets(self, *, cbox1):
        self.lbls = ListFrame_Outer_Label(self)
        self.left = ListFrame_Inner(self, label='Left',
                                    cvariableDefault=True,
                                    ljust=Justification.Left)
        self.right = ListFrame_Inner(self, label='Right',
                                     cvariableDefault=False,
                                     ljust=Justification.Right)
        self.bottom = ListFrame_Inner(self, label='Center',
                                      cvariable=cbox1,
                                      ljust=Justification.Center)


class ListFrame_Lists(FramePaned):
    layout = tk.HORIZONTAL

    def setup_widgets(self, *, vLst):
        self.lstS = Listbox(self,
                            height=6,
                            variable=vLst,
                            selectable=True)  # Selectable
        self.lstRO = ScrolledWidget(self, Listbox, label='Unselectable',
                                    maxHeight=3, expand=True,  # Varying Height, Expanded  # N/A on FramePaned
                                    variable=vLst,
                                    selectable=False,
                                    style=Listbox.Style(altbg=True),
                                    )  # Not Selectable


class ListFrame__Actions(FrameUnlabelled):
    layout = tk.HORIZONTAL

    def setup_widgets(self):
        self.op1 = Button(self, label='Op1',
                          styleID='Small')
        self.op2 = Button(self, label='Op2',
                          styleID='Small')

    def setup_adefaults(self):
        self.op1.onClick = self.genAction('OP1')
        self.op2.onClick = self.genAction('OP2')

    def genAction(self, label: str):
        def genAction(event=None):
            logger.debug('Action: %s', label)
        return genAction


class ListFrame(FrameStateful):
    label = 'List Box'
    layout = 'R3,1,2,1'

    def setup_widgets(self, *, cbox1) -> None:
        i_choices: spec.StaticMap[int] = spec.StaticMapValues(lambda i: 'I%d' % i, range(10), defaultValue=7)

        self.bFill = Button(self, label='Fill Me!')
        self.lPanes = Label(self, label='↓ Drag Separator ↓')
        self.bCheck = Button(self, label='Check')

        vLst = self.var(var.StringList, name='lst')
        self.cLst = ListFrame_Lists(self, vLst=vLst)

        self.bChoice = Button(self, label='CB=2')
        self.i_choice = ComboboxMap(self, values=i_choices)  # label='CB(int)'

        self.rstateful = ListFrame_Outer(self, labelAnchor=CP.N,
                                         cbox1=cbox1)

        self._actions = ListFrame__Actions(self).putAuto()

    def setup_layout(self, layout):
        self.pgrid_r(self.cLst, weight=0)

        self._actions.place(anchor=CP.NE.value, relx=1, rely=0,
                            x=-2, y=SStyle.Size_YF_Frame)

    def setup_defaults(self):
        self.fill_lst()
        # Events
        self.bFill.onClick = self.fill_lst
        self.bCheck.onClick = self.check_lst
        self.bChoice.onClick = self.i_choice.eSetValue(2)

        self.i_choice.trace(self.onChosen, spec=self.i_choice.specValues)

        BindingGlobal(self.bChoice, '<F1>', self.globalHelp,
                      immediate=True, description='Nothing, just showing the event object')

    def setup_adefaults(self):
        # Why not verify some invariants?
        assert self.wroot_search() == self.wroot, 'Invalid Root calculation'

    def fill_lst(self):
        ctime = str(datetime.now())
        self.gvar('lst').set(['A', 'List', 'Of', 'Letters', '@', ctime])

    def check_lst(self):
        sel = self.cLst.lstS.wselection()
        logger.debug('S: %r', sel)

    def onChosen(self, variable, etype, *, spec):
        logger.debug('V: %r', variable)
        label = variable.get()
        logger.debug('   Label: %s[%r]', label, spec.value(label))

    def globalHelp(self, event=None):
        if event:
            logger.debug('Event: %r', event)


class UpstreamBool(FrameLabelled):
    layout = 'x1N'  # Bottom-Up
    # Comment the following line to change the state
    isNoneable = False  # Don't skip this widget, even when its state is `None`

    def setup_widgets(self, what_bool):
        self.bOnFS = Button(self, label='Toggle FullScreen')
        self.u_bool = Checkbox(self, variable=what_bool, label='Upstream "bool"')
        self.bNoOp_Big = Button(self, label='No Operation')

    def setup_adefaults(self):
        self.bOnFS.onClick = self.onRootFS

    def onRootFS(self, event=None):
        self.wroot.rgstate = WindowState(fullscreen=not self.wroot.rgstate.fullscreen)


class NB_Child_Simple(FrameUnlabelled):
    layout = 'Rx,1'
    wstate_single = 'e'

    def setup_widgets(self, label):
        w = {}
        for n in range(5):
            w[f'n{n}'] = Label(self, label=f'{n}: {label}')
        w['e'] = LabelStateful(self, labelPosition=CP.E)
        return w

    def setup_defaults(self):
        self.widgets['e'].binding('<Button-1>', self.onClick_E)

    def setup_adefaults(self):
        self.widgets['e'].wstate = 'Clickable LabelStateful'

    def onClick_E(self, event=None):
        w = self.widgets['e']
        state = w.wstate
        if not state.endswith(' T'):
            state += ' T'
            imgname = 'warning-s16'
        else:
            state = state[:-2]
            imgname = 'info-s16'
        w.wstate = state
        w['image'] = self.wimage(imgname)


class NB_Child_Complex(NotebookUniform):
    tabids = {f'TC{d}': f'Tab Complex {d}' for d in range(5)}

    def setup_tab(self, tid: str, tname: str):
        return NB_Child_Simple(self, label=tid)


class NB_Child_Timeout(FrameLabelled):
    label = 'Timeout'

    def __init__(self, *args, **kwargs):
        self.t = Timeout(self, self.onTimeout, 1000, immediate=False)
        super().__init__(*args, **kwargs)

    def setup_widgets(self):
        self.cScheduled = Checkbox(self, label='Scheduled?', readonly=True,
                                   styleID='ReadonlyEmphasis')
        self.cTriggered = Checkbox(self, label='Triggered?', readonly=True,
                                   styleID='ReadonlyEmphasis')
        self.bToggle = Button(self, label='Toggle\nasync')

        self.bToggle.onClick = self.onToggle

    def setup_defaults(self):
        self.update()

    def update(self):
        self.cScheduled.wstate = self.t.isScheduled()
        self.cTriggered.wstate = self.t.isTriggered()

    def onToggle(self):
        self.t.toggle()
        self.update()

    def onTimeout(self):
        logger.debug('Timeout!')
        self.update()


class NB_Child_Timeout_Delay(FrameLabelled):
    label = 'Timeout (Delayed)'

    def __init__(self, *args, **kwargs):
        self.t = Timeout(self, self.onTimeout, 1000, immediate=False)
        super().__init__(*args, **kwargs)

    def setup_widgets(self):
        self.cScheduled = Checkbox(self, label='Scheduled?', readonly=True)
        self.cTriggered = Checkbox(self, label='Triggered?', readonly=True)
        self.bToggle = Button(self, label='  Toggle\nasync-ish')

        self.bToggle.onClick = self.onToggle

    def setup_defaults(self):
        self.update()

    def update(self):
        self.cScheduled.wstate = self.t.isScheduled()
        self.cTriggered.wstate = self.t.isTriggered()

    def onToggle(self):
        self.t.toggle()
        self.update()

    def onTimeout(self):
        logger.debug('Timeout!')
        self.update()
        logger.debug('Delay ...')
        self.after(1000)
        logger.debug('... Done!')


class NB_Child_TimeoutIdle_Delay(FrameLabelled):
    label = 'TimeoutIdle (Delayed)'

    def __init__(self, *args, **kwargs):
        self.t = TimeoutIdle(self, self.onTimeout, immediate=False)
        self.tsleep = TimeoutIdle(self, lambda: self.after(1000), immediate=False)  # Pretend this is a long calculation
        super().__init__(*args, **kwargs)

    def setup_widgets(self):
        self.cScheduled = Checkbox(self, label='Scheduled?', readonly=True)
        self.cTriggered = Checkbox(self, label='Triggered?', readonly=True)
        self.bToggle = Button(self, label='Toggle\n sync')

        self.bToggle.onClick = self.onToggle

    def setup_defaults(self):
        self.update()

    def update(self):
        self.cScheduled.wstate = self.t.isScheduled()
        self.cTriggered.wstate = self.t.isTriggered()

    def onToggle(self):
        ts = [self.tsleep, self.t]
        # (un)schedule both timeouts in tandem
        if self.t.isScheduled():
            for t in ts:
                t.unschedule()
        else:
            for t in ts:
                t.schedule()
        self.update()

    def onTimeout(self):
        logger.debug('TimeoutIdle!')
        self.update()


class NB_Child_TimeoutIdle_Chain(FrameLabelled):
    label = 'TimeoutIdle (Chained)'

    def __init__(self, *args, **kwargs):
        self.tsleep = TimeoutIdle(self, self.onTimeoutSleep, immediate=False)
        self.t = TimeoutIdle(self, self.onTimeout, immediate=False)
        super().__init__(*args, **kwargs)

    def setup_widgets(self):
        self.cScheduled = Checkbox(self, label='Scheduled?', readonly=True)
        self.cTriggered = Checkbox(self, label='Triggered?', readonly=True)
        self.bToggle = Button(self, label='Toggle\n sync')

        self.bToggle.onClick = self.onToggle

    def setup_defaults(self):
        self.update()

    def update(self):
        self.cScheduled.wstate = self.t.isScheduled()
        self.cTriggered.wstate = self.t.isTriggered()

    def onToggle(self):
        ts = [self.tsleep, self.t]
        # (un)schedule both timeouts in tandem
        if self.t.isScheduled():
            for t in ts:
                t.unschedule()
        else:
            for t in ts:
                t.schedule()
        self.update()

    def onTimeoutSleep(self):
        logger.debug('Chain Delay ...')
        self.after(1000)
        logger.debug('... Done!')
        self.t.schedule()
        self.update()

    def onTimeout(self):
        logger.debug('TimeoutIdle!')
        self.update()


class NB_Child_Timeouts(FrameUnlabelled):
    # layout = tk.HORIZONTAL

    def setup_widgets(self):
        self.timeout = NB_Child_Timeout(self)
        self.timeout_d = NB_Child_Timeout_Delay(self)
        self.timeout_idle_d = NB_Child_TimeoutIdle_Delay(self)
        self.timeout_idle_c = NB_Child_TimeoutIdle_Chain(self)


class NB_Child_Interval(FrameUnlabelled):
    layout = 'R3,3'

    def __init__(self, *args, **kwargs):
        self.interval = Interval(self, self.onInterval, 1000, immediate=False)
        super().__init__(*args, **kwargs)

    def setup_widgets(self):
        self.txt_lbl = Label(self, label='Count (1s)')
        self.txt = Entry(self, justify=CP.center, readonly=True)
        self.stateScheduled = Checkbox(self, label='Scheduled?', readonly=True)
        self.state_on = Button(self, label='ON')
        self.state_off = Button(self, label='OFF')
        self.state_offforce = Button(self, label='OFF (Force)')

    def setup_defaults(self):
        self.txt.wstate = 'Elapsed Seconds'

    def setup_adefaults(self):
        self.state_on.onClick = self.onIntervalOn
        self.state_off.onClick = self.onIntervalOff
        self.state_offforce.onClick = self.onIntervalOffForce

    def onIntervalOn(self, event=None):
        if self.interval.scheduled:
            logger.debug('Already Scheduled')
        else:
            self.txt.wstate = str(0)
            self.interval.schedule()
        self.stateScheduled.wstate = self.interval.scheduled
        self.state_off.focus()

    def onIntervalOff(self, event=None):
        self.interval.unschedule()
        self.state_on.focus()
        self.stateScheduled.wstate = self.interval.scheduled

    def onIntervalOffForce(self, event=None):
        was_scheduled = self.interval.scheduled
        self.interval.unschedule(force=True)
        if was_scheduled:
            self.txt.wstate = f'Force Stop at {self.txt.wstate}'
        self.stateScheduled.wstate = self.interval.scheduled
        self.state_on.focus()

    def onInterval(self):
        new_state = str(int(self.txt.wstate) + 1)
        if self.interval.scheduled:
            self.txt.wstate = new_state
        else:
            self.txt.wstate = f'Stop at {new_state}'


class NB_Child_RateLimiter(FrameUnlabelled):
    layout = 'R2,1,2'

    def __init__(self, *args, **kwargs):
        self.rl = RateLimiter(self, self.onRL, 1000)
        super().__init__(*args, **kwargs)

    def setup_widgets(self):
        self.txt_lbl = Label(self, label='Now')
        self.txt = Entry(self, readonly=True,
                         justify=CP.center, width=30)
        self.hit_lbl = Label(self, label='Hit me Hard!\nCount will only change once per second.\nThe timings are not perfect.')
        self.buttonHit = Button(self, label='HIT')
        self.stateRL = Checkbox(self, label='Rate Limited?', readonly=True)

    def setup_defaults(self):
        self.txt.wstate = str(0)

    def setup_adefaults(self):
        self.buttonHit.onClick = self.onHit

    def onHit(self, event=None):
        self.stateRL.wstate = not self.rl.hit()

    def onRL(self):
        self.txt.wstate = f"{datetime.now().isoformat(' ', timespec='microseconds')} μs"
        # self.txt.wstate = str(int(self.txt.wstate) + 1)
        if self.stateRL.wstate:
            logger.debug('Clear RateLimit marker')
            self.stateRL.wstate = False


class NB_Child_Dialog(FrameUnlabelled):
    layout = 'Rx,1'
    wstate_single = 'txt'

    def setup_widgets(self):
        self.ds = Button(self, label='D S')
        self.dl = Button(self, label='D L')
        self.fs = Button(self, label='F S')
        self.fl = Button(self, label='F L')
        self.flc = Button(self, label='F L(py)')
        self.fsc = Button(self, label='F S(py)')
        self.txt = LabelStateful(self)

        self.ds.onClick = self.click(fn.ask_directory_save, self, title='Directory @ .',
                                     initialDirectory=Path('.'))
        self.dl.onClick = self.click(fn.ask_directory_load, self, title='Directory @ Home',
                                     initialDirectory=Path('~').expanduser())
        self.fs.onClick = self.click(fn.ask_file_save, self, title='File @ ..',
                                     initialDirectory=Path('..'))
        self.fl.onClick = self.click(fn.ask_file_load, self, title='File @ /',
                                     initialDirectory=Path('/'))
        self.fsc.onClick = self.click(self.customFile, fn.ask_file_save)
        self.flc.onClick = self.click(self.customFile, fn.ask_file_load)

    def click(self, fn, *args, **kwargs):
        @wraps(fn)
        def wrapped():
            self.txt.wstate = ''
            ret = fn(*args, **kwargs)
            ret_loc = ret.resolve() if ret else ret
            ret_exists = str(ret.exists()) if ret else 'N/A'
            self.txt.wstate = f'{ret_loc}\nExists: {ret_exists}'
        return wrapped

    def customFile(self, function):
        return function(self, title='Custom Python Files @ .',
                        initialDirectory=Path('.'),
                        includeAll=False, filetypes=FileTypes({
                            'Python': FileType('py'),
                            'TOML': FileType('toml'),
                        }))


class NB_Child_Scrollbars(FrameUnlabelled):
    layout = 'R2,x'
    wstate_single = 'slst'

    def setup_widgets(self):
        self.randomize = Button(self, label='Randomize List Size')
        self.setscrolls = Button(self, label='Toggle Scrollbars')

        vSlist = self.var(var.StringList, name='slst')
        self.sbL = ScrolledWidget(self, Listbox,
                                  scrollHorizontal=None, scrollVertical=None,  # Auto (default)
                                  height=5, variable=vSlist)
        self.sbC = ScrolledWidget(self, Listbox,
                                  scrollHorizontal=False, scrollVertical=False,  # Manual, disabled
                                  height=5, variable=vSlist)
        self.sbR = ScrolledWidget(self, Listbox,
                                  scrollHorizontal=True, scrollVertical=True,  # Manual, enabled
                                  height=5, variable=vSlist)

        self.randomize.onClick = self.onRandom
        self.setscrolls.onClick = self.onShowAll

    def setup_adefaults(self):
        self.onRandom()

    def onRandom(self, event=None):
        randomsize = random.randint(5, 30)  # Allow an opportunity for no vertical scrollbar
        self.gvar('slst').set([f'Index {i:03}' for i in range(1, randomsize + 1)])

    def onShowAll(self, event=None):
        # sbL: Auto, Set True
        self.sbL.wproxy.set_scroll_state(True, True)
        # sbC: Manual, Set True (no-op)
        self.sbC.wproxy.set_scroll_state(True, True)
        # sbR: Manual, Set Reversed
        self.sbR.wproxy.set_scroll_state(*(not b for b in self.sbR.wproxy.get_scroll_state()))


class NB_Complex_ListboxSet(FrameUnlabelled):
    layout = tk.HORIZONTAL

    def setup_widgets(self):
        ls_all = spec.StaticList((f'String {idx:02}' for idx in range(1, 20 + 1)), defaultIndex=0)

        ls_selected = random.sample(list(ls_all.all()), k=5)
        self.left = ListboxControl(self,
                                   selAll=ls_all)
        self.right = ListboxControl(self, layout='c1,x', label='Full Control',
                                    selAll=ls_all, selList=ls_selected,
                                    buttonOne=False, buttonAll=True, buttonOrder=True)

    def setup_defaults(self):
        self.left.onAddAll()


class NB_Complex_CheckboxList(CheckboxFrame):
    def __init__(self, *args, **kwargs):
        kwargs.update({
            'stateCheckboxes': {
                '%d' % n: 'Check #%d' % n
                for n in range(0, 15, 3)
            },
            'label': 'TopLevel Label',
            'labelsCheckboxes': {
                # See the order of label keys
                '0': 'CB #0',
                ('0',): 'CheckBox #0',
            },
            'layoutCheckboxes': '2x3',
        })
        super().__init__(*args, **kwargs)


class NB_Complex_CheckboxNested(CheckboxFrame):
    def __init__(self, *args, **kwargs):
        self._bState = True
        kwargs.update({
            'layout': 'H1,2,x',
            'hasButtons': [  # Custom buttons, changes the layout above
                CheckboxFrame.IButton('enable', 'Enable ALL',
                                      onClickSetAll=True),
                CheckboxFrame.IButton('disable', 'Disable ALL',
                                      onClickSetAll=False),
                CheckboxFrame.IButton('other', 'Other',
                                      self.onClickOther),
            ],
            'stateCheckboxes': {
                **{
                    'N1(%d)' % nn: {
                        'N2(%d)' % nnn: 'N2(%d|%d)' % (nn, nnn)
                        for nnn in range(2)
                    }
                    for nn in range(3)
                },
                **{
                    'NN1(0)': {
                        'NN2': 'NN2(0|0)',
                        **{
                            'NN2(%d)' % N: {
                                'NN3(%d)' % NN: 'NN3(0|%d|%d)' % (N, NN)
                                for NN in range(3)
                            }
                            for N in range(1, 2 + 1)
                        },
                    },
                },
            },
            'stateDefault': True,
            'layoutCheckboxes': [tk.HORIZONTAL, tk.VERTICAL, 'R1,x'],
            'labelsCheckboxes': {
                ('NN1(0)',): 'NN1 [[0]]',
                **{
                    ('N1(%d)' % nn,): 'N1 [[%d]]' % nn
                    for nn in range(2)
                }
            },
            'traceFn': self.onCheckboxClick,
        })
        super().__init__(*args, **kwargs)

    def onCheckboxClick(self, *what):
        def onCheckboxClick(var, etype):
            logger.debug('Trace: %s [%s]', ' » '.join(what), var.get())
        return onCheckboxClick

    def onClickOther(self):
        logger.debug('Click "Other" @ %s', self)
        new_state = not self._bState
        logger.debug('- State: %s -> %s', self._bState, new_state)
        new_gstate = GuiState(enabled=new_state)
        bEnabled = self.wbutton('enable')
        bDisabled = self.wbutton('disable')
        for w in (bEnabled, bDisabled):
            w.gstate = new_gstate
        self._bState = new_state


class NB_Child_Checkboxen(FrameStateful):
    layout = tk.VERTICAL
    wstate_single = 'cb'

    def setup_widgets(self, *, cbReadonly: bool):
        cb_str = 'RO' if cbReadonly else 'RW'
        self.cb = Checkbox(self, label=f'Checkbox {cb_str}', readonly=cbReadonly)


class NB_Complex_ChechboxRORW(FrameUnlabelled):
    layout = 'R2,x'

    def setup_widgets(self):
        self.rw = NB_Child_Checkboxen(self, label='ReadWrite', cbReadonly=False)
        self.ro = NB_Child_Checkboxen(self, label='ReadOnly', cbReadonly=True)
        self.read = Button(self, label='Check')
        self.toggle_rw = Button(self, label='Toggle RW "alternate"')

    def setup_layout(self, layout):
        self.pgrid_r(self.read, self.toggle_rw, weight=0)
        self.toggle_rw.grid(sticky=tk.EW)

    def setup_adefaults(self):
        self.read.onClick = self.onRead
        self.toggle_rw.onClick = self.onToggleRW

    def onRead(self):
        logger.debug('=> GUI State for Checkbox')
        logger.debug('   RW: %s', self.rw.cb.gstate)
        logger.debug('   RO: %s', self.ro.cb.gstate)

    def onToggleRW(self):
        self.rw.cb.gstate = GuiState(alternate=not self.rw.cb.gstate.alternate)


class NB_Complex(Notebook):
    def setup_tabs(self):
        return {
            'lc': Notebook.Tab('ListboxControl', NB_Complex_ListboxSet(self)),
            'cl': Notebook.Tab('CheckboxFrame', NB_Complex_CheckboxList(self)),
            'cn': Notebook.Tab('CheckboxFrame\nNested', NB_Complex_CheckboxNested(self)),
            'cb_rorw': Notebook.Tab('CB RO/RW', NB_Complex_ChechboxRORW(self)),
        }

    def setup_adefaults(self):
        self.wselect('cn')


class NB(Notebook):
    def setup_tabs(self):
        return {
            'sb': Notebook.Tab('Scrollbars', NB_Child_Scrollbars(self)),
            'tt': Notebook.Tab('Timeouts', NB_Child_Timeouts(self),
                               image=self.wimage('info-s16'), labelPosition=CP.E),  # Default labelPosition
            'ti': Notebook.Tab('Interval', NB_Child_Interval(self)),
            'trl': Notebook.Tab('RateLimiter', NB_Child_RateLimiter(self)),
            'td': Notebook.Tab('Dialogues', NB_Child_Dialog(self),
                               image=self.wimage('info-msgbox-s16'), labelPosition=True),  # Only image
            'tc': Notebook.Tab('Tab Complex', NB_Child_Complex(self, styleID='TabCenter'),
                               image=self.wimage('info-s16'), labelPosition=CP.W),  # "Reverse" labelPosition
            't1': Notebook.Tab('Tab 1', NB_Child_Simple(self, label='Tab 1')),
            't2': Notebook.Tab('Tab 2', NB_Child_Simple(self, label='Tab 2')),
            'c': Notebook.Tab('Complex', NB_Complex(self, styleID='TabV_W')),  # Vertical Tabs (not fully baked)
        }

    def setup_adefaults(self):
        self.wselect('c')


class TextWidget(EntryMultiline):
    styleSheet = {
        '.emph': {
            'overstrike': True,
        }
    }


class TextEditor(FrameStateful):
    label = 'LTML'
    layout = 'Rx,1'
    wstate_single = 'txt'

    def setup_widgets(self):
        self.bTxtClean = Button(self, label='Clean TXT')
        self.bTxtReset = Button(self, label='Reset TXT')
        self.bTxtSet = Button(self, label='Set TXT')
        self.txt = ScrolledWidget(self, TextWidget,
                                  setgrid=False)

    def setup_layout(self, layout):
        self.txt.grid(sticky=tk.NS)

    def setup_defaults(self):
        self.pgrid_r(self.bTxtClean, self.bTxtReset, self.bTxtSet,  # Buttons
                     weight=0)
        # Setup events
        self.bTxtClean.onClick = self.txt.style_reset
        self.bTxtReset.onClick = self.txt_reset
        self.bTxtSet.onClick = self.txt_set
        self.txt.onClickTag = self.txt_clicked

    def setup_adefaults(self):
        self.txt_set(cnt=20)

    def txt_reset(self, event=None):
        self.txt.wstate = ''

    def txt_set(self, event=None, *, cnt=None):
        texts = []
        if cnt is None:
            cnt = random.choice(range(10, 25))
        for r in range(cnt):
            texts.append(f'<b class="emph">Line</b> <i>{"%02d" % r}</i>/{cnt} ')
            if r % 2 == 0:
                _txt = 'EVEN'
            else:
                _txt = '    '
            texts.append(f'<a>[{_txt}]</a>')
            texts.append('<br/>')
            if r % 5 == 0:
                texts.append('<br/>')
        self.txt.wstate = ''.join(texts)

    def txt_clicked(self, tag, tag_id, tags_other):
        logger.debug(f'Clicked on {tag} {tag_id} :: {tags_other}')


class TreeExample(Tree):
    def onClickHeader(self, header):
        logger.debug('Clicked on header "%s"', header.name)


class NB_Center_Spinbox(FrameUnlabelled):
    layout = 'x2E'

    def setup_widgets(self):
        lim = spec.Limit(1, 5, fn=int, imax=False)

        self.label_spinN = Label(self, label=f'{lim} :: Normal')
        self.spinN = Spinbox(self, values=lim)

        self.label_spinL = Label(self, label=f'{lim} :: Wrap Values')
        self.spinL = Spinbox(self, values=lim, wrap=True)

        self.label_spinE = Label(self, label=f'{lim} :: Editable')
        self.spinE = Spinbox(self, values=lim, readonly=False)

        lim_grow = spec.Limit(None, None, fn=int, imax=False)

        self.label_spinINF = Label(self, label=f'{lim_grow} :: Unlimited')
        self.spinINF = Spinbox(self, values=lim_grow)


class NB_Center_Combobox(FrameUnlabelled):
    layout = 'x2E'
    wstate_single = 'choice'

    def setup_widgets(self):
        choices = spec.StaticList(('Choice %d' % n for n in range(5)), defaultIndex=3)

        vcb = self.var(var.String, name='choice')

        self.label_choiceRO = Label(self, label='CB',
                                    image=self.wimage('error-s16'),
                                    labelPosition=CP.S)
        self.choiceRO = Combobox(self, variable=vcb, values=choices)  # label='CB'

        self.label_choiceRW = Label(self, label='CB [RW]',
                                    image=self.wimage('warning-s16'),
                                    labelPosition=CP.E)
        self.choiceRW = Combobox(self, variable=vcb, values=choices,
                                 readonly=False)  # label='CB [RW]'

        self.choice_reset = Button(self, label='CB: Set Last', image=self.wimage('info-s16'))
        self.choice_reset.onClick = self.choiceRO.eSet(choices[-1])


class NB_Center_Radio(FrameUnlabelled):
    layout = 'x3E'
    wstate_single = 'radio'

    def setup_widgets(self):
        choices = spec.StaticList(('%d' % n for n in range(1, 9 + 1)), defaultIndex=9 // 2)
        rvar = self.varSpecced(var.SpeccedString, name='radio', spec=choices)

        widgets = {}
        for c in choices.all():
            widgets[c] = Radio(self, label=f'§ {c} §',
                               variable=rvar, value=c)
        widgets[':button'] = Button(self, label='Check State')
        widgets[':button'].onClick = self.onCheckState
        return widgets

    def onCheckState(self):
        logger.debug('State: %s', self.wstate)
        for wname, w in self.widgets.items():
            if not wname.startswith(':'):
                logger.debug('- %s: %s', w['text'], w.isSelected())


class NB_Center_RadioFrames_Inner(FrameRadio):
    wstate_single = 'inner'

    def setup_widgets(self, n):
        self.lbl = Label(self, label=f'Inner\nRadio Frame\n{n}')
        self.inner = ListFrame_Inner(self, label=n)


class NB_Center_RadioFrames_FInner(FrameStateful):
    layout = tk.HORIZONTAL

    def setup_widgets(self, rvar):
        widgets = {}
        for c in rvar.spec.all():
            widgets[f'f:{c}'] = NB_Center_RadioFrames_Inner(self, label=f'Frame {c}',
                                                            rvariable=rvar, rvalue=c,
                                                            n=c)
        return widgets


class NB_Center_RadioFrames(FrameUnlabelled):
    layout = 'x2E'

    def setup_widgets(self):
        choices = spec.StaticList(iter(('LeftSide', 'RightSide')), defaultIndex=0)
        rvar = self.varSpecced(var.SpeccedString, name='frame', spec=choices)

        widgets = {}
        for c in choices.all():
            widgets[f'r:{c}'] = Radio(self, label=f'Radio {c}',
                                      variable=rvar, value=c)
        widgets['finner'] = NB_Center_RadioFrames_FInner(self, label='Stateful', rvar=rvar)
        return widgets

    def setup_defaults(self):
        self.pgrid_r(*(w for wname, w in self.widgets.items() if wname.startswith('r:')),  # Radio Buttons
                     weight=0)


class NB_Center_LabelAlignSL(FrameUnlabelled):
    layout = '3x5E'

    def setup_widgets(self):
        widgets = {}
        justifies = [None, *Justification]
        for justify in justifies:
            wkey = [
                'xpand',
                'justify' if justify is None else justify.name,
            ]
            widgets['_'.join(wkey)] = Label(self, label=' '.join(wkey), styleID='ShowBG|WarnFG',
                                            image=self.wimage('warning-s16'), labelPosition=CP.S,
                                            justify=justify)
        for expand in [True, False]:
            for justify in justifies:
                wkey = [
                    'X' if expand else 'x',
                    'justify' if justify is None else justify.name,
                ]
                widgets['_'.join(wkey)] = Label(self, label=' '.join(wkey), styleID='ShowBG',
                                                image=self.wimage('info-s16'), labelPosition=CP.S,
                                                justify=justify, expand=expand)
        return widgets

    def setup_layout(self, layout):
        for w in self.widgets.values():
            w.grid(padx=2, pady=2)


class NB_Center_LabelAlignML(FrameUnlabelled):
    layout = '4x6S'

    def setup_widgets(self):
        widgets = {}
        for anchor in [None, CP.N, CP.S, CP.E, CP.W, CP.center]:
            for justify in [None, Justification.Left, Justification.Center, Justification.Right]:
                wkey = [
                    'anchor' if anchor is None else anchor.name,
                    'justify' if justify is None else justify.name,
                ]
                widgets['_'.join(wkey)] = Label(self, label='\n'.join(wkey), styleID='ShowBG',
                                                anchor=anchor, justify=justify)
        return widgets

    def setup_layout(self, layout):
        for w in self.widgets.values():
            w.grid(padx=2, pady=2)


class NB_Center(Notebook):
    def setup_tabs(self):
        return {
            'cb': Notebook.Tab('Combobox', NB_Center_Combobox(self)),
            'spin': Notebook.Tab('Spinbox', NB_Center_Spinbox(self)),
            'label_align:sl': Notebook.Tab('Label Align:SL', NB_Center_LabelAlignSL(self)),
            'label_align:ml': Notebook.Tab('Label Align:ML', NB_Center_LabelAlignML(self)),
            'radio': Notebook.Tab('Radio', NB_Center_Radio(self)),
            'frame:radio': Notebook.Tab('RadioFrames', NB_Center_RadioFrames(self)),
        }

    def setup_adefaults(self):
        self.wselect('label_align:sl')


class RW(RootWindow):
    # "TNotebook.tabplacement" is undocumented and buggy, should start with the "opposite" of "tabposition"
    # - See https://stackoverflow.com/a/76007959/12287472
    styleIDs = {
        'TabCenter.TNotebook': {'tabposition': tk.N},
        'TabV_W.TNotebook': {'tabposition': tk.W + tk.N, 'tabplacement': tk.N + tk.EW},
        'ReadonlyEmphasis.TCheckbutton': {},
        'ShowBG.TLabel': {'background': DStyle.Color_BG_Selected},
        'WarnFG.TLabel': {'foreground': 'orange'},
        'FakeDisabled.TLabel': {'foreground': DStyle.Color_FG_Disabled},
        'Small.TButton': {
            'font': SStyle.Font_Button_Small,
            'padding': SStyle.Size_PadButton_Small,
        },
    }

    def setup_widgets(self):
        vc = self.var(var.Boolean, name='bool', value=True)

        self.b1 = Button(self, label='B1')
        self.c1 = Checkbox(self, label='Checkbox1')
        self.bE1 = Button(self, label='Set "example"')
        self.b2 = Button(self, label='Debug')
        self.c2ro = Checkbox(self, label='RO "bool"', readonly=True, variable=vc)
        self.c2rw = Checkbox(self, label='RW "bool"', readonly=False, variable=vc)
        self.e1 = Entry(self, expand=True)  # label='Entry1'
        self.lbs = LuftBaloons(self)
        self.nb_center = NB_Center(self)
        self.ubox = UpstreamBool(self, label='Upstream', labelAnchor=CP.S,
                                 what_bool=vc)
        self.nb_center_label = Label(self, label='↰ ↑ ↱', styleID='FakeDisabled')  # Placeholder to keep the layout
        self.lf = ListFrame(self, cbox1=self.c1.variable)

        self.txt = TextEditor(self)
        self.nb = NB(self)
        self.arbre = TreeExample(self, label=Tree.Column('Label', image=self.wimage('warning-s16')), columns={
            'number': Tree.Column('Number', image=self.wimage('info-s16'), nameAnchor=CP.W, cellAnchor=CP.E),
        }, columns_stretch=None, columns_autosize=None)  # For Test: columns_stretch=['number'])

    def setup_defaults(self):
        logger.debug('Setup arbre state:')
        self.arbre.wstate = [
            Tree.Element('First', ['1'], image=self.wimage('warning-s16')),
            Tree.Element('Second', ['2'], image=self.wimage('warning-s16'), children=[
                Tree.Element('Second.One', ['21'], image=self.wimage('error-s16')),
            ]),
            Tree.Element('Third', ['3'], image=self.wimage('warning-s16'), children=[
                Tree.Element('Third.One', ['31']),
                Tree.Element('Third.Two', ['32'], image=self.wimage('error-s16'), children=[
                    Tree.Element('Third.Two.One', ['321']),
                    Tree.Element('Third.Two.Two', ['322'], image=self.wimage('warning-s16')),
                    Tree.Element('Third.Two.3', ['323'], image=self.wimage('error-s16')),
                ]),
                Tree.Element('Third.Tee', ['33']),
            ]),
            Tree.Element('Tenth', ['10'], image=self.wimage('warning-s16')),
        ]

    def setup_adefaults(self):
        logger.debug('Setup events')
        self.b1.onClick = self.c1.toggle
        self.bE1.onClick = self.ask_contents
        self.b2.onClick = self.debug
        logger.debug('Setup bindings')
        BindingGlobal(self, '<F4>', lambda e: self.debug(),
                      immediate=True, description='Debug')
        logger.debug('Setup traces')
        self.c2ro.trace(self.onTraceBool, trace_initial=True)
        self.trace(self.onTraceRoot)

        logger.debug('Global Bindings:')
        for bname, B in self._bindings_global.items():
            logger.debug('- %s: %s%s', bname, '' if B else '[Disabled] ', B.description)

    def ask_contents(self):
        string = tk.simpledialog.askstring('Set Contents', f'Set the "{self.e1.label}" contents')
        if string is not None:
            self.e1.wstate = string

    def debug(self):
        from pprint import pformat
        logging.info('=> State @ %s[%r]', self, self)
        for line in pformat(self.wstate_get()).splitlines():  # No `.wstate` for better tracebacks
            logging.info('%s', line)
        # logging.info('=> State @ ubox')
        # for line in pformat(self.ubox.wstate).splitlines():
        #     logging.info('%s', line)
        # logging.info('=> State @ lf.cLst')
        # for line in pformat(self.lf.cLst.wstate).splitlines():
        #     logging.info('%s', line)
        # logging.info('=> State @ nb[c:lc]')
        # for line in pformat(self.nb.wtab('c:lc').wstate).splitlines():
        #     logging.info('%s', line)
        logging.info('=> State Set')
        new = self.wstate
        for b in ('0', '12'):
            new['lbs'][f'lb:{b}'] = not new['lbs'][f'lb:{b}']
        assert 'lb:1' not in new['lbs']  # Ignore the second checkbox
        self.wstate = new
        logging.info('=> GUI States')
        logging.info('   GUI State @ %s[%r]', self, self)
        for line in pformat(self.gstate).splitlines():
            pass  # logging.debug('| %s', line)
        logging.info('   GUI State @ c2ro')
        for line in pformat(self.c2ro.gstate).splitlines():
            pass  # logging.debug('| %s', line)
        logging.info('   GUI State @ c2rw')
        for line in pformat(self.c2rw.gstate).splitlines():
            pass  # logging.debug('| %s', line)
        logging.info('   GUI State @ nb_center')
        for line in pformat(self.nb_center.gstate).splitlines():
            pass  # logging.debug('| %s', line)
        logging.info('   GUI State @ e1')
        for line in pformat(self.e1.gstate).splitlines():
            pass  # logging.debug('| %s', line)
        logging.info('   GUI State @ txt.txt')
        for line in pformat(self.txt.txt.gstate).splitlines():
            pass  # logging.debug('| %s', line)
        logger.info('=> Window State')
        logger.debug('   %r', self.rgstate)
        # self.set_gui_state(enabled=True, valid=True)  # Invalid Target
        # logging.info('=> NB')
        # for tn, ti in self.nb.wtabs.items():
        #     logging.debug(f'| {tn}: {ti}')
        logging.info('=> GridSize')
        logging.debug('  %s', self.txt.gsize)

    def onTraceRoot(self, var, etype):
        logger.critical('Changed Container "%s" = %s @ %s',
                        var.cwidget,
                        var.get(),
                        datetime.now().isoformat(' ', timespec='microseconds'),
                        )

    def onTraceBool(self, var, etype):
        bool_state = var.get()
        bool_when = 'Initial' if etype is None else 'Trigger'
        logger.debug('Variable "%s" @ %s: %s', fn.vname(var), bool_when, bool_state)


def entrypoint():
    '''
    Main entrypoint to be configured
    '''
    # ./showcase-images
    default_images = Path(__file__).parent / 'showcase-images'

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=dedent('''
        Showcase for tkmilan module
        '''),
        # epilog=f'Version {PROJECT_VERSION}',
    )
    # Automatic Tab Completion
    # - Mark certain arguments with:
    #   - `parser.add_argument(...).complete = shtab.FILE`: Complete file names
    #   - `parser.add_argument(...).complete = shtab.DIRECTORY`: Complete directory names
    shtab.add_argument_to(parser, '--generate-shtab-completion', help=argparse.SUPPRESS)

    # parser.add_argument('--version', action='version', version=PROJECT_VERSION)
    parser.add_argument('-v', '--verbose', dest='loglevel',
                        action='store_const', const=logging.DEBUG, default=logging.INFO,
                        help='Add more details to the standard error log')
    parser.add_argument('--debug', action='store_true',
                        help=argparse.SUPPRESS)
    parser.add_argument('--images', type=Path, default=default_images,
                        help='Image Folder to Load. Defaults to %(default)s').complete = shtab.DIRECTORY
    parser.add_argument('--no-images', action='store_const',
                        dest='images', const=None,
                        help='Do not load any images')

    args = parser.parse_args()

    # Logs
    logs_fmt = '%(levelname)-5.5s %(name)s@%(funcName)s| %(message)s'
    try:
        import coloredlogs  # type: ignore
        coloredlogs.install(level=args.loglevel, fmt=logs_fmt)
    except ImportError:
        logging.basicConfig(level=args.loglevel, format=logs_fmt)
    logging.captureWarnings(True)
    # # Silence spammy modules, even in verbose mode
    if not args.debug and args.loglevel == logging.DEBUG:
        for dmodule in MODULES_VERBOSE:
            logging.getLogger(f'{__package__}.{dmodule}').setLevel(logging.INFO)

    # Widget Tester / Showcase
    r = RW(imgfolder=args.images)
    logger.debug('Screen Size: %r', r.size_screen)
    logger.debug('         /2: %r', r.size_screen.reduce(2))
    r.mainloop()

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(entrypoint())
