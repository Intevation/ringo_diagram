// Used to synchronize the diagrams
var diagram_syncs = [];

function renderDiagram(id, data, title, xlabel, ylabel, fieldname, errorBars) {
  g = new Dygraph(document.getElementById(id), data, {
    legend: 'always',
    title: title,
    strokeWidth: 1,
    highlightCircleSize: 5,
    xlabel: xlabel,
    ylabel: ylabel,
    labelsDiv: fieldname+'_legend',
    labelsSeparateLines: true,
    errorBars: errorBars
  });
  return g;
}

// Actually sync the diagrams.
$( document ).ready(function() {
    Dygraph.synchronize(diagram_syncs, {selection: true, zoom: false});
});
