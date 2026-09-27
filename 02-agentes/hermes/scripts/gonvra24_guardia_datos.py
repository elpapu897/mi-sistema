#!/usr/bin/env python3
"""Lectura pública acotada. No compras, carritos nuevos ni API de pago."""
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from zoneinfo import ZoneInfo
from urllib.request import Request, urlopen

BASE = 'https://gonvra.com'

def fetch(path):
    try:
        request = Request(BASE + path, headers={'User-Agent': 'GONVRA-health-readonly/1.0'})
        with urlopen(request, timeout=18) as response:
            body = response.read(1500000)
            result = {'path': path, 'status': response.status, 'final_url': response.url}
            if path.startswith('/products.json'):
                products = json.loads(body).get('products', [])
                result['products'] = [{'id': p['id'], 'title': p['title'], 'handle': p['handle'], 'variants': [{'id': v['id'], 'price': v.get('price'), 'available': v.get('available')} for v in p.get('variants', [])]} for p in products]
                result['catalog_complete'] = len(products) < 250
            return result
    except Exception as exc:
        return {'path': path, 'error_type': type(exc).__name__, 'status': getattr(exc, 'code', None)}

def main():
    paths = ['/', '/cart.js', '/checkout', '/products.json?limit=250']
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(fetch, paths))
    print(json.dumps({'checked_at': datetime.now(ZoneInfo('America/Argentina/Buenos_Aires')).isoformat(), 'checks': results,
      'limits': ['Checkout con carrito vacío: HTTP/redirect NO verifica cobro ni pago real.', 'available refleja disponibilidad pública, NO unidades reales del proveedor.', 'Sin fuente autenticada de pedidos/analytics verificada: ventas, embudo y abandonos NO OBSERVABLES, no cero.']}, ensure_ascii=False))

if __name__ == '__main__':
    main()
