function isBlank(val) {
	return (val == null || val == "" || val == "None");
}

function addDropDownOptions($select, options) {
    $select.append("<option>" + options.join("</option><option>") + "</option>");
}

function updateTable(data) {
    $("#dataLoading").hide();
    if (data.length == 0) return;

    table = [];

    table.push("<tr><th>index</th>");

    _.each(Object.keys(data), function (key) {
        table.push("<th>" + key + "</th>");
    });

    table.push("</th>");

    // add all data in a row, one row at a time
    // use index to iterate through the row data

    _.each(data['index'], function (index) {
        table.push("<td>");
        _.each(Object.keys(data), function (key) {
            table.push("<td>" + data.key.index + "</td>");
            console.log("val: " + data.key.index);
        });
        table.push("</td>");
    });

    table.push("</tr>");

    console.table(data);
    console.log(data);

    $("#dataTableBody").html(table.join(""));
    $("#dataTable").show();
}