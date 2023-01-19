BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# func, returned string with text of page and her size
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    signs = '.-!?—,:;'
    size_chunk = size
    if len(text[start:]) <= size:
        size_chunk = len(text) - start
        return text[start: start + size_chunk], size_chunk
    for i in range(start + size - 1, start, -1):
        if text[i] in signs and text[i + 1] not in signs:
            break
        size_chunk -= 1
    return text[start: start + size_chunk], size_chunk


# func for creating dict of book
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='UTF-8') as file:
        text_book = file.read()
    start, number_page = 0, 1
    full_size = len(text_book)
    while full_size > start:
        text_chunk, size = _get_part_text(text_book, start, PAGE_SIZE)
        book[number_page] = text_chunk.strip()
        number_page += 1
        start += size


# calling func prepare_book to prepare a book from a text file
prepare_book(BOOK_PATH)

