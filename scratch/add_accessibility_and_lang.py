import os
import re

workspace_dir = "c:\\Users\\nexus\\OneDrive\\Documentos\\ProyectosWeb\\avpcelespinar\\avpcelespinar-template"

# Get all HTML files in the workspace
html_files = [f for f in os.listdir(workspace_dir) if f.endswith(".html")]

multilingual_topbar_target = r"<!-- Barra superior del Ayuntamiento \(Estandarizada\) -->\s*<div class=\"bg-primary text-white py-1\.5 px-4 text-xs font-medium border-b border-primary-container\">\s*<div class=\"max-w-\[1140px\] mx-auto flex justify-between items-center\">\s*<span class=\"opacity-80\">Protección Civil El Espinar \(Segovia\)</span>\s*<a class=\"hover:underline flex items-center gap-1 hover:opacity-100 transition-opacity\" href=\"http://elespinar\.es/\" target=\"_blank\" rel=\"noopener noreferrer\">\s*<span class=\"material-symbols-outlined text-xs\" style=\"font-variation-settings: 'FILL' 1;\">account_balance</span>\s*Ayuntamiento de El Espinar\s*</a>\s*</div>\s*</div>"

multilingual_topbar_replacement = """<!-- Barra superior del Ayuntamiento (Estandarizada) -->
    <div class="bg-primary text-white py-1.5 px-4 text-xs font-medium border-b border-primary-container">
        <div class="max-w-[1140px] mx-auto flex justify-between items-center">
            <span class="opacity-80">Protección Civil El Espinar (Segovia)</span>
            <div class="flex items-center gap-6">
                <a class="hover:underline flex items-center gap-1 hover:opacity-100 transition-opacity" href="http://elespinar.es/" target="_blank" rel="noopener noreferrer">
                    <span class="material-symbols-outlined text-xs" style="font-variation-settings: 'FILL' 1;">account_balance</span>
                    Ayuntamiento de El Espinar
                </a>
                <span class="opacity-30">|</span>
                <div class="flex items-center gap-2 font-semibold">
                    <button class="hover:text-secondary-container transition-colors text-white font-bold" id="lang-es">ES</button>
                    <span class="opacity-30">/</span>
                    <button class="hover:text-secondary-container transition-colors opacity-75 font-normal" id="lang-en">EN</button>
                </div>
            </div>
        </div>
    </div>"""

