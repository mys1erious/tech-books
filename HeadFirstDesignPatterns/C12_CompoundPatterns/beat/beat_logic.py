from abc import ABC, abstractmethod


class BeatModelInterface(ABC):
    @abstractmethod
    def initialize(self):
        ...

    @abstractmethod
    def on(self):
        ...

    @abstractmethod
    def off(self):
        ...

    @abstractmethod
    def set_bpm(self, bpm):
        ...

    @abstractmethod
    def register_observer(self, o):
        ...

    @abstractmethod
    def remove_observer(self, o):
        ...


class BeatModel(BeatModelInterface):
    def __init__(self):
        self.__sequencer = None
        self.__beat_observers = []
        self.__bpm_observers = []
        self.__bpm = 90

    def initialize(self):
        self.set_up_midi()
        self.build_track_and_start()

    def on(self):
        self.__sequencer.start()
        self.set_bpm(90)

    def off(self):
        self.set_bpm(0)
        self.__sequencer.stop()

    def set_bpm(self, bpm):
        self.__bpm = bpm
        self.__sequencer.set_tempo_in_bpm(self.bpm)
        self.notify_bpm_observers()

    @property
    def bpm(self):
        return self.__bpm

    def beat_event(self):
        self.notify_beat_observers()

    def register_observer(self, o):
        pass

    def remove_observer(self, o):
        pass


class DJView(BeatObserver, BPMObserver):
    def __init__(self, controller, model):
        # View code
        self.__model = model
        self.__controller = controller

        self.__model.register_observer(self)  # as BeatObserver
        self.__model.register_observer(self)  # as BPMObserver ?

        self.view_frame = None
        self.view_panel = None
        self.beat_bar = None
        self.bpm_output_label = None

        # Controller code
        self.bpm_label = None
        self.bpm_text_field = None
        self.set_bpm_button = None
        self.increase_bpm_button = None
        self.decrease_bpm_button = None
        self.menu_bar = None
        self.menu = None
        self.start_menu_item = None
        self.stop_menu_item = None

    # View code
    def create_view(self):
        # View logic here
        ...

    def update_bpm(self):
        bpm = self.__model.get_bpm()
        if bpm == 0:
            self.bpm_output_label.set_text('offline')
        else:
            self.bpm_output_label.set_text(f'Current BPM: {self.__model.get_bpm()}')

    def update_beat(self):
        self.beat_bar.set_value(100)

    # Controller code
    def create_controls(self):
        # Controller components here
        ...

    def enable_stop_menu_item(self):
        self.stop_menu_item.set_enabled(True)

    def disable_stop_menu_item(self):
        self.stop_menu_item.set_enabled(False)

    def enable_start_menu_item(self):
        self.stop_menu_item.set_enabled(True)

    def disable_start_menu_item(self):
        self.stop_menu_item.set_enabled(False)

    def action_performed(self, event):
        if event.get_source() == self.set_bpm_button:
            bpm = int(self.bpm_text_field.get_text())
            self.__controller.set_bpm(bpm)
        elif event.get_source() == self.increase_bpm_button:
            self.__controller.increase_bpm()
        elif event.get_source() == self.decrease_bpm_button:
            self.__controller.decrease_bpm()


class ControllerInterface(ABC):
    @abstractmethod
    def start(self):
        ...

    @abstractmethod
    def stop(self):
        ...

    @abstractmethod
    def increase_bpm(self):
        ...

    @abstractmethod
    def descrease_bpm(self):
        ...

    @abstractmethod
    def set_bpm(self, bpm):
        ...


class BeatController(ControllerInterface):
    def __init__(self, model):
        self.__model = model
        self.view = DJView(self, model)
        self.view.create_view()
        self.view.create_controls()
        self.view.disable_stop_menu_item()
        self.view.enable_start_menu_item()
        model.initialize()

    def start(self):
        self.__model.on()
        self.view.disable_start_menu_item()
        self.view.enable_stop_menu_item()

    def stop(self):
        self.__model.off()
        self.view.disable_stop_menu_item()
        self.view.enable_start_menu_item()

    def increase_bpm(self):
        bpm = self.__model.get_bpm()
        self.__model.set_bpm(bpm + 1)

    def descrease_bpm(self):
        bpm = self.__model.get_bpm()
        self.__model.set_bpm(bpm - 1)

    def set_bpm(self, bpm):
        self.__model.set_bpm(bpm)


class HeartModel:
    def get_heart_rate(self):
        ...

    def register_beat_observer(self):
        ...

    def register_bpm_observer(self):
        ...


class HeartAdapter(BeatModelInterface):
    def __init__(self, heart):
        self.__heart = heart

    def initialize(self):
        pass

    def on(self):
        pass

    def off(self):
        pass

    def set_bpm(self, bpm):
        pass

    @property
    def bpm(self):
        return self.__heart

    def register_observer(self, o):
        self.__heart.register_observer(o)

    def remove_observer(self, o):
        self.__heart.remove_observer(o)


class HeartController(ControllerInterface):
    def __init__(self, model):
        self.__model = model
        self.view = DJView(self, HeartAdapter(model))
        self.view.create_view()
        self.view.create_controls()
        self.view.disable_stop_menu_item()
        self.view.enable_start_menu_item()

    def start(self):
        pass

    def stop(self):
        pass

    def increase_bpm(self):
        pass

    def descrease_bpm(self):
        pass

    def set_bpm(self, bpm):
        pass


def dj_test():
    model = BeatModel()
    controller = BeatController(model)


def heart_test():
    heart_model = HeartModel()
    model = HeartController(heart_model)


if __name__ == '__main__':
    dj_test()
    # heart_test()
