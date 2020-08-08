"""
«Есть два писателя, которые по очереди в течении определенного времени 
(у каждого разное) пишут в одну книгу. Данная книга очень популярна, 
у неё есть как минимум 3 фаната (читателя), которые ждут не дождутся, 
чтобы прочитать новые записи из неё. Каждый читатель и писатель – отдельный 
поток. Одновременно книгу может читать несколько читателей, но писать 
единовременно может только один писатель.»

"""

import threading
import os

book = os.path.join(os.getcwd(), 'Lesson 11','Book.txt')
mutex = threading.Lock()

class Author:
    last_part = 0
    def new_part_number():
        Author.last_part+=1
        return Author.last_part

    def __init__(self, name):
        self.name = name

    def write(self):
        global book
        mutex.acquire()
        with open(book, 'a', encoding='UTF-8') as f:
            f.write(f'Глава {Author.new_part_number()}, автор {self.name}\n')
        mutex.release()


class Fan:
    def __init__(self, name):
        self.name = name
        self.read_parts = 0
    def share_opinion(self):
        global book
        with open(book, 'r', encoding='UTF-8') as f:
            for part in f.readlines()[self.read_parts:]:
                print(f'{self.name}: {part[0:-1]}, просто великолепна!')
                self.read_parts+=1


author1 = Author('Толстой Л.Н.')
author2 = Author('Донцова Д.')
fan1 = Fan('Константин')
fan2 = Fan('Вася')
fan3 = Fan('Тайный поклонник')


auth1 = threading.Thread(target=author1.write()) 
auth2 = threading.Thread(target=author2.write())
rdr1 = threading.Thread(target=fan1.share_opinion())
rdr2 = threading.Thread(target=fan2.share_opinion())
rdr3 = threading.Thread(target=fan3.share_opinion())

auth1.start()
auth2.start()
rdr1.start()
rdr2.start()
rdr3.start()

auth1.join()
auth2.join()
rdr1.join()
rdr2.join()
rdr3.join()



# честно говоря, не очень понятно работает это или нет.
# Что такое .join()? В инете нашел что, 
        # "Вызов thread1.join() блокирует поток, в 
        # котором вы выполняете вызов, до тех пор, пока 
        # thread1 не будет завершен."
# но как это работает не понимаю.




