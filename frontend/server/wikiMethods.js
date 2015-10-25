Meteor.methods({
    getWikiArticleByPageid: function(pageid){
        var url = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&pageids=";
        var response = HTTP.get(url + pageid, {});
        return JSON.parse(response.content).query.pages[pageid];
    },

    getWikiArticleByTitle: function(title){
        var url = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=";
        var response = HTTP.get(url + encodeURIComponent(title), {});
        var parsedResponse = JSON.parse(response.content).query.pages;

        var firstKey;
        for (key in parsedResponse) {
            firstKey = key
        }

        return parsedResponse[firstKey];
    }
});