# Floating Accessibility Widget HTML & CSS & JS
accessibility_widget_inject = """<!-- Botón Flotante de Accesibilidad -->
<div class="fixed bottom-6 right-6 z-50 font-['Public_Sans']">
    <button id="accessibility-widget-toggle" class="w-14 h-14 bg-secondary-container text-white rounded-full flex items-center justify-center shadow-lg hover:scale-110 active:scale-95 transition-all focus:outline-none" aria-label="Opciones de Accesibilidad">
        <span class="material-symbols-outlined text-2xl" style="font-variation-settings: 'FILL' 1;">accessibility</span>
    </button>
    <!-- Menú de Accesibilidad Flotante -->
    <div id="accessibility-menu" class="hidden absolute bottom-16 right-0 bg-white dark:bg-slate-900 border border-outline-variant dark:border-slate-800 rounded-2xl p-6 shadow-xl w-72 flex flex-col gap-4 text-on-surface">
        <div class="border-b border-slate-100 dark:border-slate-800 pb-3 flex justify-between items-center">
            <h4 class="font-bold text-[#154481] dark:text-white flex items-center gap-2 text-sm">
                <span class="material-symbols-outlined text-lg" style="font-variation-settings: 'FILL' 1;">accessibility</span>
                Accesibilidad
            </h4>
            <button id="accessibility-menu-close" class="text-slate-400 hover:text-slate-600 dark:hover:text-slate-200">
                <span class="material-symbols-outlined text-lg">close</span>
            </button>
        </div>
        <!-- Opción 1: Contraste -->
        <div class="flex flex-col gap-2">
            <span class="text-[10px] font-semibold uppercase tracking-wider text-slate-400">Contraste</span>
            <div class="grid grid-cols-2 gap-2">
                <button id="acc-contrast-normal" class="py-2 px-3 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-[11px] font-bold rounded-lg border border-transparent transition-colors">Estándar</button>
                <button id="acc-contrast-high" class="py-2 px-3 bg-slate-950 text-yellow-400 hover:bg-black text-[11px] font-bold rounded-lg border border-yellow-400 transition-colors">Alto Contraste</button>
            </div>
        </div>
        <!-- Opción 2: Tamaño de Letra -->
        <div class="flex flex-col gap-2">
            <span class="text-[10px] font-semibold uppercase tracking-wider text-slate-400">Tamaño de Texto</span>
            <div class="grid grid-cols-3 gap-2">
                <button id="acc-text-decrease" class="py-2 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-xs font-bold rounded-lg transition-colors">- A</button>
                <button id="acc-text-reset" class="py-2 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-xs font-bold rounded-lg transition-colors">Normal</button>
                <button id="acc-text-increase" class="py-2 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-xs font-bold rounded-lg transition-colors">+ A</button>
            </div>
        </div>
        <!-- Opción 3: Lector de Pantalla (Voz) -->
        <div class="flex flex-col gap-2">
            <span class="text-[10px] font-semibold uppercase tracking-wider text-slate-400">Lectura de Pantalla</span>
            <button id="acc-speak-toggle" class="flex items-center justify-center gap-2 py-2.5 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-xs font-bold rounded-lg w-full transition-colors">
                <span class="material-symbols-outlined text-sm">volume_up</span>
                <span>Activar Lector de Voz</span>
            </button>
        </div>
    </div>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        // --- 1. Selector de Idioma (Simulación) ---
        const langEsBtn = document.getElementById('lang-es');
        const langEnBtn = document.getElementById('lang-en');
        
        if (langEsBtn && langEnBtn) {
            const currentLang = localStorage.getItem('pc-lang') || 'es';
            
            const updateLangUI = (lang) => {
                if (lang === 'es') {
                    langEsBtn.classList.add('font-bold');
                    langEsBtn.classList.remove('opacity-75', 'font-normal');
                    langEnBtn.classList.add('opacity-75', 'font-normal');
                    langEnBtn.classList.remove('font-bold');
                } else {
                    langEnBtn.classList.add('font-bold');
                    langEnBtn.classList.remove('opacity-75', 'font-normal');
                    langEsBtn.classList.add('opacity-75', 'font-normal');
                    langEsBtn.classList.remove('font-bold');
                }
            };
            
            updateLangUI(currentLang);
            
            const handleLangToggle = (lang) => {
                localStorage.setItem('pc-lang', lang);
                updateLangUI(lang);
                
                // Mostrar notificación elegante (toast)
                const toast = document.createElement('div');
                toast.className = 'fixed bottom-24 left-6 z-50 bg-[#154481] text-white py-3 px-6 rounded-lg shadow-xl font-semibold text-sm transition-all duration-300 transform translate-y-10 opacity-0';
                toast.innerText = lang === 'es' ? 'Idioma cambiado a Español (Simulación)' : 'Language switched to English (Simulation)';
                document.body.appendChild(toast);
                
                setTimeout(() => {
                    toast.classList.remove('translate-y-10', 'opacity-0');
                }, 50);
                
                setTimeout(() => {
                    toast.classList.add('translate-y-10', 'opacity-0');
                    setTimeout(() => toast.remove(), 300);
                }, 3000);
            };
            
            langEsBtn.addEventListener('click', () => handleLangToggle('es'));
            langEnBtn.addEventListener('click', () => handleLangToggle('en'));
        }

        // --- 2. Widget de Accesibilidad ---
        const accToggle = document.getElementById('accessibility-widget-toggle');
        const accMenu = document.getElementById('accessibility-menu');
        const accClose = document.getElementById('accessibility-menu-close');
        
        if (accToggle && accMenu && accClose) {
            accToggle.addEventListener('click', () => {
                accMenu.classList.toggle('hidden');
            });
            accClose.addEventListener('click', () => {
                accMenu.classList.add('hidden');
            });
            document.addEventListener('click', (e) => {
                if (!accToggle.contains(e.target) && !accMenu.contains(e.target)) {
                    accMenu.classList.add('hidden');
                }
            });
        }

        // --- 3. Funciones de Accesibilidad ---
        // A. Contraste
        const contrastNormal = document.getElementById('acc-contrast-normal');
        const contrastHigh = document.getElementById('acc-contrast-high');
        
        // Estilos CSS globales inyectados para el alto contraste
        const hcStyleId = 'accessibility-high-contrast-styles';
        if (!document.getElementById(hcStyleId)) {
            const hcStyle = document.createElement('style');
            hcStyle.id = hcStyleId;
            hcStyle.innerHTML = `
                .hc-active, .hc-active * {
                    background-color: #000000 !important;
                    color: #ffff00 !important;
                    border-color: #ffff00 !important;
                    text-shadow: none !important;
                    box-shadow: none !important;
                }
                .hc-active img, .hc-active video, .hc-active svg {
                    filter: grayscale(1) contrast(1.5) !important;
                }
                .hc-active button, .hc-active a {
                    outline: 2px solid #ffff00 !important;
                    background-color: #000000 !important;
                    color: #ffff00 !important;
                }
                .hc-active button:hover, .hc-active a:hover {
                    background-color: #ffff00 !important;
                    color: #000000 !important;
                }
            `;
            document.head.appendChild(hcStyle);
        }

        const applyContrast = (hc) => {
            if (hc === 'true') {
                document.documentElement.classList.add('hc-active');
                if (contrastHigh) contrastHigh.classList.add('border-2');
                if (contrastNormal) contrastNormal.classList.remove('border-primary-container', 'border-2');
            } else {
                document.documentElement.classList.remove('hc-active');
                if (contrastHigh) contrastHigh.classList.remove('border-2');
                if (contrastNormal) {
                    contrastNormal.classList.add('border-primary-container', 'border-2');
                }
            }
        };

        const activeContrast = localStorage.getItem('acc-contrast') || 'false';
        applyContrast(activeContrast);

        if (contrastNormal) {
            contrastNormal.addEventListener('click', () => {
                localStorage.setItem('acc-contrast', 'false');
                applyContrast('false');
            });
        }
        if (contrastHigh) {
            contrastHigh.addEventListener('click', () => {
                localStorage.setItem('acc-contrast', 'true');
                applyContrast('true');
            });
        }

        // B. Tamaño de Texto
        const textDecrease = document.getElementById('acc-text-decrease');
        const textReset = document.getElementById('acc-text-reset');
        const textIncrease = document.getElementById('acc-text-increase');

        const applyFontSize = (size) => {
            document.body.style.fontSize = size + '%';
        };

        let activeFontSize = parseInt(localStorage.getItem('acc-fontsize') || '100');
        applyFontSize(activeFontSize);

        if (textDecrease) {
            textDecrease.addEventListener('click', () => {
                activeFontSize = Math.max(80, activeFontSize - 10);
                localStorage.setItem('acc-fontsize', activeFontSize.toString());
                applyFontSize(activeFontSize);
            });
        }
        if (textReset) {
            textReset.addEventListener('click', () => {
                activeFontSize = 100;
                localStorage.setItem('acc-fontsize', '100');
                applyFontSize(100);
            });
        }
        if (textIncrease) {
            textIncrease.addEventListener('click', () => {
                activeFontSize = Math.min(140, activeFontSize + 10);
                localStorage.setItem('acc-fontsize', activeFontSize.toString());
                applyFontSize(activeFontSize);
            });
        }

        // C. Lector de Pantalla por Voz (Speech Synthesis)
        const speakToggle = document.getElementById('acc-speak-toggle');
        let isSpeakingActive = localStorage.getItem('acc-speaking') === 'true';

        const updateSpeakUI = () => {
            if (!speakToggle) return;
            const span = speakToggle.querySelector('span:last-child');
            if (isSpeakingActive) {
                speakToggle.classList.add('bg-primary', 'text-white');
                speakToggle.classList.remove('bg-slate-100', 'dark:bg-slate-800');
                if (span) span.innerText = 'Desactivar Voz';
            } else {
                speakToggle.classList.remove('bg-primary', 'text-white');
                speakToggle.classList.add('bg-slate-100', 'dark:bg-slate-800');
                if (span) span.innerText = 'Activar Lector de Voz';
            }
        };

        updateSpeakUI();

        const speakText = (text) => {
            if (!isSpeakingActive) return;
            window.speechSynthesis.cancel();
            if (!text || text.trim() === '') return;
            
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = 'es-ES';
            window.speechSynthesis.speak(utterance);
        };

        if (speakToggle) {
            speakToggle.addEventListener('click', () => {
                isSpeakingActive = !isSpeakingActive;
                localStorage.setItem('acc-speaking', isSpeakingActive.toString());
                updateSpeakUI();
                if (!isSpeakingActive) {
                    window.speechSynthesis.cancel();
                } else {
                    speakText("Lector de voz activado. Pase el ratón sobre cualquier texto para escucharlo.");
                }
            });
        }

        // Eventos mouseover para hablar
        document.body.addEventListener('mouseover', (e) => {
            if (!isSpeakingActive) return;
            const target = e.target;
            const readableTags = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'P', 'SPAN', 'A', 'BUTTON', 'LI', 'STRONG'];
            if (readableTags.includes(target.tagName)) {
                // Evitar hablar si el elemento contiene hijos legibles para no repetir
                const text = target.innerText || target.textContent;
                speakText(text);
            }
        });
    });
</script>
</body>"""

