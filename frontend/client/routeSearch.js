
Template.routeSearch.events({
    "submit .routeSearchForm": function (event) {
        // Prevent default browser form submit
        event.preventDefault();

        // Get value from form element
        var from = event.target.fromInput.value;
        var to = event.target.toInput.value;

        // Insert a task into the collection
        Session.set('from', from);
        Session.set('to', to);
        // Clear form

        Meteor.call("getLinkedArticles", [], function(error, response){
            debugger;
            Session.set('linkedArticles', response);
        });
    }
});


Template.routeSearch.helpers({
    from: function(){
        return Session.get('from');
    },
    to: function(){
        return Session.get('to');

    },
    linkedArticles: function(){
        return Session.get('linkedArticles');
    }
});
