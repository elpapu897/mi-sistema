from pathlib import Path
import json, re

root = Path(__file__).parent / 'theme'

def read(rel): return (root / rel).read_text()
def write(rel, text): (root / rel).write_text(text)
def getjson(rel): return json.loads(re.sub(r'/\*.*?\*/', '', read(rel), flags=re.S))
def putjson(rel, data): write(rel, json.dumps(data, ensure_ascii=False, indent=2) + '\n')
def replace(rel, old, new):
    text = read(rel)
    assert old in text, (rel, old[:80])
    write(rel, text.replace(old, new))
def schema(rel, settings):
    text = read(rel)
    match = re.search(r'{% schema %}(.*?){% endschema %}', text, re.S)
    data = json.loads(match[1])
    data['settings'].extend(settings)
    write(rel, text[:match.start(1)] + '\n' + json.dumps(data, ensure_ascii=False, indent=2) + '\n' + text[match.end(1):])

layout = 'layout/theme.liquid'
replace(layout, "    {{ content_for_header }}", "    {{ 'gv-experience.css' | asset_url | stylesheet_tag }}\n    <script src=\"{{ 'gv-experience.js' | asset_url }}\" defer></script>\n    {{ content_for_header }}")

home = 'sections/gv-home.liquid'
replace(home, '  <div class="gvhm-hero">', '  {% if section.settings.show_hero %}\n  <div class="gvhm-hero">')
replace(home, '  {% if p != blank %}\n    <div class="gvhm-wrap"', '  {% endif %}\n  {% if p != blank and section.settings.show_card %}\n    <div class="gvhm-wrap"')
replace(home, '<div class="gvhm-actions">', '''{% if p != blank and section.settings.show_price %}
        <p class="gvhm-hero-price"><strong>{{ p.selected_or_first_available_variant.price | money }}</strong><span>{{ section.settings.price_note | escape }}</span></p>
      {% endif %}
      <div class="gvhm-actions">''')
replace(home, "{{ section.settings.cta2_url | default: '#catalogo' }}", "{{ section.settings.cta2_url | default: '#como-funciona' }}")
replace(home, '{{ section.settings.sub }}</p>', '{{ section.settings.sub | escape | newline_to_br }}</p>')
replace(home, "{% if p != blank %}{{ p.url }}{% else %}", "{% if section.settings.cta_url != blank %}{{ section.settings.cta_url }}{% elsif p != blank %}{{ p.url }}{% else %}")
schema(home, [
    {'type':'checkbox','id':'show_hero','label':'Mostrar presentación','default':True},
    {'type':'checkbox','id':'show_card','label':'Mostrar contenido del kit','default':True},
    {'type':'checkbox','id':'show_price','label':'Mostrar precio en presentación','default':True},
    {'type':'text','id':'price_note','label':'Nota del precio','default':'Por unidad · precio en ARS'},
])

for rel, inner in [(home,'.gvhm-wrap'), ('sections/gv-historia.liquid','.gvh-wrap'), ('sections/gv-faq.liquid','.gvf-wrap')]:
    schema(rel, [
        {'type':'header','content':'Diseño y espaciado'},
        {'type':'range','id':'heading_size','label':'Tamaño de títulos','min':24,'max':80,'step':2,'unit':'px','default':48},
        {'type':'range','id':'body_size','label':'Tamaño de texto','min':14,'max':22,'step':1,'unit':'px','default':16},
        {'type':'select','id':'text_align','label':'Alineación','options':[{'value':'left','label':'Izquierda'},{'value':'center','label':'Centro'}],'default':'left'},
        {'type':'range','id':'padding_top','label':'Espacio superior','min':0,'max':160,'step':8,'unit':'px','default':64},
        {'type':'range','id':'padding_bottom','label':'Espacio inferior','min':0,'max':160,'step':8,'unit':'px','default':64}
    ])
    text = read(rel)
    style = '''{% style %}
  #shopify-section-{{ section.id }} { background:#f7f6f1;padding-top:{{ section.settings.padding_top }}px;padding-bottom:{{ section.settings.padding_bottom }}px; }
  #shopify-section-{{ section.id }} INNER {padding-top:0;padding-bottom:0;}
  #shopify-section-{{ section.id }} :is(.gvhm-head,.gvh-head,.gvf-head) {text-align:{{ section.settings.text_align }};}
  #shopify-section-{{ section.id }} :is(.gvhm-head h2,.gvh-head h2,.gvf-head h2) {font-size:clamp(1.8rem,4vw,{{ section.settings.heading_size }}px);}
  #shopify-section-{{ section.id }} :is(.gvhm-card__text,.gvh-text,.gvf-a) {font-size:{{ section.settings.body_size }}px;}
  @media(max-width:860px){#shopify-section-{{ section.id }} {padding-top:{{ section.settings.padding_top | times: 0.65 }}px;padding-bottom:{{ section.settings.padding_bottom | times: 0.65 }}px;}}
{% endstyle %}
'''.replace('INNER',inner)
    text = style + text
    text = re.sub(r'{% javascript %}.*?{% endjavascript %}', '', text, flags=re.S)
    write(rel, text)

