import json
from datetime import datetime

def load_books():
    """Загружает список книг из JSON‑файла."""
    try:
        with open('books.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_books(books):
    """Сохраняет список книг в JSON‑файл."""
    with open('books.json', 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def add_book(books):
    pass

def list_books(books):
    pass

def show_average_rating(books):
    pass

def show_author_stats(books):
    pass

def delete_book(books):
    pass

def main():
    books = load_books()
    while True:
        print("\n" + "="*40)
        print("ТРЕКЕР ПРОЧИТАННЫХ КНИГ")
        print("="*40)
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        choice = input("\nВыберите действие (1–6): ").strip()

        if choice == '1':
            add_book(books)
        elif choice == '2':
            list_books(books)
        elif choice == '3':
            show_average_rating(books)
        elif choice == '4':
            show_author_stats(books)
        elif choice == '5':
            delete_book(books)
        elif choice == '6':
            print("До свидания!")
            break
        else:
            print("Ошибка: выберите действие от 1 до 6.")

if __name__ == "__main__":
    main()
