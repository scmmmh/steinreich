var gulp = require('gulp'),
    sass = require('gulp-sass'),
    autoprefixer = require('gulp-autoprefixer'),
    concat = require('gulp-concat'),
    cleanCSS = require('gulp-clean-css'),
    pump = require('pump');

gulp.task('css', function(cb) {
    pump([
        gulp.src([
            'theme/src/theme.scss',
            'theme/src/fonts.scss',
        ]),
        sass({
            includePaths: [
                'node_modules/foundation-sites/scss',
                'node_modules/motion-ui/src'
            ]
        }),
        autoprefixer({
            cascade: false
        }),
        cleanCSS(),
        gulp.dest('theme/static/css')
    ], cb);
});

gulp.task('js', function(cb) {
    pump([
        gulp.src([
            'node_modules/jquery/dist/jquery.min.js',
            'node_modules/what-input/dist/what-input.min.js',
            'node_modules/foundation-sites/dist/js/foundation.min.js',
            'node_modules/femtotween//dist/femtoTween.umd.js'
        ]),
        concat('scripts.js'),
        gulp.dest('theme/static/js')
    ], cb);
});

gulp.task('default', gulp.series('css', 'js'));

gulp.task('watch', gulp.series('default', function(cb) {
    gulp.watch('theme/src/**/*.scss', gulp.series('css'));
    cb();
}))
