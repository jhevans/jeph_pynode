Template.explore.onRendered(function(){
    var width = 640*1.5,
        height = 480*1.5;

    var nodes = [
        { x: width/2, y: height/2 },
        { },
        { },
        { },
        { },
        { },
        { },
        { },
        { }
    ];

    var links = [
        { source: 0, target: 1 },
        { source: 0, target: 2 },
        { source: 0, target: 3 },
        { source: 0, target: 4 },
        { source: 0, target: 5 },
        { source: 0, target: 6 },
        { source: 0, target: 7 },
        { source: 0, target: 8 }
    ];

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

    force.on('end', function() {

        node.attr('r', width/25)
            .attr('cx', function(d) { return d.x; })
            .attr('cy', function(d) { return d.y; });

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