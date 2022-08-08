from tkinter import *
import settings
from cell import Cell


screen= Tk() # screen
screen.configure(bg="black") 
screen.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
screen.resizable(False,False) #screen no resizable

top_frame= Frame(       #change the settings in the top frame
    screen,
    bg="black", 
    width= settings.WIDTH,
    height=settings.prcnt_of(settings.HEIGHT,25)
    )
top_frame.place(        #change the position of the top frame
    x=0,
    y=0)

game_tittle= Label(     # for change the tittle settings
    top_frame,
    bg="black",
    fg="white",
    text= " MineSweeper",
    font=("Courier",48),
)
game_tittle.place(      # change the tittle place
    x=settings.prcnt_of(settings.WIDTH,33), 
    y=settings.prcnt_of(settings.HEIGHT,5)

)

left_frame= Frame(      #change the settings in the left frame
    screen,
    bg="black", 
    width= settings.prcnt_of(settings.WIDTH,25),
    height=settings.prcnt_of(settings.HEIGHT,75)
    )
left_frame.place(       #change the position of the left frame
    x=0,
    y=180    ) 

center_frame=Frame(     #change the settings in the center frame    
    screen,
    bg="black", 
    width= settings.prcnt_of(settings.WIDTH,25),
    height=settings.prcnt_of(settings.HEIGHT,25))
center_frame.place(     #change the position of the center frame
    x=  settings.prcnt_of(settings.WIDTH,27), #this was 25
    y= settings.prcnt_of(settings.HEIGHT,25)
)

for x in range(settings.GRID_SIZE):   #loop for create the board of cells
    for y in range(settings.GRID_SIZE):
        c1=Cell(x,y)
        c1.create_btn(center_frame)
        c1.cell_btn.grid(
            column=x,
            row=y
        )

#calling the counter from the cell class
Cell.create_cell_count_lable(left_frame)
Cell.cell_count_label_object.place(x=0,y=0)
Cell.randomize_mines()

#Run the window loop
screen.mainloop()

