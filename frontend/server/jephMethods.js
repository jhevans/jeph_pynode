Meteor.methods({
    getLinkedArticles: function(pageid){
        var pageid = "12";
        var response = HTTP.get("http://52.2.161.209:8080/?article_id=" + pageid);



        var expectedResponse = JSON.parse(Assets.getText('jsonContract/getLinkedArticlesResponse.json'));

        return expectedResponse.targetArticles[0].linkedArticles;
    }
});