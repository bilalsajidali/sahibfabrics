


function GetPrint()
{
    window.print()
}


function BtnAdd() {
    /*Add Button*/
    var v = $("#TRow").clone().appendTo("#TBody");
    $(v).find("input").val('');
    $(v).removeClass("d-none");
    $(v).find("th").first().html($('#TBody tr').length - 1);
}

function BtnDel(v) {
    /*Delete Button*/
    $(v).parent().parent().remove();
    GetTotal();

    $("#TBody").find("tr").each(
        function (index) {
            $(this).find("th").first().html(index);
        }

    );
}

function Calc(v) {
    /*Detail Calculation Each Row*/
    var index = $(v).parent().parent().index();

    var qty = document.getElementsByName("qty")[index].value;
    var rate = document.getElementsByName("rate")[index].value;

    var amt = qty * rate;
    document.getElementsByName("amt")[index].value = amt;

    GetTotal();
}

function GetTotal() {
    /*Footer Calculation*/

    var sum = 0;
    var amts = document.getElementsByName("amt");

    for (let index = 0; index < amts.length; index++) {
        var amt = amts[index].value;
        sum = +(sum) + +(amt);
    }

    document.getElementById("FTotal").value = sum;

    var gst = document.getElementById("FGST").value;
    var net = +(sum) + +(gst);
    document.getElementById("FNet").value = net;

}

// from there rate change in field
document.addEventListener('DOMContentLoaded', function () {
    var dropdown = document.getElementById('stockDropdown');
    var rateField = document.getElementsByName('rate')[0]; // Assuming there is only one rate field per row

    dropdown.addEventListener('change', function () {
        var selectedOption = dropdown.options[dropdown.selectedIndex];
        var rate = selectedOption.getAttribute('data-rate');

        console.log('Selected option:', selectedOption);
        console.log('Rate:', rate);

        // Update the rate field with the selected item's rate
        rateField.value = rate;

        console.log('Rate field:', rateField);
    });
});
