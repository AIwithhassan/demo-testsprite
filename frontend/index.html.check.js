const fs = require('fs');
const html = fs.readFileSync('frontend/index.html', 'utf8');
const m = html.match(/<script>([\s\S]*?)<\/script>/);
if (!m) { console.error('No script block'); process.exit(1); }
try { new Function(m[1]); console.log('JS syntax OK'); }
catch(e) { console.error('JS error:', e.message); process.exit(1); }
