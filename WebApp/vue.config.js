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
    }
  }
}