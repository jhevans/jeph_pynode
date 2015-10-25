var width = 640*1.5,
    height = 480*1.5;

function render(nodes, links) {

    var svg = d3.select('.canvasContainer').append('svg')
        .attr('width', width)
        .attr('height', height);

    var force = d3.layout.force()
        .size([width, height])
        .nodes(nodes)
        .links(links);

    force.linkDistance(width / 6);
    force.charge(-10000);

    var link = svg.selectAll('.link')
        .data(links)
        .enter().append('line')
        .attr('class', 'link');


    var nodeEnter = svg.selectAll(".nodeText")
        .data(nodes)
        .enter();

    var nodeCircle = nodeEnter.append('circle')
        .attr('class', 'nodeCircle');

    var nodeText = nodeEnter.append("a")
        .attr("xlink:href", function(d){return d.url;})
        .append('text')
        .attr("dx", function (d) {
            return -30
        })
        .text(function (d) {
            return d.name
        })
        .attr('class', 'nodeText');

    //var nodeLink = nodeEnter;

    force.on('end', function () {

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

        //nodeLink
        //    .attr('x', function (d) {
        //        return d.x;
        //    })
        //    .attr('y', function (d) {
        //        return d.y;
        //    })
        //    .attr('height', function (d) {
        //        return 100;
        //    })
        //    .attr('width', function (d) {
        //        return 100;
        //    });

        // We also need to update positions of the links.
        // For those elements, the force layout sets the
        // `source` and `target` properties, specifying
        // `x` and `y` values in each case.

        link.attr('x1', function (d) {
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
        var nodes = getNodes(targetArticle, linkedArticles)
        var links = getLinks(linkedArticles)
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
    linkedArticles.forEach(function(value, index){
        links.push({source:0, target: index+1})
    });

    return links;
}