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
				brown: {
					DEFAULT : 'rgb(223,190,125)',
					100: 'rgba(223,190,125,.1)',
					200: 'rgba(223,190,125,.2)',
					300: 'rgba(223,190,125,.3)',
					400: 'rgba(223,190,125,.4)',
					500: 'rgba(223,190,125,.5)',
					600: 'rgba(223,190,125,.6)',
					700: 'rgba(223,190,125,.7)',
					800: 'rgba(223,190,125,.8)',
					900: 'rgba(223,190,125,.9)'
				}
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
