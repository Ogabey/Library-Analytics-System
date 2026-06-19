from db import get_connection
from psycopg2.extras import RealDictCursor
def all_books():
    conn=get_connection()
    cur=conn.cursor()

    cur.execute("SELECT title, author, category, pages, puplish_year FROM books"
    )
    result = cur.fetchall()

    for book in result:
        print(book[0], book[1], book[2], book[3], book[4])

    cur.close()
    conn.close()

def search_id_book():
    conn=get_connection()
    cur=conn.cursor(cursor_factory=RealDictCursor)
    book_id=input("id kiriring:>")

    cur.execute("SELECT title, author, category, pages, puplish_year FROM books WHERE id=%s", (book_id,))

    natija=cur.fetchone()

    if natija:
        print(natija)
    else:
        print("bunaqa id mavjud emas")
        cur.close()
        conn.close()
def search_author_book():

    conn=get_connection()
    cur=conn.cursor(cursor_factory=RealDictCursor)
     
    book_author=input("kitob muallifini kliriting:>")

    cur.execute("SELECT title, author, category, pages, puplish_year FROM books WHERE author=%s",(book_author,))

    muallif=cur.fetchall()
    
    if muallif:
        for m in muallif:
           print(m)
    else:
        print("Bunaqa muallif topilmadi:()")
      

    cur.close()
    conn.close()
def min_paper():

    conn=get_connection()
    cur=conn.cursor(cursor_factory=RealDictCursor)
    
    min_son=int(input("min sahifa soni:>"))

    cur.execute("SELECT title, author, category, pages, puplish_year FROM books WHERE pages> %s",(min_son,))
    result=cur.fetchall()

    if result:
        for r in result:
            print(r)
    else:
        print("Mavjud emas")

    cur.close()
    conn.close()
def library_statistic():

    conn=get_connection()
    cur=conn.cursor(cursor_factory=RealDictCursor)
    
    statistika=""" SELECT COUNT(*) AS mavjud_kitoblar_soni,
      AVG(pages)AS urtacha_sahifa, 
      MAX(pages) AS katta_sahifali, 
      MIN(pages)AS kichik_sahifali,
      MIN(puplish_year) AS eski_kitob
      FROM books
      """
    cur.execute(statistika)

    result=cur.fetchone()

    print(result)

    cur.close()
    conn.close()




def famous_author():

    conn=get_connection()
    cur=conn.cursor(cursor_factory=RealDictCursor)
    
    famous=""" SELECT author AS muallif, 
      COUNT(*) AS kitoblar_soni
      FROM books 
      GROUP BY author 
      ORDER BY kitoblar_soni DESC
      LIMIT 1
      """
    cur.execute(famous)

    result=cur.fetchone()

    print(result)

    cur.close()
    conn.close()
    
famous_author()