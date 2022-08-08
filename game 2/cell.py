from tkinter import Button, Label
import settings
import random
import ctypes
import sys

class Cell:
    all=[]
    cell_count=settings.CELL_COUNT
    cell_count_label_object=None
    def __init__(self,x,y, is_mine=False):
        self.is_mine=is_mine
        self.is_open=False
        self.is_mine_candidate=False
        self.cell_btn= None
        self.x=x
        self.y=y

        #Append the objet to the cell list
        Cell.all.append(self)

    
    def create_btn(self,location):
        btn=Button(
            location,
            width=12,
            height=4,
            text=None
        )
        
        btn.bind("<Button-1>",self.left_click_action ) #Left Click
        btn.bind("<Button-3>",self.right_click_action )#Right Click
        self.cell_btn=btn

    @staticmethod
    def create_cell_count_lable(location):
        lbl=Label(
            location,
            bg="black",
            fg="white",
            text=f"Cells Left:\n {Cell.cell_count}",
            font=("Courier",30)
            )
        lbl.config(anchor="center")
        lbl.pack()
        Cell.cell_count_label_object=lbl
    def left_click_action(self,event):
        if self.is_mine:
           self.show_mine()
        else:
            if self.surrounded_cells_minesl==0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell() 

    #cancel left and tight click events if cell is already running
        self.cell_btn.unbind("<Button-1>")
        self.cell_btn.unbind("<Button-3>")

    @property        
    def surrounded_cells(self):
        cells=[
            self.get_the_cell_by_axis(self.x-1,self.y-1),
            self.get_the_cell_by_axis(self.x-1,self.y),
            self.get_the_cell_by_axis(self.x-1,self.y+1),
            self.get_the_cell_by_axis(self.x,self.y-1),
            self.get_the_cell_by_axis(self.x+1,self.y-1),
            self.get_the_cell_by_axis(self.x+1,self.y),
            self.get_the_cell_by_axis(self.x+1,self.y+1),
            self.get_the_cell_by_axis(self.x,self.y+1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_minesl(self): 
        counter=0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter+=1
        return counter

    def show_cell(self):
        if not self.is_open:
            Cell.cell_count-=1
            self.cell_btn.configure(text=self.surrounded_cells_minesl)
            #replace the text of cell with the new count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text =f"Cells Left: {Cell.cell_count}"
                )
            self.cell_btn.configure(
                bg="SystemButtonFace"
            )

        # mark the cell as opened(use this as the last line of this method)
        self.is_open= True
        if Cell.cell_count== settings.MINES_NUMBERS:
            ctypes.windll.user32.MessageBoxW(0,"Congratulations!! You won the game!!","game Over",0)
    
    
    def get_the_cell_by_axis(self,x,y):
       for cell in Cell.all:
        if cell.x == x and cell.y == y:
            return cell

    def show_mine(self):
        self.cell_btn.configure(bg="red")
        ctypes.windll.user32.MessageBoxW(0,"You had clicked a mine","game Over",0)
        sys.exit()


    def right_click_action(self,event):
        if not self.is_mine_candidate:
            self.cell_btn.configure(
                bg="yellow"
            )
            self.is_mine_candidate =True
        else:
            self.cell_btn.configure(
               bg="SystemButtonFace" 
            )
            self.is_mine_candidate= False
    @staticmethod
    def randomize_mines():
        picked_cells=random.sample(
            Cell.all,settings.MINES_NUMBERS
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine= True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"