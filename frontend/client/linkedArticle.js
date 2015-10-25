Template.linkedArticle.helpers({
    wikiArticle: function(){
        return Session.get('wikiArticle' + this.name);
    }
});

Template.linkedArticle.onCreated(function(){
    var title = this.data.name;

    Meteor.call("getWikiArticleByTitle", [title], function(error, response){
        Session.set('wikiArticle'+ title, response);
    });
})
