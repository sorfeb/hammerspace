/** @type {import('tailwindcss').Config} */
module.exports = {
  prefix: 'tw-',
  content: ['./main/templates/**/*.{html,js}'],
  theme: {
    extend: {
      fontFamily: {
        'seagram': ['SEAGRAM']
      }
    },
  },
  plugins: [],
}

