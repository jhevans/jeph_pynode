Template.wikiHop.events({
    "submit .registerForm": function (event) {
        // Prevent default browser form submit
        event.preventDefault();

        // Get value from form element
        var from = event.target.fromInput.value;
        // Insert a task into the collection
        Session.set('from', from);
        // Clear form

        Meteor.call("getLinkedArticles", [from], function(error, response){
            var linkedArticles = []

            for(r in response) {
                linkedArticles.push({'name':response[r]});
            }

            Session.set('linkedArticles', linkedArticles);
        });
    }

});

Template.wikiHop.helpers({
    from: function(){
        return Session.get('from');
    },
    linkedArticles: function(){
        return Session.get('linkedArticles');
    }
});