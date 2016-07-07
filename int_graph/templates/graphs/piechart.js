function pieChart(data_input, element, title) {
    var data = google.visualization.arrayToDataTable(data_input);

    var options = {
        title: title,
    };

    var chart = new google.visualization.PieChart(element);
    chart.draw(data, options);
}

