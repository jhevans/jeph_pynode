var width = 640*1,
    height = 480*1;

var xCentre = width/2;
var yCentre = height/2;

var force;


var nodes;
var links;

function update(articleName){
    console.log(articleName);

    Meteor.call("getTargetArticle", [articleName], function(error, targetArticle){
        var linkedArticles = targetArticle.linkedArticles;


        nodes = getNodes(targetArticle, linkedArticles);
        var newThing = {
            name: "fooo"
        };
        nodes.push(newThing);
        links = getLinks(linkedArticles);
        links.push({
            source:0,
            target: newThing
        });

        console.log(nodes);
        console.log(links);
        //force
        //    .nodes(nodes)
        //    .links(links);

        render(nodes, links);
        //force.start();

    });
}



function render(nodes, links) {

    var svg = d3.select('.canvasContainer')
        .attr('width', width)
        .attr('height', height);

    force = d3.layout.force()
        .size([width, height])
        .nodes(nodes)
        .links(links);

    force.linkDistance(width / 6);
    force.charge(-1000);

    var link = svg.selectAll('.link')
        .data(links)
        .enter().append('line')
        .attr('class', 'link');


    var nodeEnter = svg.selectAll(".nodeText")
        .data(nodes)
        .enter();

    var nodeCircle = nodeEnter.append('circle')
        .on('click', function(d){
            d.x = xCentre;
            d.y = yCentre;
            update(d.name);
        })
        .attr('class', 'nodeCircle');

    var nodeText = nodeEnter.append("a")
        .attr("xlink:href", function(d){return d.url;})
        .append('text')
        .attr("dx", function (d) {
            return -30;
        })
        .text(function (d) {
            console.log(d.name)
            return d.name
        })
        .attr('class', 'nodeText');

    force.on('tick', function () {

        nodeCircle.attr('r', width / 25)
            .attr('cx', function (d) {
                return d.x;
            })
            .attr('cy', function (d) {
                return d.y;
            });

        nodeText
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

        link
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
Template.explore.onRendered(function(){
    Meteor.call("getTargetArticle", [], function(error, targetArticle){
        var linkedArticles = targetArticle.linkedArticles;
        nodes = getNodes(targetArticle, linkedArticles)
        links = getLinks(linkedArticles)
        render(nodes, links);
    });
});

function getNodes(targetArticle, linkedArticles){
    var nodes = [];
    nodes.push(targetArticle);

    linkedArticles.forEach(function(article){
        nodes.push(article);
    })

    nodes.forEach(function(article){
        article.url = "https://en.wikipedia.org/wiki/Tom_Hanks";
    })
    return nodes;
};

function getLinks(linkedArticles){
    var links = [];
    linkedArticles.forEach(function(value){
        links.push({source:0, target: value})
    });

    return links;
}