replace('sections/gv-historia.liquid', '<section class="gvh" data-gvh>', '<section class="gvh" data-gvh id="como-funciona">')
faq = 'sections/gv-faq.liquid'
replace(faq, '<section class="gvf" data-gvf>', '<section class="gvf" data-gvf id="faq">')
replace(faq, '{{ section.settings.contact_link }}', "{% if section.settings.contact_link != blank %}{{ section.settings.contact_link }}{% else %}mailto:{{ shop.email | escape }}{% endif %}")

header = 'sections/gv-header.liquid'
replace(header, '<div class="gvn-bar__track">', '<div class="gvn-bar__window"><div class="gvn-bar__track">')
replace(header, '      </div>\n    </div>\n  {% endif %}', '      </div></div>\n      <button class="gvn-pause" type="button" data-gv-pause aria-pressed="false" aria-label="{{ section.settings.pause_label | escape }}">Ⅱ</button>\n    </div>\n  {% endif %}')
replace(header, 'aria-label="{{ shop.name | escape }}"', 'aria-label="{{ section.settings.brand_text | escape }}"')
replace(header, 'aria-expanded="false"><span>', 'aria-expanded="false" aria-controls="gv-menu-{{ section.id }}"><span>')
replace(header, 'class="gvn-drawer" data-gvn-drawer', 'class="gvn-drawer" id="gv-menu-{{ section.id }}" data-gvn-drawer')
schema(header,[{'type':'text','id':'pause_label','label':'Etiqueta de pausa','default':'Pausar animación de anuncios'}])
text=read(header)
start=text.index('{% javascript %}');end=text.index('{% endjavascript %}',start)+len('{% endjavascript %}')
text=text[:start]+'''{% javascript %}
(() => {
  const init = () => document.querySelectorAll('[data-gvn]').forEach(root => {
    if (root.dataset.ready) return;
    root.dataset.ready = 'true';
    const burger = root.querySelector('[data-gvn-burger]');
    const drawer = root.querySelector('[data-gvn-drawer]');
    if (!burger || !drawer) return;
    const close = () => {burger.setAttribute('aria-expanded','false');drawer.hidden=true;};
    burger.addEventListener('click', () => {
      const open = burger.getAttribute('aria-expanded') === 'true';
      burger.setAttribute('aria-expanded', String(!open));drawer.hidden=open;
    });
    drawer.addEventListener('click', event => {if(event.target.closest('a')) close();});
    root.addEventListener('keydown', event => {if(event.key==='Escape'){close();burger.focus();}});
    root.addEventListener('focusout', event => {if(!root.contains(event.relatedTarget)) close();});
    document.addEventListener('pointerdown', event => {if(!root.contains(event.target)) close();});
    window.matchMedia('(min-width:861px)').addEventListener('change', close);
  });
  init();
  document.addEventListener('shopify:section:load', init);
})();
{% endjavascript %}'''+text[end:]
write(header,text)

footer='sections/gv-footer.liquid'
replace(footer, '<footer class="gvft">','<footer class="gvft" id="contacto">')
replace(footer, '      </div>\n\n      <div class="gvft-cols">', '        <a class="gvft-contact" href="mailto:{{ shop.email | escape }}">{{ shop.email | escape }}</a>\n      </div>\n\n      <div class="gvft-cols">')
replace(footer, "            {% form 'customer' %}", "            {% form 'customer' %}\n              {% if form.errors %}<div class=\"gvft-errors\" role=\"alert\">{{ form.errors | default_errors }}</div>{% endif %}")
replace(footer, 'name="contact[email]" placeholder', 'name="contact[email]" autocomplete="email" placeholder')
replace(footer, '<small class="gvft-ok">', '<small class="gvft-ok" role="status">')

