const { defineConfig } = require('@vue/cli-service')
module.exports = {
    transpileDependencies: ['@material/web'],
  chainWebpack: (config) => {
      config.module
          .rule('vue')
          .use('vue-loader')
          .tap((options) => ({
              ...options,
              compilerOptions: {
                  // treat any tag that starts with ion- as custom elements
                  isCustomElement: (tag) => tag.startsWith('md-')
              }
          }))

  },
  configureWebpack: {
    optimization: {
      minimize: false
    }
  },
  productionSourceMap: true,
  pwa:{
    name: 'WildEye',
    themeColor: '#4DBA87',
    msTileColor: '#000000',
    appleMobileWebAppCapable: 'yes',
    appleMobileWebAppStatusBarStyle: 'black',
    workboxPluginMode: 'GenerateSW',
    workboxOptions: {
      skipWaiting: true,
      clientsClaim: true,
    },
      iconPaths:{
          faviconSVG: 'favicon.svg',
          favicon32: 'favicon-32x32.png',
          favicon16: 'favicon-16x16.png',
          appleTouchIcon: 'apple-touch-icon.png',
          maskIcon: 'favicon.svg',
          msTileImage: 'android-chrome-512x512.png'
      },
      icons:[
          {
              "src": "android-chrome-192x192.png",
              "sizes": "192x192",
              "type": "image/png"
          },
          {
              "src": "android-chrome-512x512.png",
              "sizes": "512x512",
              "type": "image/png"
          },
          {
              "src": "android-chrome-192x192.png",
              "sizes": "192x192",
              "type": "image/png",
              "purpose": "maskable"
          },
          {
              "src": "android-chrome-512x512.png",
              "sizes": "512x512",
              "type": "image/png",
              "purpose": "maskable"
          }
      ]

  }
}