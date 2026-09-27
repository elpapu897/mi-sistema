from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

ROOT=Path('/home/matiigonzz/Claude/gonvra2/creativo')
AS=ROOT/'assets'
OUTS={k:ROOT/k for k in ['feed-4x5','vertical-9x16','tiktok-portada']}
for p in OUTS.values(): p.mkdir(exist_ok=True)

FONT='/usr/share/fonts/open-sans/OpenSans-Regular.ttf'
BOLD='/usr/share/fonts/open-sans/OpenSans-Bold.ttf'
GREEN=(205,235,16); INK=(25,27,28); CREAM=(247,245,238); MUTED=(91,95,91); WHITE=(255,255,255)

def font(size,bold=False): return ImageFont.truetype(BOLD if bold else FONT,size)
def fit(im,size):
    return im.resize(size,Image.Resampling.LANCZOS)
def rounded(draw,xy,r,fill,outline=None,w=1): draw.rounded_rectangle(xy,radius=r,fill=fill,outline=outline,width=w)
def wrap(draw,text,f,maxw):
    words=text.split(); lines=[]; cur=''
    for word in words:
        test=(cur+' '+word).strip()
        if draw.textbbox((0,0),test,font=f)[2] <= maxw: cur=test
        else:
            if cur: lines.append(cur)
            cur=word
    if cur: lines.append(cur)
    return lines
def text_block(draw,text,xy,f,fill,maxw,gap=12):
    x,y=xy
    for line in wrap(draw,text,f,maxw):
        draw.text((x,y),line,font=f,fill=fill)
        y += f.size+gap
    return y

def brand(draw,x,y,light=False):
    draw.text((x,y),'GONVRA',font=font(34,True),fill=WHITE if light else INK)

def feed_base():
    return Image.new('RGB',(1080,1350),CREAM)
def save(im,path):
    im.save(path,format='PNG',optimize=True)

hero=Image.open(AS/'rasuradora-integral-hero-v1.png').convert('RGB')
uso=Image.open(AS/'rasuradora-integral-uso-v1.png').convert('RGB')
acc=Image.open(AS/'rasuradora-integral-accesorios-v1.png').convert('RGB')

# Feed 01
im=feed_base(); d=ImageDraw.Draw(im); brand(d,72,62)
d.text((72,145),'¿Tres aparatos',font=font(70,True),fill=INK); d.text((72,225),'para una sola rutina?',font=font(70,True),fill=INK)
d.text((72,335),'Una opción para rostro y cuerpo.',font=font(32),fill=MUTED)
photo=fit(hero,(650,812)); im.paste(photo,(215,475)); rounded(d,(72,1190,1008,1280),28,GREEN); d.text((110,1214),'Rasuradora Integral · Rostro y Cuerpo',font=font(29,True),fill=INK)
save(im,OUTS['feed-4x5']/'01-hero.png')

# Feed 02 typography
im=feed_base(); d=ImageDraw.Draw(im); brand(d,72,62)
d.rounded_rectangle((72,220,1008,1140),radius=42,fill=INK)
d.text((126,330),'Barba.',font=font(92,True),fill=GREEN); d.text((126,475),'Patillas.',font=font(92,True),fill=WHITE); d.text((126,620),'Vello',font=font(92,True),fill=GREEN); d.text((126,725),'corporal.',font=font(92,True),fill=WHITE)
d.text((126,1000),'Una sola rutina, menos vueltas.',font=font(34),fill=WHITE)
d.text((72,1210),'Rostro y cuerpo, en un solo equipo.',font=font(32,True),fill=INK)
save(im,OUTS['feed-4x5']/'02-rutina.png')

# Feed 03 accessories
im=feed_base(); d=ImageDraw.Draw(im); brand(d,72,62)
d.text((72,145),'Peines guía',font=font(72,True),fill=INK); d.text((72,230),'para elegir el largo.',font=font(56,True),fill=INK)
im.paste(fit(acc,(860,1074)),(110,335)); rounded(d,(72,1190,1008,1280),28,GREEN); d.text((120,1214),'Consultá las indicaciones de uso.',font=font(31,True),fill=INK)
save(im,OUTS['feed-4x5']/'03-accesorios.png')

