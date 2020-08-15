$(document).ready(function() {
    $.get("/wrds-data-model/get_libraries/", function (data, success) {
        addDropDownOptions($("#library"), JSON.parse(data));
    });

    $("#library").on("change", function () {
        $.get("/wrds-data-model/get_tables/" + $("#library").val(), function (data, success) {
            $("#table").val("");
            addDropDownOptions($("#table"), JSON.parse(data));
        });
    });

    $("#table").on("change", function () {
        $("#dataLoading").show();
        $.get("/wrds-data-model/get_table_data?library=" + $("#library").val() + "&table="
                + $("#table").val(), function (data, success) {
            updateTable(JSON.parse(data));
        });
    });

    $("#submit").on("click", function () {
        $.get("/wrds-data-model/get_table_Data/" + $("#query-input").val(), function (data, success) {
            updateTable(JSON.parse(data));
        });
    });
    
});

