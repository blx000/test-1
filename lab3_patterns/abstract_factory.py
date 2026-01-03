from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class WindowsButton(Button):
    def render(self) -> str:
        return "Windows Button"


class WindowsCheckbox(Checkbox):
    def render(self) -> str:
        return "Windows Checkbox"


class MacButton(Button):
    def render(self) -> str:
        return "Mac Button"


class MacCheckbox(Checkbox):
    def render(self) -> str:
        return "Mac Checkbox"


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()
