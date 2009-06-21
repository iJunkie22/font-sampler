# -*- coding: utf-8 -*-


pil_colors = {
    'indigo': (75, 0, 130),
    'gold': (255, 215, 0),
    'firebrick': (178, 34, 34),
    'indianred': (205, 92, 92),
    'yellow': (255, 255, 0),
    'darkolivegreen': (85, 107, 47),
    'darkseagreen': (143, 188, 143),
    'mediumvioletred': (199, 21, 133),
    'mediumorchid': (186, 85, 211),
    'chartreuse': (127, 255, 0),
    'mediumslateblue': (123, 104, 238),
    'black': (0, 0, 0),
    'springgreen': (0, 255, 127),
    'crimson': (220, 20, 60),
    'lightsalmon': (255, 160, 122),
    'brown': (165, 42, 42),
    'turquoise': (64, 224, 208),
    'olivedrab': (107, 142, 35),
    'cyan': (0, 255, 255),
    'silver': (192, 192, 192),
    'skyblue': (135, 206, 235),
    'gray': (128, 128, 128),
    'darkturquoise': (0, 206, 209),
    'goldenrod': (218, 165, 32),
    'darkgreen': (0, 100, 0),
    'darkviolet': (148, 0, 211),
    'darkgray': (169, 169, 169),
    'lightpink': (255, 182, 193),
    'teal': (0, 128, 128),
    'darkmagenta': (139, 0, 139),
    'lightgoldenrodyellow': (250, 250, 210),
    'lavender': (230, 230, 250),
    'yellowgreen': (154, 205, 50),
    'thistle': (216, 191, 216),
    'violet': (238, 130, 238),
    'navy': (0, 0, 128),
    'orchid': (218, 112, 214),
    'blue': (0, 0, 255),
    'ghostwhite': (248, 248, 255),
    'honeydew': (240, 255, 240),
    'cornflowerblue': (100, 149, 237),
    'darkblue': (0, 0, 139),
    'darkkhaki': (189, 183, 107),
    'mediumpurple': (147, 112, 219),
    'cornsilk': (255, 248, 220),
    'red': (255, 0, 0),
    'bisque': (255, 228, 196),
    'slategray': (112, 128, 144),
    'darkcyan': (0, 139, 139),
    'khaki': (240, 230, 140),
    'wheat': (245, 222, 179),
    'deepskyblue': (0, 191, 255),
    'darkred': (139, 0, 0),
    'steelblue': (70, 130, 180),
    'aliceblue': (240, 248, 255),
    'gainsboro': (220, 220, 220),
    'mediumturquoise': (72, 209, 204),
    'floralwhite': (255, 250, 240),
    'coral': (255, 127, 80),
    'purple': (128, 0, 128),
    'lightgrey': (211, 211, 211),
    'lightcyan': (224, 255, 255),
    'darksalmon': (233, 150, 122),
    'beige': (245, 245, 220),
    'azure': (240, 255, 255),
    'lightsteelblue': (176, 196, 222),
    'oldlace': (253, 245, 230),
    'greenyellow': (173, 255, 47),
    'royalblue': (65, 105, 225),
    'lightseagreen': (32, 178, 170),
    'mistyrose': (255, 228, 225),
    'sienna': (160, 82, 45),
    'lightcoral': (240, 128, 128),
    'orangered': (255, 69, 0),
    'navajowhite': (255, 222, 173),
    'lime': (0, 255, 0),
    'palegreen': (152, 251, 152),
    'burlywood': (222, 184, 135),
    'seashell': (255, 245, 238),
    'mediumspringgreen': (0, 250, 154),
    'fuchsia': (255, 0, 255),
    'papayawhip': (255, 239, 213),
    'blanchedalmond': (255, 235, 205),
    'peru': (205, 133, 63),
    'aquamarine': (127, 255, 212),
    'white': (255, 255, 255),
    'darkslategray': (47, 79, 79),
    'ivory': (255, 255, 240),
    'dodgerblue': (30, 144, 255),
    'lemonchiffon': (255, 250, 205),
    'chocolate': (210, 105, 30),
    'orange': (255, 165, 0),
    'forestgreen': (34, 139, 34),
    'slateblue': (106, 90, 205),
    'olive': (128, 128, 0),
    'mintcream': (245, 255, 250),
    'antiquewhite': (250, 235, 215),
    'darkorange': (255, 140, 0),
    'cadetblue': (95, 158, 160),
    'moccasin': (255, 228, 181),
    'limegreen': (50, 205, 50),
    'saddlebrown': (139, 69, 19),
    'darkslateblue': (72, 61, 139),
    'lightskyblue': (135, 206, 250),
    'deeppink': (255, 20, 147),
    'plum': (221, 160, 221),
    'aqua': (0, 255, 255),
    'darkgoldenrod': (184, 134, 11),
    'maroon': (128, 0, 0),
    'sandybrown': (244, 164, 96),
    'magenta': (255, 0, 255),
    'tan': (210, 180, 140),
    'rosybrown': (188, 143, 143),
    'pink': (255, 192, 203),
    'lightblue': (173, 216, 230),
    'palevioletred': (219, 112, 147),
    'mediumseagreen': (60, 179, 113),
    'dimgray': (105, 105, 105),
    'powderblue': (176, 224, 230),
    'seagreen': (46, 139, 87),
    'snow': (255, 250, 250),
    'mediumblue': (0, 0, 205),
    'midnightblue': (25, 25, 112),
    'paleturquoise': (175, 238, 238),
    'palegoldenrod': (238, 232, 170),
    'whitesmoke': (245, 245, 245),
    'darkorchid': (153, 50, 204),
    'salmon': (250, 128, 114),
    'lightslategray': (119, 136, 153),
    'lawngreen': (124, 252, 0),
    'lightgreen': (144, 238, 144),
    'tomato': (255, 99, 71),
    'hotpink': (255, 105, 180),
    'lightyellow': (255, 255, 224),
    'lavenderblush': (255, 240, 245),
    'linen': (250, 240, 230),
    'mediumaquamarine': (102, 205, 170),
    'green': (0, 128, 0),
    'blueviolet': (138, 43, 226),
    'peachpuff': (255, 218, 185),
}



