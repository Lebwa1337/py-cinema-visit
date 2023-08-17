class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_numer: int) -> None:
        print(f"Cleaner {self.name} is cleaning hall number {hall_numer}.")