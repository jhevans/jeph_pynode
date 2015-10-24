Meteor.methods({
    getWikiArticleByPageid: function(pageid){


        var expectedResponse = JSON.parse(Assets.getText('wikiResponses/getArticleByPageid.json'));

        return expectedResponse;
    }
});