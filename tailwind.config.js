/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.{html,js}',  // Specify the paths to all of your template files
  ],
  theme: {
    extend: {
      colors: {
        primary: '#1DA1F2',  // Add a custom color
        secondary: '#14171A',
      },
      spacing: {
        '72': '18rem',  // Add a custom spacing value
        '84': '21rem',
        '96': '24rem',
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],  // Customize the default font
      },
    },
  },
  plugins: [],
}
