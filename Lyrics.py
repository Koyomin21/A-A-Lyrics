import os
import requests
from bs4 import BeautifulSoup
import csv
from tkinter import * 
from PIL import *
from PIL import Image, ImageTk
from utils import *
from io import BytesIO
from urllib.request import urlopen




def save():
    text=lyric.get(1.0,END)
    name_of_file=artist.get()+" "+song.get()
    if file_type.get() == 0:
        name_of_file = name_of_file + ".cvg"    
        f = open(name_of_file,"w", encoding='utf-8')
        f.write(text)
        f.close()
    if file_type.get() == 1:
        name_of_file = name_of_file + ".txt"    
        f = open(name_of_file,"w", encoding='utf-8')
        f.write(text)
        f.close()
    if file_type.get() == 2:
        name_of_file = name_of_file + ".doc"
        f = open(name_of_file,"w", encoding='utf-8')
        f.write(text)
        f.close()
    


    def search(event=None):



        if song.get() and artist.get():
            song_info = get_song_info(song.get())
            # artist_info = get_artist_info(artist.get())
            artist_info = get_artist_id(artist_name=artist.get())
            

            if check_artist(artist_info,song_info['response']['hits']):
                artist_info = get_artist_info(artist_info)
            else:
                print('There\'s no such song with this author')#make a taost
                return
                
        elif song.get() and len(artist.get()) ==0:#make a better check for empty string
            
            song_info = get_song_info(song.get())
            artist_info = get_artist_info(artist_id=song_info['response']['hits'][0]['result']['primary_artist']['id'])

        elif len(song.get())==0 and artist.get():
            artist_info = get_artist_info(artist_name=artist.get())
            song_info = get_song_info(artist.get())
        
        elif song.get() == artist.get() == None:
            return



    
    lyrics = get_lyric(song_info['response']['hits'][0]['result']['url'])

    lyric.delete(0.0,END)
    lyric.insert(0.0,lyrics)
    
    info = artist_info['response']['artist']['description']['plain']
    img_url = artist_info['response']['artist']['image_url']
    artist.delete(0, END)
    artist.insert(0,artist_info['response']['artist']['name'])
    song.delete(0, END)
    song.insert(0,song_info['response']['hits'][0]['result']['title'])
    

    response = requests.get(img_url)
    img_data = response.content
    img2 = Image.open(BytesIO(img_data))
    img2 = img2.resize((190, 190), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)

    panel.configure(image= img2)
    panel.image = img2

    info_text = Text(window, font = 'helvatica 12', width = 45, height = 12, bg = 'gray22', fg= 'white', bd =1)
    info_text.insert(1.0,info)
    info_text.place(x=10, y= 450)

    
    artist_name.set(artist.get())
    if len(artist.get())>17:
        artist_name.set(artist.get()[:17]+'\n'+artist.get()[17:])
        

def on_enter(e):
    btn_save['background'] = 'white smoke'

def on_leave(e):
    btn_save['background'] = 'snow3'

def on_enter1(e):
    btn_search['background'] = 'white smoke'

def on_leave1(e):
    btn_search['background'] = 'snow3'

def about_program():
    window_about_program = Toplevel(window)
    window_about_program.title('About program')
    window_about_program.geometry('520x580+500+150')
    window_about_program['bg']= 'gray22'
    title_about_program = Label(window_about_program,text = 'A&A Lyrics',font= 'helvatica 26',bg= 'gray22',fg= 'white')
    title_about_program.place(x=180, y =10)
    info_program = """A&A Lyrics is an application with some functionality. The main one is finding the lyrics by artist and title of his song. (input fields are white, in the left corner of the window). However, it is not necessary to enter all the fields, the application can find a song by only one name or artist name.
After the request, the lyrics and information about the artist and his photo are displayed. You can also save the lyrics to a file (the format can be selected in the toolbar, but the default is "doс").
There are additional functions in the toolbar such as "exit" and others.
Enjoy your use!"""
    label_about_program = Text(window_about_program, font= 'helvatica 18',bg= 'gray22',fg= 'white',bd =0,width =36, height = 18 )
    label_about_program.place(x=10,y=50)
    label_about_program.insert(1.0,info_program)

def create_window(title,geometry,bg_color):
    window = Tk() 
    window.title(title) 
    window.geometry(geometry) 
    window['bg'] = 'gray22'
    return window


