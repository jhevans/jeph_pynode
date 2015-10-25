var count= 0

Template.linkedArticle.helpers({
    wikiArticle: function(){
        count++;
        console.log("count = " + count)
        return Session.get('wikiArticle' + this.pageid);
    }
});

Template.linkedArticle.onCreated(function(){
    var pageId = this.data.pageid;

    Meteor.call("getWikiArticleByPageid", [pageId], function(error, response){
        Session.set('wikiArticle'+ pageId, response);
    });
})
