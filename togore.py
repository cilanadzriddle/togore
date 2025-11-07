#!/usr/bin/env python3

from textual.app import App, ComposeResult
from textual.widgets import Footer, Static, Digits
from textual.reactive import reactive
import time
import argparse
import subprocess

parser = argparse.ArgumentParser(description='My first ever coding project!')
parser.add_argument('-t', '--title', type=str, help='Title of task')
parser.add_argument('-r', '--workhours', type=int, default=0, help='Work hours for task')
parser.add_argument('-m', '--workminutes', type=int, default=0, help='Work minutes for task')
parser.add_argument('-s', '--workseconds', type=int, default=0, help='Work seconds for task')
parser.add_argument('-R', '--resthours', type=int, default=0, help='Rest hours for task')
parser.add_argument('-M', '--restminutes', type=int, default=0, help='Rest minutes for task')
parser.add_argument('-S', '--restseconds', type=int, default=0, help='Rest seconds for task')
parser.add_argument('-c', '--cycles', type=int, default=0, help='Number of cycles, should default to one')
args = parser.parse_args()

total_work_time = (args.workseconds) + (args.workminutes * 60) + (args.workhours * 3600)
total_rest_time = (args.restseconds) + (args.restminutes * 60) + (args.resthours * 3600)
total_cycles = (args.cycles)

class Timer(Static):
    CSS_PATH = "togore.css"

    is_paused = reactive(False)
    work_time = reactive(total_work_time)
    is_work_mode = reactive(True)
    completed_cycles = reactive(1)

    if(total_cycles <= 0):
        status_message = reactive("WORK")
    else:
        status_message = reactive(f"WORK [1/{total_cycles}]")

    def compose(self) -> ComposeResult:
        yield Digits()
        yield Static(self.status_message, id="pomodoro_status",)

    def tick(self) -> None:
        if self.is_paused:
            return
        if total_cycles <= 0:
            self.work_time -= 1
            if not self.work_time:
                self.query_one(Static).update("END")
                self.remove_class("work")
                self.add_class("rest")
                self.tick_timer.stop()
                return
        else:
            self.work_time -= 1
            if not self.work_time:
                if self.is_work_mode == True:
                    self.work_time = total_rest_time
                    self.remove_class("work")
                    self.add_class("rest")
                    self.is_work_mode = False
                    self.query_one(Static).update(f"REST [{self.completed_cycles}/{total_cycles}]")
                else:
                    self.work_time = total_work_time
                    self.remove_class("rest")
                    self.add_class("work")
                    self.is_work_mode = True
                    self.completed_cycles += 1
                    self.query_one(Static).update(f"WORK [{self.completed_cycles}/{total_cycles}]")
                    if(self.completed_cycles == total_cycles + 1):
                        self.query_one(Digits).update(f"00:00:00")
                        self.query_one(Static).update("END")
                        self.remove_class("work")
                        self.add_class("rest")
                        self.tick_timer.stop()
                        return
                # self.tick_timer.stop()

    def watch_work_time(self, work_time: int) -> None:
        time, seconds = divmod(work_time, 60)
        hours, minutes = divmod(time, 60)
        self.query_one(Digits).update(f"{hours:02}:{minutes:02}:{seconds:02}")

    def on_mount(self) -> None:
        self.tick_timer = self.set_interval(1, self.tick)

class togore(App):
    CSS_PATH = "togore.css"
    is_paused = reactive("")
    paused = reactive(False)

    BINDINGS = [
        ("q", "pause_or_resume_timer", "Pause / resume timer"),
        ]

    def compose(self):
        yield Static(args.title, classes="title",)
        yield Timer(classes="work", id="main_timer")
        yield Static(self.is_paused, id="pause_status")
        yield Footer()

    def action_pause_or_resume_timer(self):
        timer_widget = self.query_one("#main_timer", Timer)
        timer_widget.is_paused = not timer_widget.is_paused

        if self.paused == False:
            self.query_one("#pause_status", Static).update(f"PAUSED")
            self.paused = True
        else:
            self.query_one("#pause_status", Static).update(f"")
            self.paused = False
    def on_mount(self) -> None:
        self.title = "Countdown Timer"

if __name__ == "__main__":
    app = togore()
    app.run()
