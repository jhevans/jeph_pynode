

Template.linkedArticle.helpers({
    wikiArticle: function(){
        return Session.get('wikiArticle');
    }
});

Template.linkedArticle.onCreated(function(){
    Meteor.call("getWikiArticleByPageid", [this.pageid], function(error, response){
        Session.set('wikiArticle', response);
    });
})