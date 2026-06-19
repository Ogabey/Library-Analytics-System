from book import (
    all_books,
    min_paper,
    search_author_book,
    search_id_book,
    library_statistic,
    famous_author
)

print(" Kitoblar ro'yxati ")
ruyxat=all_books
print(ruyxat)


print("Minimal sahifa")
minimal_sahifa=min_paper
print(minimal_sahifa)


print("Muallif bo'yicha qidirish ")
muallif_buyicha=search_author_book
print(muallif_buyicha)


print(" Kitob id orqali qidirish:")
kitob_id=search_id_book
print(search_id_book)


print("Kutubxona statistikasi")
kutubxona_statistika=library_statistic
print(library_statistic)


print("Eng ko'p kitob yozganyozuvchi")
kup_kitob=famous_author
print(famous_author)
