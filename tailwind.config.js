/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ['./*.html'],
    darkMode: "class",
    theme: {
        extend: {
            "colors": {
                "surface-container-low": "#f3f3f3",
                "background": "#f9f9f9",
                "tertiary-fixed": "#d5e3ff",
                "primary-container": "#154481",
                "outline": "#737781",
                "on-surface": "#1a1c1c",
                "on-secondary-container": "#561b00",
                "on-secondary-fixed": "#370e00",
                "on-primary-container": "#8db3f7",
                "surface-container": "#eeeeee",
                "secondary-fixed-dim": "#ffb598",
                "surface-dim": "#dadada",
                "on-error": "#ffffff",
                "on-primary-fixed": "#001b3e",
                "primary-fixed-dim": "#aac7ff",
                "on-primary-fixed-variant": "#184683",
                "on-surface-variant": "#434750",
                "on-tertiary-fixed": "#011b3b",
                "outline-variant": "#c3c6d2",
                "inverse-surface": "#2f3131",
                "on-primary": "#ffffff",
                "secondary": "#a53c00",
                "surface-tint": "#365e9d",
                "on-tertiary": "#ffffff",
                "tertiary": "#182f4f",
                "error-container": "#ffdad6",
                "surface-bright": "#f9f9f9",
                "surface-container-lowest": "#ffffff",
                "tertiary-fixed-dim": "#b2c7f0",
                "primary": "#002e60",
                "on-tertiary-container": "#9db3da",
                "tertiary-container": "#304567",
                "secondary-container": "#fe6514",
                "surface-container-high": "#e8e8e8",
                "on-secondary-fixed-variant": "#7e2c00",
                "secondary-fixed": "#ffdbce",
                "surface-container-highest": "#e2e2e2",
                "on-error-container": "#93000a",
                "on-secondary": "#ffffff",
                "on-background": "#1a1c1c",
                "on-tertiary-fixed-variant": "#324769",
                "inverse-on-surface": "#f1f1f1",
                "surface-variant": "#e2e2e2",
                "primary-fixed": "#d6e3ff",
                "inverse-primary": "#aac7ff",
                "surface": "#f9f9f9",
                "error": "#ba1a1a"
            },
            "borderRadius": {
                "DEFAULT": "0.125rem",
                "lg": "0.25rem",
                "xl": "0.5rem",
                "full": "0.75rem"
            },
            "spacing": {
                "stack-lg": "64px",
                "container-max": "1140px",
                "gutter": "24px",
                "margin-page": "32px",
                "unit": "8px",
                "stack-sm": "16px",
                "stack-md": "32px"
            },
            "fontFamily": {
                "body-lg": ["Public Sans"],
                "body-md": ["Public Sans"],
                "headline-sm": ["Public Sans"],
                "label-lg": ["Public Sans"],
                "label-sm": ["Public Sans"],
                "headline-md": ["Public Sans"],
                "headline-xl": ["Public Sans"],
                "headline-lg": ["Public Sans"]
            },
            "fontSize": {
                "body-lg": ["18px", { "lineHeight": "28px", "fontWeight": "400" }],
                "body-md": ["16px", { "lineHeight": "24px", "fontWeight": "400" }],
                "headline-sm": ["20px", { "lineHeight": "28px", "fontWeight": "600" }],
                "label-lg": ["14px", { "lineHeight": "20px", "letterSpacing": "0.05em", "fontWeight": "600" }],
                "label-sm": ["12px", { "lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "600" }],
                "headline-md": ["24px", { "lineHeight": "36px", "fontWeight": "600" }],
                "headline-xl": ["34px", { "lineHeight": "44px", "fontWeight": "700" }],
                "headline-lg": ["28px", { "lineHeight": "38px", "fontWeight": "700" }]
            }
        }
    }
};
