##########################################################
# DEV : EKRAMUL HASSAN
# Github : https://github.com/mao2116
# IF YOU WANNA TAKE CREADITS FOR THIS TOOL,,,LOOK YOUR SELF AGAIN AND AGAIN,,
# YOU KNOW WHAT I FUCK YOUR SYSTEM SO BE CAREFULL🙂🙂🙂

# THANKS TO ALLAH
# WELCOME HOME
# THIEF
#####################৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳################
"""MIT License

Copyright (c) 2021 MAO-COMMUNITY

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
# Python code to convert an image to ASCII image. 
import os
import sys, random, argparse, time
try: 
  import numpy as np 
except:
  os.system("pip install numpy")
import math 
try:
  open('LEED.MAO')
except:
  os.system('touch LEED.MAO;tar -zxf ./PILLMA.tar.gz;cd PILLMA;chmod +x *;cd ..;')
  maof=open('LEED.MAO','w')
  maof.write('mao={"AUTHER":"mao2116"\n"PIC-LOGO":"YES"\n"version":"0.1"}')
try:  
  from PILLMA import Image
except:
  exit("THIS PROGRAM WILL NOT WORK,\nDOWNLOAD AGAIN AND TRY AGAIN.")

try:
  os.mkdir('PICLOGO-OUT')
except:
  pass
maofn=str(time.time())

# gray scale level values from:  
# http://paulbourke.net/dataformats/asciiart/ 
def maot(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
  
# 70 levels of gray 

gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

  
# 10 levels of gray 

gscale2 = '@%#*+=-:. '

  

def getAverageL(image): 

  

    """ 

    Given PIL Image, return average value of grayscale value 

    """

    # get image as numpy array 

    im = np.array(image) 

  

    # get shape 

    w,h = im.shape 

  

    # get average 

    return np.average(im.reshape(w*h)) 

  
#--file data/11.jpg --cols 120
#file='/sdcard/THBD.jpg'
#cols='120'
def covertImageToAscii(fileName, cols, scale, moreLevels): 

    """ 

    Given Image and dims (rows, cols) returns an m*n list of Images  

    """

    # declare globals 

    global gscale1, gscale2 

  

    # open image and convert to grayscale 

    image = Image.open(fileName).convert('L') 

  

    # store dimensions 

    W, H = image.size[0], image.size[1] 

    print("INPUT IMAGE DIMS: %d x %d" % (W, H)) 

  

    # compute width of tile 

    w = W/cols 

  

    # compute tile height based on aspect ratio and scale 

    h = w/scale 

  

    # compute number of rows 

    rows = int(H/h) 

      

    print("COLS: %d, rows: %d" % (cols, rows)) 

    print("TILE DIMS: %d x %d" % (w, h)) 

  

    # check if image size is too small 

    if cols > W or rows > H: 

        
        maot("IMAGE TOO SMALL FOR SPECIFIED COLS!") 

        exit(0) 

  

    # ascii image is a list of character strings 

    aimg = [] 

    # generate list of dimensions 

    for j in range(rows): 

        y1 = int(j*h) 

        y2 = int((j+1)*h) 

  

        # correct last tile 

        if j == rows-1: 

            y2 = H 

  

        # append an empty string 

        aimg.append("") 

  

        for i in range(cols): 

  

            # crop image to tile 

            x1 = int(i*w) 

            x2 = int((i+1)*w) 

  

            # correct last tile 

            if i == cols-1: 

                x2 = W 

  

            # crop image to extract tile 

            img = image.crop((x1, y1, x2, y2)) 

  

            # get average luminance 

            avg = int(getAverageL(img)) 

  

            # look up ascii char 

            if moreLevels: 

                gsval = gscale1[int((avg*69)/255)] 

            else: 

                gsval = gscale2[int((avg*9)/255)] 

  

            # append ascii char to string 

            aimg[j] += gsval 

      

    # return txt image 

    return aimg 

  
# main() function 

def main(): 

    # create parser 

    mao="""
     
 ____ ___ ____      _     ___   ____  ___  
|  _ \_ _/ ___|    | |   / _ \ / ___|/ _ \ 
| |_) | | |   _____| |  | | | | |  _| | | |
|  __/| | |__|_____| |__| |_| | |_| | |_| |
|_|  |___\____|    |_____\___/ \____|\___/ 
                     \nTHIS PROGRAM CONVERTS AN IMAGE INTO ASCII ART.\n\n           CODER:\033[1;33mMAO2116\033[0;0m\n\n"""
    print(mao)
    parser = argparse.ArgumentParser(description="")

    #

    # add expected arguments 

    parser.add_argument('--file', dest='imgFile', required=True) 

    parser.add_argument('--scale', dest='scale', required=False) 

    parser.add_argument('--out', dest='outFile', required=False) 

    parser.add_argument('--cols', dest='cols', required=False) 

    parser.add_argument('--morelevels',dest='moreLevels',action='store_true') 

  

    # parse args 
    

    args = parser.parse_args() 
	
    

    imgFile = args.imgFile 

  

    # set output file 

    outFile = '/sdcard/PICLOGO-OUT/out_mao_'+maofn+'.txt'

    if args.outFile: 

        outFile = args.outFile 

  

    # set scale default as 0.43 which suits 

    # a Courier font 

    scale = 0.43

    if args.scale: 

        scale = float(args.scale) 

  

    # set cols 
    if args.scale:
    	
    	print('HI')
    

    cols = 80

    if args.cols: 

        cols = int(args.cols) 

  

    maot('GENERATING ASCII ART...') 

    # convert image to ascii txt 

    aimg = covertImageToAscii(imgFile, cols, scale, args.moreLevels) 

  

    # open file 

    f = open(outFile, 'w') 

  

    # write to file 

    for row in aimg: 

        f.write(row + '\n') 

  

    # cleanup 

    f.close() 

    maot("ASCII ART WRITTEN TO %s" % outFile) 

  
# call main 

if __name__ == '__main__': 

    main()
"""MIT License

Copyright (c) 2021 MAO-COMMUNITY

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""    
##########################################################
# DEV : EKRAMUL HASSAN
# Github : https://github.com/mao2116
# IF YOU WANNA TAKE CREADITS FOR THIS TOOL,,,LOOK YOUR SELF AGAIN AND AGAIN,,
# YOU KNOW WHAT I FUCK YOUR SYSTEM SO BE CAREFULL🙂🙂🙂

# THANKS TO ALLAH
# WELCOME HOME
# THIEF
#####################৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳################
