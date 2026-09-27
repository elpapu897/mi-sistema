const fs = require('fs');
const path = require('path');

const dir = '/home/matiigonzz/tiendas/gonvra-auditoria-2026/templates';
const files = fs.readdirSync(dir).filter(f => (f.startsWith('product.') || f === 'index.json') && f.endsWith('.json'));

for (const file of files) {
  const filePath = path.join(dir, file);
  let content = fs.readFileSync(filePath, 'utf8');
  let cleanContent = content.replace(/\/\*[\s\S]*?\*\//g, '');
  let json = JSON.parse(cleanContent);
  let modified = false;

  // Remove Loox blocks
  if (json.sections) {
    for (const [sectionId, section] of Object.entries(json.sections)) {
      if (section.blocks) {
        for (const [blockId, block] of Object.entries(section.blocks)) {
          if (block.type && (block.type.includes('loox') || block.type.includes('judge'))) {
            delete section.blocks[blockId];
            section.block_order = section.block_order.filter(id => id !== blockId);
            modified = true;
          }
        }
      }
    }
  }

  // Convert back to string for global text replacements
  let str = JSON.stringify(json, null, 2);
  let initialStr = str;
  
  str = str.replace(/Garantía de 7 días/g, 'Garantía de 10 días');
  str = str.replace(/Garantía 7 días/g, 'Garantía 10 días');
  str = str.replace(/Soporte ortopédico/gi, 'Soporte completo');
  str = str.replace(/diseño ortopédico/gi, 'diseño anatómico');
  str = str.replace(/Cuida las articulaciones/gi, 'Comodidad para el día a día');
  str = str.replace(/Materiales seguros/gi, 'Materiales seleccionados');
  str = str.replace(/gonvra0@gmail\.com/g, 'contacto@gonvra.com');
  
  if (str !== initialStr) {
    modified = true;
  }

  if (modified) {
    fs.writeFileSync(filePath, str, 'utf8');
    console.log(`Modified ${file}`);
  }
}
