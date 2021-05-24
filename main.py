import tkinter as tk
from tkinter.constants import NE, TOP
import mysql.connector as sqlc

#variales
row = 0
col = 0 
data = None
label = None

#display tkinter screen
main_win = tk.Tk()
main_win.title("title")
main_win.attributes("-fullscreen",True)
main_win['background'] = "#1CAA9C"

searchBox_text = tk.StringVar()
RadioButtonVar = tk.IntVar()
#database connectivity
conn = sqlc.connect(host = "localhost", user = "root" , passwd = "Danger@123" , database = "dbmsa1")
cursor = conn.cursor()

def books_table_head():
    #year
    tableHead_year = tk.Label(frame,text = "YEAR",height = 3,width = 25,wraplength = 150, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_year.grid(row = 0,column = 0)

    #title
    tableHead_title = tk.Label(frame,text = "TITLE",height = 3,width = 25,wraplength = 150, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_title.grid(row = 0,column = 1)  
    
    #cost
    tableHead_cost = tk.Label(frame,text = "COST",height = 3,width = 25,wraplength = 150, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_cost.grid(row = 0,column = 2)  
    
    #isbn number
    tableHead_isbn = tk.Label(frame,text = "ISBN",height = 3,width = 25,wraplength = 150, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_isbn.grid(row = 0,column = 3)
    
    #author name
    tableHead_Author_name = tk.Label(frame,text = "AUTHOR NAME",height = 3,width = 25,wraplength = 150, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_Author_name.grid(row = 0,column = 4)
def author_table_head():
    tableHead_AuthorName = tk.Label(frame,text = "Author Name",height = 3,width = 25,wraplength = 150, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_AuthorName.grid(row = 0,column = 0)

    tableHead_address = tk.Label(frame,text = "Address",height = 3,width = 25,wraplength = 150, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_address.grid(row = 0,column = 1)

    tableHead_url = tk.Label(frame,text = "URL",height = 3,width = 25,wraplength = 150, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_url.grid(row = 0,column = 2)    

    tableHead_title = tk.Label(frame,text = "Title",height = 3,width = 25,wraplength = 150, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_title.grid(row = 0,column = 3)   
def publish_table_head():
    tableHead_name = tk.Label(frame,text = "Publisher Name",height = 3,width = 25,wraplength = 150, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_name.grid(row = 0,column = 0)

    tableHead_address = tk.Label(frame,text = "address",height = 3,width = 25,wraplength = 150, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_address.grid(row = 0,column = 1)

    tableHead_phone = tk.Label(frame,text = "phone no.",height = 3,width = 25,wraplength = 150, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_phone.grid(row = 0,column = 2)

    tableHead_URL = tk.Label(frame,text = "URL",height = 3,width = 25,wraplength = 100, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_URL.grid(row = 0,column = 3)

    tableHead_title = tk.Label(frame,text = "Title",height = 3,width = 25,wraplength = 100, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_title.grid(row = 0,column = 4)
def warehouse_table_head():
    tableHead_code = tk.Label(frame,text = "Warehouse code",height = 3,width = 25,wraplength = 150, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_code.grid(row = 0,column = 0) 

    tableHead_phone = tk.Label(frame,text = "Phone",height = 3,width = 25,wraplength = 150, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_phone.grid(row = 0,column = 1) 

    tableHead_address = tk.Label(frame,text = "Address",height = 3,width = 25,wraplength = 150, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_address.grid(row = 0,column = 2) 

    tableHead_stock = tk.Label(frame,text = "Stock",height = 3,width = 25,wraplength = 150, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_stock.grid(row = 0,column = 3) 

    tableHead_title = tk.Label(frame,text = "Title",height = 3,width = 25,wraplength = 100, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_title.grid(row = 0,column = 4) 
def customer_table_head():
    tableHead_name = tk.Label(frame,text = "customer name",height = 3,width = 25,wraplength = 150, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_name.grid(row = 0,column = 0) 

    tableHead_mail = tk.Label(frame,text = "Email",height = 3,width = 25,wraplength = 150, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_mail.grid(row = 0,column = 1) 

    tableHead_phone = tk.Label(frame,text = "Phone no.",height = 3,width = 25,wraplength = 150, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_phone.grid(row = 0,column = 2)

    tableHead_basket_id = tk.Label(frame,text = "Basket_id",height = 3,width = 25,wraplength = 150, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_basket_id.grid(row = 0,column = 3) 

    tableHead_title = tk.Label(frame,text = "Title",height = 3,width = 25,wraplength = 150, justify = "right",bg = "#1CAA9C",font = bold_text)
    tableHead_title.grid(row = 0,column = 4)  

def search():
    global label
    empty_frame()
    # table_head()
    global data
    row = 1
    col = 0
    searchText = searchBox_text.get()
    SearchBox.delete(-1,"end")

    if RadioButtonVar.get() == 1:
        query = "select * from books where title = '"+searchText+"'"
        cursor.execute(query)
        data = cursor.fetchall()
        books_table_head()
        for r in data:
            for c in r:
                label = tk.Label(frame,text = str(c),bg = "#1CAA9C",wraplength=150)
                # label.config(text=str(c))
                label.grid(row = row,column = col)
                label.configure(font = Font_tuple)
                col += 1
            col = 0
            row += 1 
    if RadioButtonVar.get() == 2:
        query = "select author.Author_name,author.address,author.URL,books.title from author left join books on author.Author_name =  books.Author_name where author.Author_name = '"+ searchText  +"'"
        cursor.execute(query)
        data = cursor.fetchall()  

        # # table_head() 
        author_table_head()
        for r in data:
            for c in r:
                label = tk.Label(frame,text = str(c),bg = "#1CAA9C",wraplength=150)
                # label.config(text=str(c))
                label.grid(row = row,column = col)
                label.configure(font = Font_tuple)
                col += 1
            col = 0
            row += 1 
    if RadioButtonVar.get() == 3:
        query = "select published_by.pname,published_by.address,published_by.phone,published_by.url,books.title from published_by left join books on published_by.isbn = books.isbn where published_by.pname = '"+searchText+"'"
        cursor.execute(query)
        data = cursor.fetchall()
        publish_table_head()
        for r in data:   
            for c in r:
                label = tk.Label(frame,text = str(c),bg = "#1CAA9C",wraplength=150)
                # label.config(text=str(c))
                label.grid(row = row,column = col)
                label.configure(font = Font_tuple)
                col += 1
            col = 0
            row += 1
    if RadioButtonVar.get() == 4:
        query = "select warehouse.code,warehouse.phone,warehouse.address,warehouse.stock,books.title from warehouse left join books on warehouse.isbn = books.isbn where books.title = '"+searchText+"'"
        cursor.execute(query)
        data = cursor.fetchall()
        warehouse_table_head()
        for r in data:   
            for c in r:
                label = tk.Label(frame,text = str(c),bg = "#1CAA9C",wraplength=150)
                # label.config(text=str(c))
                label.grid(row = row,column = col)
                label.configure(font = Font_tuple)
                col += 1
            col = 0
            row += 1
    if RadioButtonVar.get() == 5:
        query = "select customer.name,customer.email,customer.phone,shopping_basket.basket_id,books.title from customer join shopping_basket on customer.email = shopping_basket.email join books on shopping_basket.isbn = books.isbn where customer.name = '"+searchText+"'"
        cursor.execute(query)
        data = cursor.fetchall()
        customer_table_head()
        for r in data:   
            for c in r:
                label = tk.Label(frame,text = str(c),bg = "#1CAA9C",wraplength=150)
                # label.config(text=str(c))
                label.grid(row = row,column = col)
                label.configure(font = Font_tuple)
                col += 1
            col = 0
            row += 1

def empty_frame():
    global label
    # books_table_head()
    for r in range(11):
            for c in range(5):
                label = tk.Label(frame,text = "      ",height = 3,width = 25,wraplength = 150, justify = "right",bg = "#1CAA9C")
                label.grid(row = r,column = c)
                label.configure(font = Font_tuple) 

#font widget
Font_tuple = ("san sarif", 12)
medium_font = ("san sarif" , 25)
small_font = ("sansarif",14)
bold_text = ("san sarif",12,"bold")


#search frame
SearchFrame = tk.Frame(main_win)
SearchFrame.place(x = 450,y = 30)
#radiobutton frame
rd_frame = tk.Frame(main_win)
rd_frame.place(x=460,y=100)
#frame widget
frame = tk.Frame(main_win,bg="#1CAA9C")
frame.place(x=30,y=150)

#Entry widget
SearchBox = tk.Entry(SearchFrame,width=20,font = medium_font,textvariable = searchBox_text,bd=0)
SearchBox.grid(row =  0 , column = 0)

#button widget
button = tk.Button(SearchFrame,text = "click", command = search,height = 2,width = 12,bd=0)
button.grid(row =  0 , column = 1)

#radioButton 
books = tk.Radiobutton(rd_frame,text = "Books", variable = RadioButtonVar, value = 1,bg="#1CAA9C",font = Font_tuple)
books.grid(row = 0, column = 0)
books.select()
author = tk.Radiobutton(rd_frame,text = "Author", variable = RadioButtonVar, value = 2,bg="#1CAA9C",font = Font_tuple)
author.grid(row = 0, column = 1)
publish = tk.Radiobutton(rd_frame,text = "Publish", variable = RadioButtonVar, value = 3,bg="#1CAA9C",font = Font_tuple)
publish.grid(row = 0, column = 2)
warehouse = tk.Radiobutton(rd_frame,text = "warehouse", variable = RadioButtonVar, value = 4,bg="#1CAA9C",font = Font_tuple)
warehouse.grid(row = 0, column = 3)
customer = tk.Radiobutton(rd_frame,text = "customer", variable = RadioButtonVar, value = 5,bg="#1CAA9C",font = Font_tuple)
customer.grid(row = 0, column = 4)

close = tk.Button(main_win,text="close",height=3,width=10,command=main_win.destroy)
close.pack(side = TOP,anchor=NE)

# table_head()
# empty_frame()


main_win.mainloop()