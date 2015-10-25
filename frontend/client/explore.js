var width = 640*1.5,
    height = 480*1.5;

var xCentre = width/2;
var yCentre = height/2;

var force;

var nodes;
var links;
var svg;

function update(nextArticle){

    Meteor.call("getLinkedArticles", [nextArticle], function(error, linkedArticles){
        renderArticleLinks(nextArticle);
    });
}


//function render(nodes, links) {
function render() {

    svg = d3.select('.canvasContainer')
        .attr('width', width)
        .attr('height', height);

    force = d3.layout.force()
        .size([width, height])
        .nodes(nodes)
        .links(links);

    force.linkDistance(width / 6);
    force.charge(-1000);

    var linkGroup = svg.selectAll('.link');
    var link = linkGroup
        .data(links, name)
        .enter().append('line')
        .attr('class', 'link');

    linkGroup
        .data(links, name)
        .exit().remove();

    var nodeCircleGroup = svg.selectAll(".nodeCircle");
    var nodeEnter = nodeCircleGroup
        .data(nodes, name)
        .enter();

    nodeCircleGroup
        .data(nodes, name)
        .exit().remove();

    var nodeCircle = nodeEnter.append('circle')
        .on('click', function(d){
            //d.x = xCentre;
            //d.y = yCentre;
            update(d.name);
        })
        .attr('class', 'nodeCircle');

    var nodeHyperlinkGroup = svg.selectAll(".nodeHyperlink");
    var nodeText = nodeHyperlinkGroup
        .data(nodes, name)
        .enter()
        .append("a")
        .attr("xlink:href", function(d){return d.url;});

    nodeHyperlinkGroup
        .data(nodes, name)
        .exit().remove();

    var nodeTextGroup = svg.selectAll(".nodeText");

    nodeTextGroup
        .data(nodes, name)
        .enter()
        .append('text')
        .attr("dx", function (d) {
            return -30;
        })
        .text(function (d) {
            console.log(d.name);
            return d.name;
        })
        .attr('class', 'nodeText');

    nodeTextGroup
        .data(nodes, name)
        .exit().remove();

    nodeTextGroup
        .data(nodes, name)
        .text(function (d) {
            console.log(d.name);
            return d.name;
        });

    force.on('tick', function () {

        svg.selectAll(".nodeCircle")
            .attr('r', width / 25)
            .attr('cx', function (d) {
                return d.x;
            })
            .attr('cy', function (d) {
                return d.y;
            });

        svg.selectAll(".nodeText")
            .attr('x', function (d) {
                return d.x;
            })
            .attr('y', function (d) {
                return d.y;
            });

        // We also need to update positions of the links.
        // For those elements, the force layout sets the
        // `source` and `target` properties, specifying
        // `x` and `y` values in each case.

        svg.selectAll(".link")
            .attr('x1', function (d) {
                return d.source.x;
            })
            .attr('y1', function (d) {
                return d.source.y;
            })
            .attr('x2', function (d) {
                return d.target.x;
            })
            .attr('y2', function (d) {
                return d.target.y;
            });

    });


    force.start();
}
function renderArticleLinks(articleName) {
    Meteor.call("getLinkedArticles", [articleName], function (error, linkedArticles) {

        var linkedArticleObjects = [];

        linkedArticles.forEach(function (articleName) {
            linkedArticleObjects.push({
                name: articleName
            })
        })
        var targetArticle = {
            name: articleName
        };
        nodes = getNodes(targetArticle, linkedArticleObjects)
        links = getLinks(targetArticle, linkedArticleObjects)
        render(nodes, links);
        addToHistory(articleName);
    })
}
function getNodes(targetArticle, linkedArticles){
    nodes = [];
    nodes.push(targetArticle);

    linkedArticles.forEach(function(article){
        nodes.push(article);
    })

    nodes.forEach(function(article){
        article.url = "https://en.wikipedia.org/wiki/" + article.name;
    })
    return nodes;
};

function getLinks(targetArticle, linkedArticles){
    links = [];
    linkedArticles.forEach(function(value){
        links.push({source:targetArticle, target: value})
    });

    return links;
}

function addToHistory(articleName){
    var history = Session.get('history');
    if(!history){
        history = [];
    }

    history.push({name:articleName});

    Session.set('history', history);
}

Template.explore.onRendered(function(){

    Meteor.call("getRelatedRandomArticles", [], function(error, response){
        var sourceArticle = response.title1;
        var targetArticle = response.title2;
        Session.set('target', targetArticle);
        Session.set('pathLength', response.pathLength);
        renderArticleLinks(sourceArticle);
    });
});


Template.explore.helpers({
    historyItems: function(){
        return Session.get('history');
    },
    target: function(){
        return Session.get('target');
    },
    pathLength: function(){
        return Session.get('pathLength');
    }
});

