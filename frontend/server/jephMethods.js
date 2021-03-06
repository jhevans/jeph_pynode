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
        console.log(from);
        console.log(to);
        var url = "http://52.2.161.209:8080/related?limit=4&title=" + from + "&destinationTitle=" + to;
        console.log(url);
        var response = HTTP.get(url, {});
        return response.data.articles;
    },
    getLinkedArticlesBasedOnTwoPointsWithLimit: function(from, to, limit){
        var response = HTTP.get("http://52.2.161.209:8080/specificPath?title=" + from +
            "&destinationTitle=" + to + "&limit=" + limit, {});
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