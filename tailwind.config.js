/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './templates/**/*.html',
        './templates/**/*.j2',
    ],
    theme: {
        extend: {
            colors: {
                'custom-background': '#33292B',
                'custom-default-text': '#EEB3B9',
                'custom-primary-accent': '#BE3C56',
                'custom-primary-accent-darker': '#862c40',
                'custom-secondary-accent': '#7691FF',
                'custom-tertiary-accent': '#FFA16C',
            },
            fontFamily: {
              'sans': ['adobe-gothic-std', 'sans-serif'],

            },
        },
    },
    plugins: [],
}

