'use-strict';

/**
 * Global Gulp variables
 */
module.exports = {
  paths: {
    //Sources
    src: './frontend_src/',
    //Cache
    sassCache: './.sass-cache/',
    //Javascript
    mainJSFile: './frontend_src/js/Main.js',
    srcJS: './frontend_src/js/**/*',
    srcJSComponents: './frontend_src/js/components/',
    //Styles
    srcSASSFile: './frontend_src/styles/sass/main.scss',
    srcSASS: './frontend_src/styles/sass/',
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
