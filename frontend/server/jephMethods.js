Meteor.methods({
    getLinkedArticles: function(from){
        var response = HTTP.get("http://52.2.161.209:8080/related?title=" + from, {});
        return response.data.linkedArticles;
    },
    getRandomArticle: function(){
        var response = HTTP.get("http://52.2.161.209:8080/randomTitle", {});

        return response.data.name;
    },
    getLinkedArticlesBasedOnTwoPoints: function(from, to){
        var response = HTTP.get("http://52.2.161.209:8080/related?title=" + from + "&destinationTitle=" + to, {});
        return response.data.linkedArticles;
    },
    getLinkedArticlesShortestPath: function(from, to){
        var response = HTTP.get("http://52.2.161.209:8080/shortestPath?fromTitle=" + from + "&destinationTitle=" + to, {});
        return response.data.linkedArticles;
    },
    getTargetArticle: function(from){
        var response = HTTP.get("http://52.2.161.209:8080/related?title=" + from, {});

        return response.data.name;
    }
});