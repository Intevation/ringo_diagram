// Used to synchronize the diagrams
var diagram_syncs = [];

function renderDiagram(id, data, title, xlabel, ylabel, fieldname, errorBars, legend, hlcb, uhlcb) {
  if (legend === true) {
      legend = fieldname+'_legend'
  } else {
      legend = null
  }
  g = new Dygraph(document.getElementById(id), data, {
    legend: 'always',
    title: title,
    strokeWidth: 1,
    highlightCircleSize: 5,
    axisLabelFontSize: 11,
    xlabel: xlabel,
    ylabel: ylabel,
    labelsDiv: legend,
    labelsSeparateLines: true,
    errorBars: errorBars,
    highlightCallback: hlcb,
    unhighlightCallback: uhlcb
  });
  return g;
}

// Actually sync the diagrams.
$( document ).ready(function() {
    if (diagram_syncs.length > 0) {
        Dygraph.synchronize(diagram_syncs, {selection: true, zoom: false});
    }
});
