Template.wikiHop.events({
    "submit .wikiHopForm": function (event) {
        Session.set('linkedArticles', null);
        // Prevent default browser form submit
        event.preventDefault();

        // Get value from form element
        var from = event.target.fromInput.value;
        var to = event.target.toInput.value;
        var checkbox = event.target.shortestCheckbox.checked;
        var limit = event.target.limitInput.value;
        // Insert a task into the collection.va
        Session.set('from', from);
        // Clear form
        if(from && to && checkbox){
            Meteor.call("getLinkedArticlesShortestPath", [from], [to], function (error, response) {
                var linkedArticles = []

                for (r in response) {
                    linkedArticles.push({'name': response[r]});
                }
                Session.set('linkedArticles', linkedArticles);
            });
         } else if(from && to && limit) {
            Meteor.call("getLinkedArticlesBasedOnTwoPointsWithLimit", [from], [to], [limit], function (error, response) {
                var linkedArticles = []

                for (r in response) {
                    linkedArticles.push({'name': response[r]});
                }
                Session.set('linkedArticles', linkedArticles);
            });
        } else if(from && to) {
            Meteor.call("getLinkedArticlesBasedOnTwoPointsWithLimit", [from], [to], [10], function (error, response) {
                var linkedArticles = []

                for (r in response) {
                    linkedArticles.push({'name': response[r]});
                }
                Session.set('linkedArticles', linkedArticles);
            });
        } else if(from && !to) {
            Meteor.call("getLinkedArticles", [from], function(error, response){
                var linkedArticles = []

                for(r in response) {
                    linkedArticles.push({'name':response[r]});
                }
                Session.set('linkedArticles', linkedArticles);
            });
        } else {

        }

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