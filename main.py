from Controller import Controller
from UIView import MenuUI
from KoleksiBuku import KoleksiBuku

book_titles = [
    "To Kill a Mockingbird",
    "1984",
    "The Great Gatsby",
    "Pride and Prejudice",
    "The Catcher in the Rye",
    "Harry Potter and the Sorcerer's Stone",
    "The Lord of the Rings",
    "The Hobbit",
    "Brave New World",
    "The Hunger Games"
]

koleksiBuku = KoleksiBuku(book_titles)

view = MenuUI()
controller = Controller(view,koleksiBuku)