window = create_window(title="A&A Lyrics",geometry='1020x680+500+150',bg_color='gray22')


ex = BooleanVar()#перменная для функции выхода программы
file_type = IntVar()#перемення для определения формата файла в котором мы будем сохранять лирикс
file_type.set(2)


mainmenu = Menu(window)
window.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)

filemenu2= Menu(filemenu, tearoff=0)
filemenu2.add_radiobutton(label='cvg',value =0,variable=file_type) #параметры для определения формата файла, который выберет юзер
filemenu2.add_radiobutton(label='txt',value =1,variable=file_type) #параметры для определения формата файла, который выберет юзер
filemenu2.add_radiobutton(label='doc',value =2,variable=file_type) #параметры для определения формата файла, который выберет юзер
filemenu.add_cascade(label = 'Format...', menu=filemenu2)
filemenu.add_separator()
filemenu.add_checkbutton(label = 'Exit', offvalue = 0, onvalue = 1,variable= ex, command = window.destroy)


helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="About program", command = about_program)
helpmenu.add_command(label="Donate")
 
mainmenu.add_cascade(label="File", menu=filemenu)
mainmenu.add_cascade(label="reference", menu=helpmenu)

filemenu.config(bg= 'gray', foreground = 'white',activeforeground = 'white', activebackground = 'gray22')
helpmenu.config(bg= 'gray', foreground = 'white',activeforeground = 'white', activebackground = 'gray22')
filemenu2.config(bg= 'gray', foreground = 'white',activeforeground = 'white', activebackground = 'gray22')








scrl = Scrollbar(window, width = 25) 
scrl.pack(side=RIGHT, fill=Y)

lyric = Text(window, height = 27, width = 33,wrap=WORD,yscrollcommand=scrl.set, bg = 'gray22',fg = 'white' ,borderwidth = 1, font ='helvetica 16')#переменная h=38
lyric.place (x = 500, y =10)
btn_save = Button(window,font = 'Purisa 14', text = 'save', command=save,bg= 'snow3',relief =  FLAT)
btn_save.place(x=440, y =580)#y450
btn_save.bind("<Enter>", on_enter)
btn_save.bind("<Leave>", on_leave)

scrl.config(command=lyric.yview)




response = requests.get('https://avatanplus.com/files/resources/original/5759b69c2046c155367151e4.png')
img_data = response.content
img = Image.open(BytesIO(img_data))
img = img.resize((190, 190), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img) 
panel =Label(window, image=img)
panel.place(x=10, y=250)






icon1 = Label(window, text = '🎶', bg= 'gray22', fg = 'purple',font = 'helvetica 25')
icon1.place(x=125, y=5)
icon1 = Label(window, text = '🎶', bg= 'gray22', fg = 'purple',font = 'helvetica 25')
icon1.place(x=320, y=5)

icon2 =Label(window, text = '🔴', bg= 'gray22', fg = 'red',font = 'helvetica 15')
icon2.place(x=6, y= 71)
icon2 =Label(window, text = '🔴', bg= 'gray22', fg = 'red',font = 'helvetica 15')
icon2.place(x=6, y= 126)





title = Label(window,text = 'A&A Lyrics', font = 'helvetica 25', bg = 'gray22', fg= 'white' )
title.place(x=160, y =10)





label1 = Label(window,text = 'Enter artist or singer:', font = 'helvetica 18', bg = 'gray22', fg = 'white')
label2 = Label(window, text = 'Enter song title:', font = 'helvetica 18', bg ='gray22', fg = 'white')

label1.place(x=30, y=73)
label2.place (x=30,y=128)



artist = Entry(window,font = 'helvetica 15')
song = Entry(window,font = 'helvetica 15')



artist.place(x=260, y =77)
song.place(x=260, y=132)



btn_search = Button(window,font = 'helvetica 18', text = 'SEARCH',bg= 'snow3',relief =  FLAT, command = search)
btn_search.place(x=180, y =183)
btn_search.bind("<Enter>", on_enter1)
btn_search.bind("<Leave>", on_leave1)

window.bind('<Return>',search)

artist_name = StringVar()
artist_name_label = Label(window,textvariable = artist_name,font = 'helvetica 24', bg= 'gray22', fg = 'white')
artist_name_label.place (x=220, y=260)

window.mainloop()