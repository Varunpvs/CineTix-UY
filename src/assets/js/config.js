/**
 * Config
 * -------------------------------------------------------------------------------------
 * ! IMPORTANT: Make sure you clear the browser local storage In order to see the config changes in the template.
 * ! To clear local storage: (https://www.leadshook.com/help/how-to-clear-local-storage-in-google-chrome-browser/).
 */

'use strict';

// JS global variables
window.config = {
  colors: {
    primary: '#ffde00',
    secondary: '#8a8d93',
    success: '#56ca00',
    info: '#16b1ff',
    warning: '#ffb400',
    danger: '#ff4c51',
    dark: '#4b4b4b',
    black: '#2e263d',
    white: '#fff',
    cardColor: '#fff',
    bodyBg: '#f4f5fa',
    bodyColor: '#6D6777',
    headingColor: '#433C50',
    textMuted: '#ABA8B1',
    borderColor: '#E6E5E8',
    chartBgColor: '#F0F2F8'
  },
  colors_label: {
    primary: '#ffde001f',
    secondary: '#8a8d931f',
    success: '#56ca001f',
    info: '#16b1ff1f',
    warning: '#ffb4001f',
    danger: '#ff4c511f',
    dark: '#4b4b4b1f'
  },
  colors_dark: {
    cardColor: '#312d4b',
    bodyBg: '#28243d',
    bodyColor: '#B0ACC7',
    headingColor: '#D5D1EA',
    textMuted: '#7A7692',
    borderColor: '#474360',
    chartBgColor: '#474360'
  },
  enableMenuLocalStorage: true // Enable menu state with local storage support
};

window.assetsPath = document.documentElement.getAttribute('data-assets-path');
window.templateName = document.documentElement.getAttribute('data-template');
window.rtlSupport = true; // set true for rtl support (rtl + ltr), false for ltr only.
