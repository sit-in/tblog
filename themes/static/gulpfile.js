//livereload
var gulp = require('gulp'),
    less = require('gulp-less'),
    livereload = require('gulp-livereload');

gulp.task('default', function() {
  livereload.listen();
  gulp.watch(['../static/app/**', '../templates/**', '../../mongo_admin/**', '../../ui/**']).on('change', livereload.changed);
});
