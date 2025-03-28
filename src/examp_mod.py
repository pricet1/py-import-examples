# Module: examp_mod
# This module is imported by examp1.py and examp2.py

MSG = 'Thank you for importing (or directly running) the module examp_mod'

def yolo(x: int = 9, creature: str = 'cat') -> None:
  print(f"\nIf you're the {creature}, you only live {x} times.\n")

if __name__ == '__main__':
  yolo(10000)