product='sections/gv-producto.liquid'
replace(product, '                assign disc = block.settings.discount', '                assign disc = 0')
replace(product, "behavior: 'smooth'", "behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'")
replace(product, '  offers.forEach((btn) => btn.addEventListener(\'click\', () => pick(btn)));', '''  offers.forEach((btn, index) => {
    btn.addEventListener('click', () => pick(btn));
    btn.addEventListener('keydown', event => {
      if (!['ArrowDown','ArrowUp','ArrowLeft','ArrowRight'].includes(event.key)) return;
      event.preventDefault();
      const direction = ['ArrowRight','ArrowDown'].includes(event.key) ? 1 : -1;
      const next = offers[(index + direction + offers.length) % offers.length];
      pick(next); next.focus();
    });
  });''')
replace(product,'data-gv-sticky-add>{{ section.settings.cta_text }}','data-gv-sticky-add {% unless v.available %}disabled{% endunless %}>{{ section.settings.cta_text }}')
replace(product, '  <div class="gv-sticky" data-gv-sticky>', '  {% if v.available %}<div class="gv-sticky" data-gv-sticky>')
replace(product, '  </div>\n</section>\n\n{% stylesheet %}', '  </div>{% endif %}\n</section>\n\n{% stylesheet %}')
replace(product, "loading: 'eager', alt: product.title", "loading: media_loading, alt: product.title")
replace(product, '<figure data-gv-slide="{{ forloop.index0 }}">', "{% assign media_loading = 'lazy' %}{% if forloop.first and section.settings.gallery_clip == blank %}{% assign media_loading = 'eager' %}{% endif %}\n                <figure data-gv-slide=\"{{ forloop.index0 }}\">")
replace(product, 'aria-label="Ver el video"', 'aria-label="Ver presentación del producto"')

index=getjson('templates/index.json')
sections=index['sections']
sections['portada']['settings'].update(show_card=False,show_hero=True,show_price=True,padding_top=0,padding_bottom=0,heading='Un equipo. Tu rutina resuelta.',sub='Recortá barba y vello corporal con el largo que elegís vos. Peines de 1, 3 y 5 mm, carga USB y un formato fácil de llevar.',cta_label='Elegir mi rasuradora',cta2_url='#como-funciona',price_note='Por unidad · precio en ARS')
sections['portada']['blocks']['chip1']['settings']['text']='Rostro y cuerpo'
sections['portada']['blocks']['chip2']['settings']['text']='3 peines incluidos'
sections['portada']['blocks']['chip3']['settings']['text']='Recargable por USB'
kit=json.loads(json.dumps(sections['portada']))
kit['settings'].update(show_hero=False,show_card=True,padding_top=64,padding_bottom=64,cat_kicker='Qué incluye',cat_heading='Abrís la caja. Empezás tu rutina.',card_tag='Kit completo',card_eyebrow='Una herramienta, varios usos',card_text='Todo junto para recortar, limpiar y volver a cargar. Elegí la cantidad que necesitás en la página del producto.',card_cta='Elegir cantidad',card_image='shopify://shop_images/rasuradora-integral-accesorios-v1.png')
kit['blocks']['p1']['settings']['text']='Rasuradora + peines de 1, 3 y 5 mm'
kit['blocks']['p2']['settings']['text']='Cable de carga USB incluido'
kit['blocks']['p3']['settings']['text']='Cepillo para retirar los restos de vello'
sections['kit']=kit
sections['beneficios']={'type':'gv-beneficios','blocks':{},'block_order':[],'settings':{'anchor':'beneficios','kicker':'Menos aparatos. Más simple.','heading':'Cuidado personal a tu manera.','intro':'Tres detalles que hacen más práctica la rutina de todos los días.'}}
benefits=[('01','Elegí tu largo','Peines guía de 1, 3 y 5 mm para mantener el largo que buscás.'),('02','Rostro y cuerpo','Un mismo equipo para los retoques de barba y el recorte de vello corporal.'),('03','Cargá y seguí','Cable USB incluido y un formato compacto para tener a mano o llevar de viaje.')]
for i,(n,t,d) in enumerate(benefits):
 key=f'b{i}';sections['beneficios']['blocks'][key]={'type':'item','settings':{'number':n,'title':t,'text':d}};sections['beneficios']['block_order'].append(key)
