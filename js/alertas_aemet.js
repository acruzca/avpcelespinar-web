document.addEventListener('DOMContentLoaded', () => {
    // URL of the generated JSON (could be absolute or relative depending on host)
    const jsonUrl = 'data/alertas_aemet.json';
    
    fetch(jsonUrl)
        .then(response => {
            if (!response.ok) throw new Error('No alertas JSON found');
            return response.json();
        })
        .then(data => {
            const alertas = data.alertas || [];
            updateBanner(alertas);
            updateAvisosPage(alertas);
        })
        .catch(error => {
            console.error('Error loading alerts:', error);
            // Default to showing green banner if there's an error (assuming normal)
            updateBanner([]);
            updateAvisosPage([]);
        });

    function updateBanner(alertas) {
        const banner = document.getElementById('alert-banner');
        if (!banner) return;
        
        // Find highest severity alert
        let highestAlert = null;
        if (alertas.find(a => a.nivel === 'Rojo')) {
            highestAlert = alertas.find(a => a.nivel === 'Rojo');
        } else if (alertas.find(a => a.nivel === 'Naranja')) {
            highestAlert = alertas.find(a => a.nivel === 'Naranja');
        } else if (alertas.find(a => a.nivel === 'Amarillo')) {
            highestAlert = alertas.find(a => a.nivel === 'Amarillo');
        }

        // Reset base classes
        banner.className = "py-2 px-4 text-center text-sm font-bold sticky top-0 z-[60] border-b";
        banner.style.display = 'block';

        const textSpan = banner.querySelector('span:nth-child(2)');
        const iconSpan = banner.querySelector('span:nth-child(1)');
        const linkWrapper = banner.querySelector('a');
        const linkText = banner.querySelector('a span:first-child');
        const linkIcon = banner.querySelector('a span:last-child');
        const closeBtn = banner.querySelector('button');
        
        // Helper to reset inner elements colors
        if (linkText) { linkText.className = "underline font-bold"; }
        if (linkIcon) { linkIcon.className = "material-symbols-outlined text-sm ml-0.5"; }
        if (closeBtn) { closeBtn.className = "absolute right-0 transition-all p-1 hover:scale-110"; }

        if (highestAlert) {
            if (highestAlert.nivel === 'Rojo') {
                banner.classList.add('bg-[#ba1a1a]', 'text-white', 'border-red-800');
                iconSpan.textContent = '🚨';
                if (linkText) linkText.classList.add('text-white');
                if (linkIcon) linkIcon.classList.add('text-white');
                if (closeBtn) closeBtn.classList.add('text-white/80', 'hover:text-white');
            } else if (highestAlert.nivel === 'Naranja') {
                banner.classList.add('bg-[#a53c00]', 'text-white', 'border-orange-800');
                iconSpan.textContent = '⚠️';
                if (linkText) linkText.classList.add('text-white');
                if (linkIcon) linkIcon.classList.add('text-white');
                if (closeBtn) closeBtn.classList.add('text-white/80', 'hover:text-white');
            } else if (highestAlert.nivel === 'Amarillo') {
                banner.classList.add('bg-[#D4AF37]', 'text-slate-900', 'border-yellow-600');
                iconSpan.textContent = '⚠️';
                if (linkText) linkText.classList.add('text-slate-900');
                if (linkIcon) linkIcon.classList.add('text-slate-900');
                if (closeBtn) closeBtn.classList.add('text-slate-700', 'hover:text-slate-900');
            }
            if (textSpan) {
                textSpan.textContent = `Aviso Meteorológico (${highestAlert.nivel}): ${highestAlert.titulo}`;
            }
            if (linkText) linkText.textContent = "Más información";
        } else {
            // Verde - Todo OK
            banner.classList.add('bg-[#2E7D32]', 'text-white', 'border-green-800');
            iconSpan.textContent = '✅';
            if (linkText) {
                linkText.classList.add('text-white');
                linkText.textContent = "Ver estado";
            }
            if (linkIcon) linkIcon.classList.add('text-white');
            if (closeBtn) closeBtn.classList.add('text-white/80', 'hover:text-white');
            
            if (textSpan) {
                textSpan.textContent = 'Situación Normal: No hay avisos meteorológicos activos en la zona.';
            }
        }
    }

    function updateAvisosPage(alertas) {
        const container = document.getElementById('alertas-container');
        if (!container) return; // Not on avisos.html
        
        container.innerHTML = ''; // Clear loading or dummy text
        
        if (alertas.length === 0) {
            // Show Green normal status
            container.innerHTML = `
                <article class="bg-surface-container-lowest border border-[#2E7D32] rounded-lg p-6 relative overflow-hidden shadow-sm">
                    <div class="absolute top-0 left-0 w-2 h-full bg-[#2E7D32]"></div>
                    <div class="flex items-start gap-4">
                        <div class="bg-[#E8F5E9] p-3 rounded-full shrink-0">
                            <span class="material-symbols-outlined text-[#2E7D32] text-3xl" style="font-variation-settings: 'FILL' 1;">check_circle</span>
                        </div>
                        <div class="flex-1">
                            <span class="text-[#2E7D32] font-label-sm text-label-sm uppercase tracking-wider font-bold">Situación Normal</span>
                            <h3 class="font-headline-sm text-headline-sm text-on-surface font-bold mt-1 mb-2">Sin alertas activas</h3>
                            <p class="text-body-md font-body-md text-on-surface-variant mb-4">
                                Actualmente no hay avisos meteorológicos en vigor para la zona del Sistema Central de Segovia ni Meseta.
                            </p>
                        </div>
                    </div>
                </article>
            `;
            return;
        }

        const levelConfig = {
            'Rojo': { color: '#ba1a1a', bg: 'bg-error-container', icon: 'warning' },
            'Naranja': { color: '#a53c00', bg: 'bg-secondary-fixed', icon: 'air' },
            'Amarillo': { color: '#D4AF37', bg: 'bg-[#FFF8E7]', icon: 'thermostat' }
        };

        alertas.forEach(alerta => {
            const config = levelConfig[alerta.nivel] || levelConfig['Amarillo'];
            
            const article = document.createElement('article');
            article.className = `bg-surface-container-lowest border rounded-lg p-6 relative overflow-hidden shadow-sm mb-4`;
            article.style.borderColor = config.color;
            
            article.innerHTML = `
                <div class="absolute top-0 left-0 w-2 h-full" style="background-color: ${config.color};"></div>
                <div class="flex items-start gap-4">
                    <div class="${config.bg} p-3 rounded-full shrink-0">
                        <span class="material-symbols-outlined text-3xl" style="color: ${config.color}; font-variation-settings: 'FILL' 1;">${config.icon}</span>
                    </div>
                    <div class="flex-1">
                        <div class="flex justify-between items-start mb-2">
                            <div>
                                <span class="font-label-sm text-label-sm uppercase tracking-wider font-bold" style="color: ${config.color};">Nivel ${alerta.nivel}</span>
                                <h3 class="font-headline-sm text-headline-sm text-on-surface font-bold mt-1 mb-2">${alerta.titulo}</h3>
                            </div>
                            <span class="bg-surface-container-high px-2 py-1 rounded text-label-sm font-label-sm text-on-surface-variant flex items-center gap-1">
                                <span class="material-symbols-outlined text-[14px]">schedule</span>
                                ${alerta.valido_hasta || 'En vigor'}
                            </span>
                        </div>
                        <p class="text-body-md font-body-md text-on-surface-variant mb-4">
                            ${alerta.descripcion}
                        </p>
                    </div>
                </div>
            `;
            container.appendChild(article);
        });
    }
});
