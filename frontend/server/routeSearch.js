Meteor.methods({
    getRoute: function(from, to){
        console.log("getRoute");
        var response = HTTP.get("http://randomword.setgetgo.com/get.php", {

        });

        console.log(response.content);
        console.log(typeof response.content);
        return response.content;
    }
});