import ImageDraw, Image, ImageFont
import os,sys
from optparse import OptionParser  #not needed if used as a module



def simple_bidi_reverse(s):
    return s
    s = unicode(s)
    news = ''
    hebrew = u'אבגדהוזחטיכךלמםנןסעפףצץקרשתֱֲֳִֵֶַָֹּׁׂ'
    hebword = ''
    for c in s:
        if c in hebrew:
            if not hebword:     #start new hebword
                hebword = c
            else:
                hebword += c    # cont. hebword
            continue
        
        else:
            if hebword:
                hebword = hebword[::-1] #reverse last hebword so far
                news += hebword
                hebword = ''    # falsify hebword
            else:
                news += c
    return news
        


def parse_options():
    
    option_parser = OptionParser()
    option_parser.add_option('-f', '--fore', action='store', dest='fore', default='black', help="fore color [default: black]", type='string')
    option_parser.add_option('-b', '--background', action='store', dest='background', default='white', help="bg color [default: white]", type='string')
    option_parser.add_option('-s', '--split-height', action='store', dest='height', default=0, help="split new image every n pixels. default=0 (no split, single image)", type='int')
    option_parser.add_option('-t', '--text-sample', action='store', dest='sample', default='', help="sample text", type='string')
    option_parser.add_option('-p', '--font-dir', action='store', dest='fontdir', default=r'c:\windows\fonts', help=r"font directory (default: c:\windows\fonts)", type='string')
    option_parser.add_option('-z', '--font-size', action='store', dest='size', default=22, help=r"font size (pixels)", type='int')
    option_parser.add_option('-c', '--color-list', action='store_false', dest='colorlist', default=False, help=r"print a list of all colors")
    option_parser.add_option('-o', '--output-dir', action='store', dest='outputdir', default='.', help=r"output directory")    

    (options, args) = option_parser.parse_args(sys.argv[1:])
    options.help = option_parser.format_help()
    temp = [unicode(opt)+': '+unicode(options.__dict__[opt]) for opt in options.__dict__ if opt!='help']
    print 'command line options:', temp
    return options


