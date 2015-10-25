Meteor.methods({
    getLinkedArticles: function(from){
        var response = HTTP.get("http://52.2.161.209:8080/related?title=" + from, {});
        return response.data.articles;
    },
    getRandomArticle: function(){
        var response = HTTP.get("http://52.2.161.209:8080/randomTitle", {});

        return response.data.name;
    },
    getLinkedArticlesBasedOnTwoPoints: function(from, to){
        var response = HTTP.get("http://52.2.161.209:8080/related?title=" + from + "&destinationTitle=" + to, {});
        return response.data.articles;
    },
    getLinkedArticlesShortestPath: function(from, to){
        var response = HTTP.get("http://52.2.161.209:8080/shortestPath?title=" + from + "&destinationTitle=" + to, {});
        return response.data.articles;
    },
    getRelatedRandomArticles: function(){
        var response = HTTP.get("http://52.2.161.209:8080/randomTitles", {});
        return response.data;
    },
    getTargetArticle: function(from){
        var response = HTTP.get("http://52.2.161.209:8080/related?title=" + from, {});

        return response.data.name;
    }
});