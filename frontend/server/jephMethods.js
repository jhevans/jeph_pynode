Meteor.methods({
    getLinkedArticles: function(pageid){
        var pageid = "12";
        var response = HTTP.get("http://52.2.161.209:8080/?article_id=" + pageid);


        //var expectedResponse = JSON.parse(Assets.getText('jsonContract/getLinkedArticlesResponse.json'));
        var expectedResponse = {
            "targetArticles": [
                {
                    "pageid": "43568",
                    "name": "Tom_Hanks",
                    "linkedArticles": [
                        {
                            "pageid": "41528",
                            "name": "Forrest_Gump"
                        },
                        {
                            "pageid": "946164",
                            "name": "The_Green_Mile_(film)"
                        }
                    ]
                }
            ]
        };

        return expectedResponse.targetArticles[0].linkedArticles;
    },
    getTargetArticle: function(){
        var pageid = "12";
        //var response = HTTP.get("http://52.2.161.209:8080/?article_id=" + pageid);


        //var expectedResponse = JSON.parse(Assets.getText('jsonContract/getLinkedArticlesResponse.json'));
        var expectedResponse = {
            "targetArticles": [
                {
                    "pageid": "43568",
                    "name": "Tom_Hanks",
                    "linkedArticles": [
                        {
                            "pageid": "41528",
                            "name": "Forrest_Gump"
                        },
                        {
                            "pageid": "946164",
                            "name": "The_Green_Mile_(film)"
                        }
                    ]
                }
            ]
        };

        return expectedResponse.targetArticles[0];
    }
});