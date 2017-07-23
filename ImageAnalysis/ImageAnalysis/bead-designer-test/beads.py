import Image
from ImageColor import getrgb
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
import uuid

BEAD_RADIUS = 1.75*mm
BEAD_THICKNESS = 1*mm
BOARD_SPACING = 4.85*mm
BOARD_BORDER = 4*mm

#A4 60x43 = 2580
#A3 86x60 = 5160
#A2 86x120 = 10,320
#MARQUEE A4+A4 = 120x43

class beadColours():
  def __init__(self):
    self.palette = self.getColours()
  
  def getColours(self, csv="colours\\all.csv"):
    """read colour table
    CODE, NAME, R, G, B, TYPE, INCLUDE/EXCLUDE"""
    palette = []
    with open(csv, 'r') as f:
      read_data = f.read()
      lines = read_data.split("\n")
    f.closed
    return lines

  def bestMatch(self, r=0, g=0, b=0):
    """return nearest bead colour to the r,g,b value specified"""
    tmp = []
    for row in self.palette:
      cell = row.split(",")
      if cell[0] != 'CODE' and cell[6] != 'E': #ignore some lines        
        if cell[0][0] in ('H'):  #Hama and Perler only for now
          tmp_r = int(cell[2])
          tmp_g = int(cell[3])
          tmp_b = int(cell[4])        
          
          if tmp_r > r: dif_r = tmp_r - r
          else: dif_r = r - tmp_r
          if tmp_g > g: dif_g = tmp_g - g
          else: dif_g = g - tmp_g
          if tmp_b > b: dif_b = tmp_b - b
          else: dif_b = b - tmp_b
            
          difference = dif_r + dif_g + dif_b
          tmp.append((difference, tmp_r, tmp_g, tmp_b))        
    tmp.sort()
    return tmp[0][1:]
        
        
colours = beadColours()
  
#read image file header
try:
  im = Image.open("images\\pikachu.gif")
  image_width = im.size[0]
  image_height = im.size[1]
  image_format = im.format    
except IOError:
  print "Error opening file"
    
out_file = 'result%s.pdf' % uuid.uuid1()
pdf = canvas.Canvas(out_file, pagesize=A4)

##work out the best orientation
a4_width, a4_height = A4
#if (width - (BOARD_BORDER * 2)) < (image_width * BOARD_SPACING):
  #width_temp = width
  #width = height
  #height = width_temp
  
#for now,  just use generated page size
width = (image_width * BOARD_SPACING) + (BOARD_BORDER * 2)
height = (image_height * BOARD_SPACING) + (BOARD_BORDER * 2)
if width < a4_width and width < a4_height: 
  height = a4_height

pdf.setPageSize((width, height))

im = im.convert('RGB')
data = list(im.getdata())
list_pos = 0
for y in range(0, im.size[1]):
  pos_y = height - BOARD_BORDER - (y * BOARD_SPACING)
  for x in range(0, im.size[0]):
    r = data[list_pos][0]
    g = data[list_pos][1]
    b = data[list_pos][2]
    r, g, b = colours.bestMatch(r,g,b)
    pos_x = BOARD_BORDER + (x * BOARD_SPACING)
    pdf.setLineWidth(BEAD_THICKNESS)
    pdf.setStrokeColorRGB(float(r)/255,float(g)/255,float(b)/255)
    pdf.circle(pos_x, pos_y, BEAD_RADIUS, stroke=1, fill=0)
    
    #for light colour we need a thin black border
    if r + g + b >= 750:
      pdf.setLineWidth(0.25*mm)
      pdf.setStrokeColorRGB(0,0,0)
      pdf.circle(pos_x, pos_y, BEAD_RADIUS + (BEAD_THICKNESS / 2), stroke=1, fill=0)
      pdf.circle(pos_x, pos_y, BEAD_RADIUS - (BEAD_THICKNESS / 2), stroke=1, fill=0)
    
    list_pos += 1

pdf.showPage()
pdf.save()    