sections['historia']['settings'].update(kicker='Cómo funciona',heading='Tu rutina, en tres pasos.',intro='<p>Elegí el peine, recortá con movimientos suaves y dejala lista para el próximo uso.</p>',cta_text='',padding_top=64,padding_bottom=64)
steps=sections['historia']['blocks']
steps['h1']['settings'].update(list='Peines de 1, 3 y 5 mm|Para barba y vello corporal',clip='',image='shopify://shop_images/rasuradora-integral-accesorios-v1.png')
steps['h2']['settings'].update(text='<p>Usala sobre piel limpia y seca, sin presionar. En zonas sensibles, probá primero en un área pequeña.</p>',list='Movimientos suaves|No usar sobre piel irritada',clip='',image='shopify://shop_images/rasuradora-integral-uso-v1.png')
steps['h3']['settings'].update(text='<p>Retirá los restos de vello con el cepillo incluido. Recargala con el cable USB y seguí las indicaciones del manual.</p>',list='Cepillo y cable incluidos|Limpieza en seco',clip='',image='shopify://shop_images/rasuradora-integral-hero-v1.png')
faqblocks=[
 ('¿Sirve para rostro y cuerpo?','Está pensada para recortar barba y vello corporal. Elegí el peine apropiado y usá movimientos suaves. En zonas sensibles, probá primero en un área pequeña.'),
 ('¿Qué viene en la caja?','Incluye rasuradora, peines guía de 1, 3 y 5 mm, cable de carga USB y cepillo de limpieza. La variante disponible es negro y verde lima.'),
 ('¿Se puede usar en la ducha?','La ficha disponible no certifica uso bajo el agua. Usala en seco y seguí el manual para su limpieza y carga.'),
 ('¿Cómo consulto el envío?','El costo se calcula al ingresar tu dirección durante la compra. Para confirmar los plazos de tu zona antes de pagar, escribinos a gonvra0@gmail.com.'),
 ('¿Cuánto pago si llevo más de una?','Elegís una, dos o tres unidades en la página del producto. El precio del pack corresponde a esa cantidad; podés revisar el total y el envío antes de confirmar la compra.'),
 ('¿Dónde consulto por cambios o devoluciones?','Escribinos a gonvra0@gmail.com con tu consulta. Si ya compraste, incluí el número de pedido para que podamos identificarlo.')
]
questions=sections['preguntas']
questions['blocks']={f'q{i}':{'type':'faq','settings':{'q':q,'a':f'<p>{a}</p>'}} for i,(q,a) in enumerate(faqblocks)}
questions['block_order']=list(questions['blocks'])
questions['settings'].update(kicker='Antes de decidir',sub='El producto, el pedido y las respuestas que necesitás.',contact_link='mailto:gonvra0@gmail.com',cta_heading='Más simple desde el próximo recorte.',cta_text='Revisá la rasuradora, elegí cuántas necesitás y conocé el total antes de pagar.',cta_button='Elegir mi rasuradora',cta_clip='',padding_top=64,padding_bottom=64)
sections['compra_info']={'type':'gv-beneficios','blocks':{},'block_order':[],'settings':{'anchor':'ayuda','kicker':'Comprá con la información a mano','heading':'Del primer clic a tu pedido.','intro':'Consultá lo que necesites antes de elegir.','bg':'#e9eddf','ink':'#14271e','accent':'#496020','padding_top':48,'padding_bottom':48}}
for i,(n,t,d,url) in enumerate([('01','Tu total, a la vista','Cantidad y precio del producto antes de avanzar. El envío se calcula con tu dirección.','/products/face-body-electric-shaver#comprar'),('02','Consultá tu envío','Escribinos para confirmar los plazos disponibles para tu zona.','mailto:gonvra0@gmail.com'),('03','Estamos para ayudarte','Consultas del producto, seguimiento de pedidos, cambios y devoluciones.','mailto:gonvra0@gmail.com')]):
 key=f's{i}';sections['compra_info']['blocks'][key]={'type':'item','settings':{'number':n,'title':t,'text':d,'url':url,'link_label':'Consultar' if i else 'Ver producto'}};sections['compra_info']['block_order'].append(key)
index['order']=['portada','beneficios','historia','kit','compra_info','preguntas']
for key in list(sections):
 if key not in index['order']:sections[key]['disabled']=True
putjson('templates/index.json',index)

