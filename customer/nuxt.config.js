
// module.exports = {
//   mode: 'universal',
//   /*
//   ** Headers of the page
//   */
//   head: {
//     title: process.env.npm_package_name || '',
//     meta: [
//       { charset: 'utf-8' },
//       { name: 'viewport', content: 'width=device-width, initial-scale=1' },
//       { hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
//     ],
//     link: [
//       { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
//     ]
//   },
//   /*
//   ** Customize the progress-bar color
//   */
//   loading: { color: '#fff' },
//   /*
//   ** Global CSS
//   */
//   css: [
//     'element-ui/lib/theme-chalk/index.css'
//   ],
//   /*
//   ** Plugins to load before mounting the App
//   */
//   plugins: [
//     '@/plugins/element-ui'
//   ],
//   /*
//   ** Nuxt.js modules
//   */
//   modules: [
//   ],
//   /*
//   ** Build configuration
//   */
//   build: {
//     transpile: [/^element-ui/],
//     /*
//     ** You can extend webpack config here
//     */
//     extend(config, ctx) {
//     }
//   }
// }




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
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  loading: { color: '#fff' },

  css: [
    'element-ui/lib/theme-chalk/index.css',
    '@/assets/css/app.css',
  ],

  plugins: [
    '@/plugins/element-ui'
  ],

  modules: [
    '@nuxtjs/axios',
    // '@nuxtjs/google-analytics',
  ],

  axios: {
    baseURL: "http://localhost:8000/api/"
  },

  build: {
    transpile: [/^element-ui/],
    extend(config, ctx) {
    }
  }
}
