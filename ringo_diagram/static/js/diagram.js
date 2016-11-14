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
}
