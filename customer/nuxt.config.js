const pkg = require('./package')


module.exports = {
  mode: 'universal',

  head: {
    title: '株式会社Neekey',
    meta: [
      { charset: 'utf-8' },
      { name: 'keywords', content: 'Neekey' },
      { name: 'description', content: '株式会社Neekeyは「今ここにない未来を自分で作る」をビジョンに掲げ、代行業を一括で比較できるサイト「代行エンジン」の運営やAIの研究、Web・アプリの受託開発を展開しています。インターネット産業の変化に合わせ新規事業を生み出しながら事業拡大をしていきます。' },
      { name: 'copyright', content: '©Neekey.inc 2019 allright reserved.' },
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
