# Write your solution here:
class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year
    
    def print_book(self):
        print(f'{self.author}: {self.name} ({self.year})')

    def print_blurb(self):
        print(f'The genre of the book {self.name} is {self.genre}')

if __name__ == '__main__':
    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
    python.print_book()
    everest.print_blurb()
    print(f"{python.author}: {python.name} ({python.year})")
    print(f"The genre of the book {everest.name} is {everest.genre}")