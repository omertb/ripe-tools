$(document).ready(function () {
    $("a").tooltip({container:'body'});
});

let $pathResultTable = $('#pathResultTable');
let resultArea = document.getElementById("resultArea")
let formErrorArea = document.getElementById("formErrorArea")

$(document).on("submit", "#asOrNetsubmitForm", function(event){
    event.preventDefault();
    $pathResultTable.bootstrapTable("destroy");
    let asOrIpNet = $pathResultTable.val();
    //var csrftoken = $('meta[name=csrf-token]').attr('content');
    $.ajax(
        {
            url: "/",
            type: "POST",
            data: new FormData(this),
            dataType: "json",
            contentType: false,
            cache: false,
            processData: false,
            //beforeSend: function(xhr, settings) {
            //    if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
            //        xhr.setRequestHeader("X-CSRFToken", csrftoken)
            //    }
            //},
            success: function(data) {
                // resultArea.innerHTML = JSON.stringify(data);
                formErrorArea.innerHTML = "";
                $pathResultTable.bootstrapTable({data: data});
                $("a").tooltip({container:'body'});

            },
            error: function(data) {
                console.log("ERROR:");
                console.log(data);
                formErrorArea.innerHTML = data.responseText;
            }
        }
    );
});

$('#pathResultTable').on('all.bs.table', function(){
    $("a").tooltip({container:'body'});
});