Meteor.methods({
    getLinkedArticles: function(from){
        var response = HTTP.get("http://52.2.161.209:8080/related?title=" + from, {});
        return response.data.linkedArticles;
    },
    getTargetArticle: function(from){
        var response = HTTP.get("http://52.2.161.209:8080/related?title=" + from, {});

        return expectedResponse.targetArticles[0];
    }
});