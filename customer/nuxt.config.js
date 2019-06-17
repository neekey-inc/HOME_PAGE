const pkg = require('./package')


module.exports = {
  mode: 'universal',

  head: {
    title: 'Neekey.inc【ホームページ】',
    meta: [
      { charset: 'utf-8' },
      { name: 'keywords', content: 'Neekey' },
      { name: 'description', content: 'Neekey.inc【ホームページ】' },
      { name: 'copyright', content: '©Neekey.inc 2019 allright reserved. 無断転載禁止' },
      { name: 'mobile-web-app-capable', content: 'yes' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {
        rel: 'stylesheet',
        href: 'https://use.fontawesome.com/releases/v5.6.1/css/all.css',
        integrity: 'sha384-gfdkjb5BdAXd+lj+gudLWI+BXq4IuLW5IT+brZEZsLFm++aCMlF1V92rMkPaX4PP',
        crossorigin: 'anonymous'
      }
    ]
  },

  loading: { color: '#fff' },

  css: [
    'element-ui/lib/theme-chalk/index.css',
    '@/assets/css/app.css',
  ],

  plugins: [
    '@/plugins/element-ui',
  ],

  modules: [
    '@nuxtjs/axios',
    'nuxt-fontawesome'
    // '@nuxtjs/google-analytics',
  ],

  fontawesome: {
    imports: [
      {
        set: '@fortawesome/free-solid-svg-icons',
        icons: ['fas']
      }
    ]
  },

  axios: {
    baseURL: "http://localhost:8000/api/"
  },

  build: {
    transpile: [/^element-ui/],
    extend(config, ctx) {
    }
  }
}
