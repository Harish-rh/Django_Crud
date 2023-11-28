
document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        document.querySelectorAll(".alert").forEach(function(alert) {
            alert.style.display = "none";
        });
    }, 4000);
});

document.addEventListener("DOMContentLoaded", function () {
    var searchInput = document.getElementById("search");

    searchInput.addEventListener("keyup", function () {
        var value = this.value.toLowerCase();
        var tableRows = document.querySelectorAll("#mytable tr");

        tableRows.forEach(function (row) {
            var rowText = row.textContent.toLowerCase();
            row.style.display = rowText.indexOf(value) > -1 ? "" : "none";
        });
    });
});
