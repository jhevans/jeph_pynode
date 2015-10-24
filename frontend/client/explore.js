Template.explore.onCreated(function() {
    getTargetArticle();
});

Template.explore.onRendered(function(){
    var width = 640*1.5,
        height = 480*1.5;



    var nodes = getNodes();

    var links = getLinks();

    var svg = d3.select('.canvasContainer').append('svg')
        .attr('width', width)
        .attr('height', height);

    var force = d3.layout.force()
        .size([width, height])
        .nodes(nodes)
        .links(links);

    force.linkDistance(width/6);
    force.charge(-10000);

    var link = svg.selectAll('.link')
        .data(links)
        .enter().append('line')
        .attr('class', 'link');

    var node = svg.selectAll('.node')
        .data(nodes)
        .enter().append('circle')
        .attr('class', 'node');

    var nodeText = svg.selectAll(".nodeText")
        .data(nodes)
        .enter().append('text')
        .attr("dx", function(d){return -30})
        .text(function(d){return d.name})
        .attr('class', 'nodeText');

    force.on('end', function() {

        node.attr('r', width/25)
            .attr('cx', function(d) { return d.x; })
            .attr('cy', function(d) { return d.y; });

        nodeText
            .attr('x', function(d) { return d.x; })
            .attr('y', function(d) { return d.y; });

        // We also need to update positions of the links.
        // For those elements, the force layout sets the
        // `source` and `target` properties, specifying
        // `x` and `y` values in each case.

        link.attr('x1', function(d) { return d.source.x; })
            .attr('y1', function(d) { return d.source.y; })
            .attr('x2', function(d) { return d.target.x; })
            .attr('y2', function(d) { return d.target.y; });

    });


    force.start();

});

function getTargetArticle(){
    Meteor.call("getRoute", [], function(error, response){
        console.log(response.targetArticles[0])
        Session.set("targetArticle", response.targetArticles[0]);
    });
}

function getNodes(){
    var nodes = [];
    debugger;
    var targetArticle = Session.get("targetArticle");
    nodes.push(targetArticle);
    targetArticle.linkedArticles.forEach(function(article){
        nodes.push(article);
    })
    return nodes;
};

function getLinks(){
    var links = [];
    getNodes().forEach(function(value, index){
        links.push({source:0, target: index})
    });

    links.shift();
    return links;
}