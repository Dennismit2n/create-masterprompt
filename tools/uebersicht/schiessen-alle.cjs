// Rendert jede index-<code>.html in diesem Ordner zu uebersicht-<code>.png.
// Aufruf: node schiessen-alle.cjs [code ...]   (ohne Argumente: alle)
// Playwright kommt aus PLAYWRIGHT_PATH (Pfad zu einem node_modules/playwright)
// oder, ohne die Variable, per gewoehnlichem require('playwright').
const { chromium } = require(process.env.PLAYWRIGHT_PATH || 'playwright');
const fs = require('fs');
const path = require('path');

const HIER = __dirname.replace(/\\/g, '/');
const codes = process.argv.slice(2).length
  ? process.argv.slice(2)
  : fs.readdirSync(HIER).filter(f => /^index-[a-z]{2}\.html$/.test(f)).map(f => f.slice(6, 8)).sort();

(async () => {
  const browser = await chromium.launch();
  for (const code of codes) {
    const seite = await browser.newPage({ viewport: { width: 1100, height: 1200 }, deviceScaleFactor: 1.5 });
    await seite.goto('file:///' + HIER + '/index-' + code + '.html', { waitUntil: 'networkidle' });
    // Schriften fuer CJK/Devanagari laden ggf. nach — kurz warten, bis das Layout steht
    await seite.evaluate(() => document.fonts.ready);
    const blatt = seite.locator('.blatt');
    const box = await blatt.boundingBox();
    // Ueberlauf-Check: kein Element darf breiter als das Blatt sein
    const ueberlauf = await seite.evaluate(() => {
      const b = document.querySelector('.blatt').getBoundingClientRect();
      return [...document.querySelectorAll('.blatt *')]
        .filter(el => el.getBoundingClientRect().right > b.right + 1)
        .map(el => el.className || el.tagName).slice(0, 5);
    });
    await blatt.screenshot({ path: HIER + '/uebersicht-' + code + '.png' });
    console.log(code + ': ' + Math.round(box.width) + ' x ' + Math.round(box.height) + ' CSS-px'
      + (ueberlauf.length ? '   UEBERLAUF: ' + ueberlauf.join(', ') : ''));
    await seite.close();
  }
  await browser.close();
})();
