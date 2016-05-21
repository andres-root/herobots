'use-strict';

/**
 * Global Gulp variables
 */
module.exports = {
  paths: {
    //Sources
    src: './src/',
    //Cache
    sassCache: './.sass-cache/',
    //Javascript
    mainJSFile: './src/js/Main.js',
    srcJS: './src/js/**/*',
    srcJSComponents: './src/js/components/',
    //Styles
    srcSASSFile: './src/styles/sass/main.scss',
    srcSASS: './src/styles/sass/',
    //Destinations
    dist: './dist/',
    distJS: './dist/js/',
    distCSS: './dist/css/'
  },
  extensions: {
    js: '*.js',
    css: '*.{css,map}',
    sass: '*.{sass,scss}',
  },
  gjslint: {
    flags: [
      '--max_line_length 125'
    ]
  }
};
