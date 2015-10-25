Router.configure({
    layoutTemplate: 'main'
});

Router.route('/', {
    template: 'routeSearch'
});

Router.route('/about', function () {
    this.render('about');
});

Router.route('/wikiHop', function () {
    this.render('explore');
});


Router.route('/explore', function () {
    this.render('wikiHop');
});

