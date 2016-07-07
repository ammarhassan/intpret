function pieChart(data_input, id, title) {
    var data = google.visualization.arrayToDataTable(data_input);

    var options = {
        title: title,
    };

    var chart = new google.visualization.PieChart(document.getElementById(id));
    chart.draw(data, options);
}