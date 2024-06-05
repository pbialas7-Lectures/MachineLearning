import matplotlib.pyplot as plt
import matplotlib.text as text

from matplotlib.patches import Rectangle


class TextBox:
    def __init__(self, l, b, w, h, text = None, fc='w', ec='k', linewidth=1, fontsize=16, zorder=1):
        self.l = l
        self.b = b
        self.w = w
        self.h = h
        self.fc=fc
        self.ec=ec
        self.text = text
        self.fontsize = fontsize
        self.zorder = zorder
        self.box = Rectangle((l, b), w, h, fill=True, fc=fc, ec=ec, linewidth=linewidth,
                             zorder=zorder)

    def draw(self, ax):
        ax.add_patch(self.box)
        if self.text is not None:
            t = text.Text(self.l + self.w / 2, self.b + self.h / 2, self.text, ha='center', bbox ={'fc':self.fc, 'ec': 'none'},
                          va='center', fontsize=self.fontsize, zorder=self.zorder)
            ax.add_artist(t)

def is_padding(size, padding,i):
    return (i<padding) or (i>= size+padding)
            
def draw_grid_with_padding(ax, h,w, padding=0, background = 'white', pbackground ='lightgrey',  left=0, bottom=0):
    for i in  range(h+2*padding):
        for j in range(w+2*padding):
            if is_padding(h,padding,i) or is_padding(w,padding,j):
                color = pbackground
            else:
                color = background    
            
            tb = TextBox(left+i-padding,bottom+j-padding,1,1, fc=color)
            tb.draw(ax)
    
            
            
def draw_kernel(ax, size,i,j, left=0, bottom=0, color ='lightblue'):
    kernel = Rectangle((i+left,j+bottom),size, size, fill=True, fc=color, ec='none', alpha =0.5)
    ax.add_patch(kernel)
    return kernel