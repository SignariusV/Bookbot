import os

BOOK_PATH = '..\\book\\book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    stop = start + size
    if len(text) <= stop:
        page = text[start:]
    else:
        for i in range(stop-1, start,-1):
            if text[i] in ',.!:;?':
                if text[i+1] in ',.!:;?':
                    continue
                page = text[start:i + 1]
                break
    return page, len(page)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    text=''
    with open(path, encoding='utf-8') as file:
        for line in file.readlines():
            text=text+line
    num_page=1
    while text:
        book[num_page]=_get_part_text(text, 0, PAGE_SIZE)[0].lstrip()
        stop=_get_part_text(text, 0, PAGE_SIZE)[1]
        text=text[stop:]
        num_page+=1



# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(os.getcwd(), BOOK_PATH))