def color_to_hex(c):
    return hex(c[0])[2:]+hex(c[1])[2:]+hex(c[2])[2:]

def generate_font_image(options):

    if os.path.isfile(options.outputdir):
        print 'fatal error - outputdir exists, and is a file. writing output to "."'
        options.outputdir = os.path.abspath('.')
    elif not os.path.isdir(options.outputdir):
        os.makedirs( options.outputdir )

    fontfiles = [options.fontdir + os.sep + f for f in os.listdir(options.fontdir) if f[-3:].lower()=='ttf']
    if not fontfiles:
        print 'no font files found'
        sys.exit(1)

    text = options.sample
    #print type(text)
    #print len(text)
    #print text

    if not text:
        text = 'אבגד זהוחף קרשצת 123 ?$%^!'
    if type(text) is unicode:
        #text = text.decode('utf-8')
        pass
    width = 950
    img_counter = 0
    fontsize = options.size
    ystep = int(fontsize*1.5)
    i=0
    img = False
    tot = len(fontfiles)
    height = options.height or len(fontfiles) * ystep + 20

    if type(options.fore) is str:
        forecolor = pil_colors[options.fore]
    else:
        try:
            forecolor = options.fore
            if len(forecolor)==3:
                print forecolor 
                forecolor = forecolor[:3]
            forecolorname = color_to_hex(forecolor)
        except:
            print 'fatal error - fore color not in right format'
            return
        
    if type(options.background) is str:
        backcolor = pil_colors[options.background]
        backcolorname = options.background
    else:
        try:
            backcolor = options.background
            if len(backcolor)==3:
                backcolor = backcolor[:3]
            backcolorname = color_to_hex(backcolor)
        except:
            print 'fatal error - color not in right format'
            return
    
    for fontfile in fontfiles:
        if not img:
            img = Image.new('RGB',(width, height), backcolor )
            draw = ImageDraw.Draw(img)
            draw.fontmode = 'I' #"1", "P", "I", "F"
            y = 6

        last_printed = False
        i+=1
        font = ImageFont.truetype(fontfile, fontsize)
        wtf = '%s %s ' % (os.path.basename(fontfile) , font.getname()[0])

        if type(wtf) is unicode:
            pass #wtf = wtf.encode('utf-8')
        text2 = wtf + text
        print '%% %0.2d \r' % (100.0* i / tot),
        draw = ImageDraw.Draw(img)
        try:
            draw.text((10, y), text2, font=font, fill=forecolor )
            y += ystep
        except:
            print 'error',y,fontfile
    
        # for testing:  if y> 500: break
    
        if y >= height:
            #fname = 'fonts.%s-on-%s.%04d.png' % (forecolorname, backcolorname, img_counter)
            fname = 'generated_fonts_%04d.png' % (img_counter)
            fname = os.path.join( options.outputdir, fname )
            print 'saving ' + fname
            img.save(fname)
            
            #init new image
            img_counter += 1
            img = False
            last_printed=True

    if not last_printed:
        fname = 'generated_fonts_%04d.png' % (img_counter)
        fname = os.path.join( options.outputdir, fname )
        print 'saving ' + fname
        img.save(fname)
    
    return i 


if __name__ == "__main__":
    options = parse_options()
    if options.colorlist:
        for c in pil_colors:
            print c[1]
        sys.exit(0)
    if options.fore not in pil_colors:
        options.fore = 'black'
    if options.background not in pil_colors:
        options.background = 'white'
    generate_font_image(options)

    