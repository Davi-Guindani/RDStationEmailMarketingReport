import matplotlib.pyplot as plt
import datetime as dt
from client import Client


class Graphic:
    def __init__(self, x_axis: list, y_axis: list, x_bar: list, y_bar: list, x_ticks: list, y_ticks: list, x_label: str,
                 f_name: str):
        self.X_AXIS = x_axis
        self.Y_AXIS = y_axis
        self.X_BAR = x_bar
        self.Y_BAR = y_bar
        self.X_TICKS = x_ticks
        self.Y_TICKS = y_ticks
        self.X_LABEL = x_label
        self.F_NAME = f_name

    def get_x_axis(self): return self.X_AXIS

    def set_x_axis(self, x_axis): self.X_AXIS = x_axis

    def get_y_axis(self): return self.Y_AXIS

    def set_y_axis(self, y_axis): self.Y_AXIS = y_axis

    def get_x_bar(self): return self.X_BAR

    def set_x_bar(self, x_bar): self.X_BAR = x_bar

    def get_y_bar(self): return self.Y_BAR

    def set_y_bar(self, y_bar): self.Y_BAR = y_bar

    def get_x_ticks(self): return self.X_TICKS

    def set_x_ticks(self, x_ticks): self.X_TICKS = x_ticks

    def get_y_ticks(self): return self.Y_TICKS

    def set_y_ticks(self, y_ticks): self.Y_TICKS = y_ticks

    def get_x_label(self): return self.X_LABEL

    def set_x_label(self, x_label): self.X_LABEL = x_label

    def get_f_name(self): return self.F_NAME

    def set_f_name(self, f_name): self.F_NAME = f_name

    def set_graphics_settings(self, campaign: dict, cliente: Client):
        fig, ax = plt.subplots(facecolor=cliente.get_background_color())
        ax.set_facecolor(cliente.get_background_color())

        ax.set_title(campaign['campaign_name'], color=cliente.get_first_color())

        p1 = ax.bar(self.get_x_bar(), self.get_y_bar(), color=cliente.get_second_color(), width=0.3)
        ax.bar_label(p1, color=cliente.get_second_color())

        ax.set_xticks(self.get_x_ticks(), color=cliente.get_first_color(), labels=self.get_x_ticks())
        ax.set_yticks(self.get_y_ticks(), color=cliente.get_first_color(), labels=self.get_y_ticks())

        ax.set_xlabel(self.get_x_label(), color=cliente.get_first_color())

        for direction in ['top', 'right', 'left', 'bottom']:
            ax.spines[direction].set_visible(False)

        fname = self.get_f_name() + cliente.get_name() + campaign['campaign_name'] + str(dt.date.today()) + ".png"
        plt.savefig(fname, dpi=300)
        plt.close(fig)
        return fname
