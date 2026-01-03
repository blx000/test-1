class OldPrinter:
    def print_text(self, text: str):
        return f"Old printer: {text}"


class PrinterAdapter:
    def __init__(self, printer: OldPrinter):
        self.printer = printer

    def print(self, text: str):
        return self.printer.print_text(text)
