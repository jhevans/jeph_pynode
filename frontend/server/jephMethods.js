Meteor.methods({
    getLinkedArticles: function(from){
        var response = HTTP.get("http://52.2.161.209:8080/related?title=" + from, {});
        return response.data.linkedArticles;
    },
    getRandomArticle: function(){
        var response = HTTP.get("http://52.2.161.209:8080/randomTitle", {});

        return response.data.name;
    }
});