/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './utileria/static/utileria/src/**/*.css',
    './utileria/static/utileria/src/**/*.html',
    './utileria/static/utileria/src/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("daisyui"),
  ],
  daisyui: {
    styled: false,
    themes: false,
    base: true,
    utils: true,
    logs: true,
    rtl: false,
    prefix: "",
    darkTheme: "dark",
  },
}
