// Pruebas reales con Chromium aislado; no controla la sesión personal del navegador.
// npm install playwright; CHROME_PATH puede señalar una instalación local de Chrome.
const fs=require('fs');const path=require('path');const http=require('http');
const {chromium}=require('playwright');
const root=path.resolve(process.argv[2]||path.join(__dirname,'..'));
const out=path.join(root,'evidencias/validacion');fs.mkdirSync(out,{recursive:true});
const mime={'.html':'text/html; charset=utf-8','.htm':'text/html; charset=utf-8','.jpg':'image/jpeg','.json':'application/json','.jsonld':'application/ld+json','.md':'text/plain; charset=utf-8','.png':'image/png'};
const server=http.createServer((req,res)=>{
  let name=decodeURIComponent(new URL(req.url,'http://localhost').pathname);if(name==='/')name='/index.html';
  const p=path.resolve(root,'.'+name);
  if(!p.startsWith(root+path.sep)||!fs.existsSync(p)||!fs.statSync(p).isFile()){res.writeHead(404);return res.end('No encontrado');}
  res.writeHead(200,{'Content-Type':mime[path.extname(p)]||'application/octet-stream','Cache-Control':'no-store'});fs.createReadStream(p).pipe(res);
});
(async()=>{
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));const base=`http://127.0.0.1:${server.address().port}`;
 const browser=await chromium.launch({headless:true,...(process.env.CHROME_PATH?{executablePath:process.env.CHROME_PATH}:{})});
 const report={executedAt:new Date().toISOString(),browser:await browser.version(),base,method:'Contexto nuevo por ancho y DPR; caché de servidor desactivada; lectura de currentSrc y respuestas HTTP. Capturas automatizadas, no capturas de DevTools.',responsive:[],pages:[],failures:[]};
 for(const dpr of [1,2])for(const width of [320,375,767,768,1199,1200,1440]){
  const context=await browser.newContext({viewport:{width,height:900},deviceScaleFactor:dpr});const page=await context.newPage();const responses=[];const errors=[];
  page.on('response',r=>responses.push({url:r.url(),status:r.status(),resource:r.request().resourceType()}));page.on('pageerror',e=>errors.push(String(e)));
  await page.goto(base+'/galeria.html',{waitUntil:'networkidle'});
  const images=await page.locator('picture img').evaluateAll(els=>els.map(e=>({alt:e.alt,currentSrc:e.currentSrc,naturalWidth:e.naturalWidth,naturalHeight:e.naturalHeight,renderedWidth:e.width,renderedHeight:e.height,complete:e.complete})));
  const expected=width>=1200?1920:width>=768?768:480;
  const imageResponses=responses.filter(r=>r.resource==='image');
  const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
  const pass=images.length===3&&images.every(i=>i.complete&&i.naturalWidth===expected&&i.currentSrc.endsWith(`-${expected}w.jpg`))&&imageResponses.length===3&&imageResponses.every(r=>r.status===200&&r.url.endsWith(`-${expected}w.jpg`))&&!errors.length&&!overflow;
  report.responsive.push({width,dpr,expected,pass,overflow,images,requests:imageResponses,errors});
  if(!pass)report.failures.push(`Responsive ${width}px DPR ${dpr}`);
  if(dpr===1&&[375,768,1200].includes(width))await page.screenshot({path:path.join(out,`galeria-${width}px.png`),fullPage:true});
  await context.close();
 }
 const pages=['index.html','maquinas.html','maquina-extension-piernas.html','galeria.html','galeria.htm','docs/licencias_recursos.html','docs/entrega-3-2.html'];
 for(const filename of pages){
  const context=await browser.newContext({viewport:{width:1280,height:900}});const page=await context.newPage();const errors=[];page.on('pageerror',e=>errors.push(String(e)));
  const r=await page.goto(base+'/'+filename,{waitUntil:'networkidle'});
  const summary=await page.evaluate(()=>({title:document.title,h1:document.querySelectorAll('h1').length,main:document.querySelectorAll('main').length,lang:document.documentElement.lang,brokenImages:[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src),headings:[...document.querySelectorAll('h1,h2,h3,h4')].map(e=>e.tagName+': '+e.textContent.trim())}));
  let keyboard=null;
  if(filename==='galeria.html'){
    await page.keyboard.press('Tab');const first=await page.evaluate(()=>document.activeElement.getAttribute('href'));await page.keyboard.press('Enter');const jumped=await page.evaluate(()=>document.activeElement.id==='contenido');
    await page.keyboard.press('Tab');const following=await page.evaluate(()=>document.activeElement.textContent.trim());keyboard={first,jumped,following};
    await page.screenshot({path:path.join(out,'teclado-salto-contenido.png'),fullPage:false});
    if(first!=='#contenido'||!jumped)report.failures.push('Salto con teclado');
  }
  const entry={filename,status:r.status(),...summary,keyboard,errors};report.pages.push(entry);
  if(r.status()!==200||summary.h1!==1||summary.main!==1||summary.lang!=='es'||summary.brokenImages.length||errors.length)report.failures.push(filename);
  await context.close();
 }
 {
  const context=await browser.newContext({viewport:{width:1200,height:1000}});await context.route('**/assets/images/**',route=>route.abort('blockedbyclient'));const page=await context.newPage();await page.goto(base+'/galeria.html',{waitUntil:'networkidle'});
  const blocked=await page.locator('img').evaluateAll(els=>els.map(e=>({alt:e.alt,naturalWidth:e.naturalWidth,complete:e.complete})));
  report.withoutImages={blocked,figcaptions:await page.locator('figcaption').count(),articles:await page.locator('article').count(),method:'Petición de cada JPEG bloqueada antes de cargar. Se conserva el texto alternativo y el contenido HTML.'};
  if(blocked.length!==3||blocked.some(i=>!i.alt||i.naturalWidth!==0))report.failures.push('Imágenes bloqueadas');
  await page.screenshot({path:path.join(out,'accesibilidad_sin_imagenes.png'),fullPage:true});await context.close();
 }
 report.result=report.failures.length?'FAIL':'PASS';fs.writeFileSync(path.join(out,'navegador.json'),JSON.stringify(report,null,2));
 console.log(JSON.stringify({result:report.result,browser:report.browser,responsive:report.responsive.length,pages:report.pages.length,failures:report.failures}));
 await browser.close();server.close();process.exitCode=report.failures.length?1:0;
})().catch(e=>{console.error(e);server.close();process.exitCode=1});