print(f"Modifying {len(html_files)} HTML files...")

for file_name in html_files:
    file_path = os.path.join(workspace_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False

    # 1. Replace top bar with multilingual version
    new_content, count = re.subn(multilingual_topbar_target, multilingual_topbar_replacement, content, flags=re.IGNORECASE)
    if count > 0:
        content = new_content
        modified = True
    else:
        # Try a simpler replace if full regex failed due to whitespace/formatting discrepancies
        simple_target = "<!-- Barra superior del Ayuntamiento (Estandarizada) -->"
        if simple_target in content:
            # Let's locate the full block and replace it manually
            start_idx = content.find(simple_target)
            end_idx = content.find("</div>", start_idx) # outer div close
            end_idx = content.find("</div>", end_idx + 6) # second outer div close (container)
            end_idx = content.find("</div>", end_idx + 6) # check how many divs it had
            # Wait, let's just use regex with looser spaces
            loose_regex = r"<!-- Barra superior del Ayuntamiento \(Estandarizada\) -->\s*<div[^>]*>.*?</a>\s*</div>\s*</div>"
            content, count = re.subn(loose_regex, multilingual_topbar_replacement, content, flags=re.DOTALL)
            if count > 0:
                modified = True

    # 2. Inject Accessibility Widget before </body>
    if "</body>" in content and "accessibility-widget-toggle" not in content:
        content = content.replace("</body>", accessibility_widget_inject)
        modified = True

    if modified:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f" [+] Modified {file_name}")
    else:
        print(f" [-] No changes made to {file_name}")

print("Multilingual and Accessibility updates completed successfully!")