for rel in ['templates/product.json','templates/product.tienda.json']:
 d=getjson(rel); ss=d['sections']; ficha=ss['ficha']
 ficha['settings'].update(promo_title='',promo_text='',discount_note='',show_timeline=False,show_dynamic=False,stock_text='Disponible',gallery_clip='',gallery_extra='',trust_1_t='Envíos',trust_1_s='Consultá los plazos de tu zona',trust_2_t='Atención por email',trust_2_s='Antes y después de comprar',trust_3_t='Pago en Shopify',trust_3_s='Revisá el total antes de pagar',trust_4_t='Contenido claro',trust_4_s='Accesorios detallados',price_note='Precio en ARS. El envío se calcula al ingresar tu dirección.',pill='Rasuradora + peines + cable + cepillo')
 for b in ficha['blocks'].values():
  if b['type']=='oferta':b['settings'].update(discount=0,tag='',gift='')
 ficha['blocks']['b3']['settings']['text']='Recargable por USB con el cable incluido'
 ficha['blocks']['b4']['settings']['text']='Cuchilla de acero inoxidable y cepillo de limpieza'
 ficha['blocks']['d1']['settings']['body']='<p>Rasuradora, peines guía de 1, 3 y 5 mm, cable USB y cepillo de limpieza. Color negro y verde lima.</p>'
 ficha['blocks']['d2']['settings']['body']='<p>El costo del envío se calcula con tu dirección. Para confirmar los plazos de tu zona, <a href="mailto:gonvra0@gmail.com">escribinos antes de comprar</a>.</p>'
 ficha['blocks']['d4']['settings']['body']='<p>Para consultas de cambios o devoluciones, escribinos a <a href="mailto:gonvra0@gmail.com">gonvra0@gmail.com</a>. Si ya compraste, incluí tu número de pedido.</p>'
 ss['historia']=json.loads(json.dumps(sections['historia']))
 ss['preguntas']=json.loads(json.dumps(questions));ss['preguntas']['settings']['show_cta']=False
 ss['beneficios']=json.loads(json.dumps(sections['beneficios']))
 d['order']=['ficha','beneficios','historia','preguntas']
 for k in ss:
  if k not in d['order']:ss[k]['disabled']=True
 putjson(rel,d)

h=getjson('sections/header-group.json')['sections']['gv_header']
h['blocks']['a1']['settings']['text']='Rostro y cuerpo · un solo equipo'
h['blocks']['a2']['settings']['text']='Peines de 1, 3 y 5 mm incluidos'
h['blocks']['a3']['settings']['text']='Carga USB · cable incluido'
for k,label,url in [('l1','Beneficios','/#beneficios'),('l2','Cómo se usa','/#como-funciona'),('l3','Preguntas','/#faq')]:h['blocks'][k]['settings'].update(label=label,url=url)
head=getjson('sections/header-group.json');head['sections']['gv_header']=h;putjson('sections/header-group.json',head)
f=getjson('sections/footer-group.json');foot=f['sections']['gv_footer']
foot['blocks']['c2']['settings']['links']='Preguntas frecuentes::/#faq\nEnvíos y entrega::/#ayuda\nCambios y devoluciones::mailto:gonvra0@gmail.com'
foot['blocks']['c3']['settings'].update(title='Contacto',links='Escribinos::mailto:gonvra0@gmail.com')
foot['settings']['tagline']='Cuidado personal a tu manera. Una rasuradora, tres largos y una rutina más simple.'
putjson('sections/footer-group.json',f)

meta='snippets/meta-tags.liquid'
replace(meta, '  assign og_title = page_title | default: shop.name', "  assign display_brand = settings.gv_brand | default: shop.name\n  assign seo_title = page_title\n  assign seo_description = page_description\n  if request.page_type == 'index'\n    assign seo_title = settings.gv_home_title | default: page_title\n    assign seo_description = settings.gv_home_description | default: page_description\n  endif\n  assign og_title = seo_title | default: display_brand")
replace(meta,'assign og_description = page_description | default: shop.description | default: shop.name','assign og_description = seo_description | default: shop.description | default: display_brand')
replace(meta,'content="{{ shop.name }}"','content="{{ display_brand | escape }}"')
replace(meta,'  {{ page_title }}','  {{ seo_title | escape }}')
replace(meta,'{%- unless page_title contains shop.name %} &ndash; {{ shop.name }}{% endunless -%}','{%- unless seo_title contains display_brand %} &ndash; {{ display_brand | escape }}{% endunless -%}')
replace(meta,'{% if page_description %}','{% if seo_description %}')
replace(meta,'content="{{ page_description | escape }}"','content="{{ seo_description | escape }}"')
config=getjson('config/settings_schema.json')
config.append({'name':'GONVRA · Identidad','settings':[{'type':'text','id':'gv_brand','label':'Nombre de marca','default':'GONVRA'},{'type':'text','id':'gv_home_title','label':'Título de la portada','default':'GONVRA | Rasuradora para rostro y cuerpo'},{'type':'textarea','id':'gv_home_description','label':'Descripción para buscadores','default':'Simplificá tu rutina con la rasuradora integral GONVRA. Peines de 1, 3 y 5 mm, carga USB y accesorios incluidos. Conocé el producto y elegí tu cantidad.'}]})
putjson('config/settings_schema.json',config)
settings=getjson('config/settings_data.json')
settings['current']['color_palette'].update(background='#f7f6f1',foreground='#14271e',color1='#496020',color2='#d9dfd1')
putjson('config/settings_data.json',settings)
print('Theme updated')
