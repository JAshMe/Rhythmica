/**
 Author: JAshMe
 CSE, MNNIT Allahabad
 */

$('input[type="file"]').change(function (e) {
            var fileName = e.target.files[0].name;
            $(this).siblings("label").html(fileName);
        });