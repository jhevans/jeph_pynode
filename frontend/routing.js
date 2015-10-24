Router.configure({
    layoutTemplate: 'main'
});

Router.route('/', {
    template: 'routeSearch'
});

Router.route('/about', function () {
    this.render('about');
});

Router.route('/register', function () {
    this.render('register');
});