# Feed 04 typography
im=feed_base(); d=ImageDraw.Draw(im); brand(d,72,62)
d.rounded_rectangle((72,205,1008,1145),radius=42,fill=GREEN)
d.text((130,340),'Equipo',font=font(86,True),fill=INK); d.text((130,445),'recargable',font=font(86,True),fill=INK); d.text((130,550),'para ordenar',font=font(70,True),fill=INK); d.text((130,640),'tu rutina.',font=font(70,True),fill=INK)
d.text((130,920),'Sin prometer resultados que todavía no podemos comprobar.',font=font(29),fill=INK)
d.text((72,1210),'GONVRA · cuidado personal masculino',font=font(30,True),fill=INK)
save(im,OUTS['feed-4x5']/'04-recargable.png')

# Feed 05 closing
im=feed_base(); d=ImageDraw.Draw(im); brand(d,72,62)
im.paste(fit(hero,(590,738)),(245,185));
d.text((72,970),'Rostro y cuerpo,',font=font(58,True),fill=INK); d.text((72,1040),'en un solo equipo.',font=font(58,True),fill=INK)
d.text((72,1145),'$36.900 ARS · Envío gratis a todo el país.',font=font(29,True),fill=INK)
d.text((72,1210),'Conocela en gonvra.com',font=font(31),fill=MUTED)
save(im,OUTS['feed-4x5']/'05-cierre.png')

# Vertical story 01
im=Image.new('RGB',(1080,1920),CREAM); d=ImageDraw.Draw(im); brand(d,64,64)
d.text((64,190),'¿Usás más de un',font=font(66,True),fill=INK); d.text((64,270),'aparato para tu rutina?',font=font(66,True),fill=INK)
im.paste(fit(hero,(720,900)),(180,515)); rounded(d,(160,1480,920,1630),35,INK); d.text((260,1520),'SÍ     /     A VECES',font=font(42,True),fill=GREEN)
d.text((64,1740),'La Rasuradora Integral GONVRA',font=font(33,True),fill=INK); d.text((64,1795),'está pensada para rostro y cuerpo.',font=font(32),fill=MUTED)
save(im,OUTS['vertical-9x16']/'historia-01-encuesta.png')

# Vertical story 02
im=Image.new('RGB',(1080,1920),CREAM); d=ImageDraw.Draw(im); brand(d,64,64)
d.text((64,190),'Rostro y cuerpo.',font=font(68,True),fill=INK); d.text((64,275),'Una opción más simple.',font=font(52,True),fill=MUTED)
im.paste(fit(acc,(900,1124)),(90,480)); rounded(d,(64,1660,1016,1830),34,GREEN); d.text((118,1700),'Peines guía para elegir el largo.',font=font(35,True),fill=INK); d.text((118,1760),'Equipo recargable.',font=font(34),fill=INK)
save(im,OUTS['vertical-9x16']/'historia-02-producto.png')

# Vertical story 03
im=Image.new('RGB',(1080,1920),INK); d=ImageDraw.Draw(im); brand(d,64,64,light=True)
im.paste(fit(hero,(680,850)),(200,260)); d.text((64,1210),'¿Querés ordenar',font=font(68,True),fill=WHITE); d.text((64,1290),'tu rutina?',font=font(68,True),fill=GREEN)
d.text((64,1450),'$36.900 ARS',font=font(48,True),fill=WHITE); d.text((64,1525),'Envío gratis a todo el país',font=font(36),fill=WHITE); d.text((64,1665),'Conocé el producto en',font=font(34),fill=WHITE); d.text((64,1720),'gonvra.com/products/face-body-electric-shaver',font=font(25,True),fill=GREEN)
save(im,OUTS['vertical-9x16']/'historia-03-cierre.png')

# TikTok cover
im=Image.new('RGB',(1080,1920),INK); d=ImageDraw.Draw(im); brand(d,64,64,light=True)
d.text((64,205),'¿Otro aparato',font=font(84,True),fill=WHITE); d.text((64,310),'más?',font=font(84,True),fill=GREEN)
d.text((64,465),'Una opción más simple',font=font(43,True),fill=WHITE); d.text((64,520),'para rostro y cuerpo.',font=font(43,True),fill=WHITE)
im.paste(fit(hero,(770,963)),(155,710)); d.text((64,1770),'Presentación, no testimonio.',font=font(34,True),fill=GREEN); d.text((64,1825),'Conocé los detalles en gonvra.com',font=font(30),fill=WHITE)
save(im,OUTS['tiktok-portada']/'portada-tiktok-otro-aparato.png')
print('generadas')
