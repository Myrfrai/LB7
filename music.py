import pygame as pg
import os

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Music player')

play_img = pg.image.load('music_assets/play.png')
stop_img = pg.image.load('music_assets/stop.png')
previous_img = pg.image.load('music_assets/previous.png')
next_img = pg.image.load('music_assets/next.png')

play_img = pg.transform.scale(play_img, (100, 100))
stop_img = pg.transform.scale(stop_img, (100, 100))
previous_img = pg.transform.scale(previous_img, (100, 100))
next_img = pg.transform.scale(next_img, (100, 100))

music_folder = 'songs/'
playlist = [f for f in os.listdir(music_folder) ]
cur_song= 0

def play_music():
    if playlist:
        pg.mixer.music.load(os.path.join(music_folder, playlist[cur_song]))
        pg.mixer.music.play(0)

class Button():
    def __init__(self, image, x, y, action=None, toggle_images=None):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.clicked = False
        self.toggle_images = toggle_images
        self.toggled = False
        self.action = action 

    def draw(self):
        pos = pg.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True

                if self.toggle_images:
                    self.toggled = not self.toggled
                    self.image = self.toggle_images[self.toggled]

                if self.action:
                    self.action() 

            if not pg.mouse.get_pressed()[0]:
                self.clicked = False    

        screen.blit(self.image, self.rect.topleft)

is_paused = False 

def toggle_play():
    global is_paused

    if pg.mixer.music.get_busy(): 
        pg.mixer.music.pause()
        is_paused = True
        play_button.image = play_button.toggle_images[True] 
    elif is_paused: 
        pg.mixer.music.unpause()
        is_paused = False
        play_button.image = play_button.toggle_images[False] 
    else:  
        play_music()
        play_button.image = play_button.toggle_images[True]  



def next_song():
    global cur_song
    if playlist:
        cur_song = (cur_song + 1) % len(playlist)
        play_music()

def previous_song():
    global cur_song
    if playlist:
        cur_song = (cur_song - 1) % len(playlist)
        play_music()

previous_button = Button(previous_img, 180, 200, action=previous_song)
play_button = Button(play_img, 330, 200, action=toggle_play, toggle_images=(play_img, stop_img))
next_button = Button(next_img, 480, 200, action=next_song)

done = False
while not done:
    screen.fill((255, 255, 255))

    previous_button.draw()
    play_button.draw()
    next_button.draw()


        #todo: add more buttons for volume control, shuffle, repeat, etc.
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                previous_song()
            elif event.key == pg.K_RIGHT:
                next_song()
            elif event.key == pg.K_SPACE:        
                toggle_play()

    pg.display.flip()

pg.quit()
