module.exports = {
    css: {
        loaderOptions: {
            sass: {
                prependData: '@import "@/sass/style.scss";'
            }
        }
    },
    chainWebpack: config => {
        config.module.rules.delete('eslint');
    }
}