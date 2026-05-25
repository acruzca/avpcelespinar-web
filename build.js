const postcss = require('postcss');
const tailwindcss = require('tailwindcss');
const fs = require('fs');

const css = fs.readFileSync('css/input.css', 'utf8');

postcss([
  tailwindcss('./tailwind.config.js'),
])
.process(css, { from: 'css/input.css', to: 'css/style.css' })
.then(result => {
  fs.writeFileSync('css/style.css', result.css);
  console.log('Tailwind compiled successfully via PostCSS API');
})
.catch(err => {
  console.error(err);
  process.exit(1);
});
