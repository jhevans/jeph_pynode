Meteor.methods({
    getWikiArticleByPageid: function(pageid){
        var url = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&pageids=";
        var response = HTTP.get(url + pageid, {});
        return JSON.parse(response.content).query.pages[pageid];
    }
});