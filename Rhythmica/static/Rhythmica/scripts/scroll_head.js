/**
 Author: JAshMe
 CSE, MNNIT Allahabad
 */

$(window).scroll(function () {
        //console.log($(window).scrollTop());
        if($(window).scrollTop() > 200)
        {
            $("#off-div").removeClass('offset-md-3');
            $("#btn-col").removeClass('col-md-4').addClass('col-md-7');
            $(".main-btn").removeClass('offset-md-2').removeClass('col-md-8').addClass('col-md-5');
            $("#signup-btn").removeClass('signup-ini-btn').addClass('offset-md-1');
            $("#head").addClass('small-head');
            $("#sub-head").addClass('small-subhead');
            $("#logo").addClass('small-logo');
            $("#head-container").removeClass('col-md-9').addClass('col-md-6');

        }
        else
        {
            $("#off-div").addClass('offset-md-3');
            $("#btn-col").addClass('col-md-4').removeClass('col-md-7');
            $(".main-btn").addClass('offset-md-2').addClass('col-md-8').removeClass('col-md-5');
            $("#signup-btn").addClass('signup-ini-btn').removeClass('offset-md-1');
            $("#head").removeClass('small-head');
            $("#sub-head").removeClass('small-subhead');
            $("#logo").removeClass('small-logo');
            $("#head-container").addClass('col-md-9').removeClass('col-md-6');
        }
    });