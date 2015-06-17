function getCookie(name) {
  var matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

function randWDn(n){
  var s ='';
  while(s.length < n)
    s += Math.random().toString(36).slice(2, 12);
  return s.substr(0, n);
}

$(document).ready(function(){

    $("#top_count_cart").load("/cart/get_count_cart/");

    //$(".img-block img").each(function(){
    //    $(this).load(function(){
    //        var width = $(this).width();
    //        var left = (width - 233) / 2;
    //        $(this).animate({'left': (-1 * left) + "px"}, 200);
    //    });
    //});

    if ($("a").is(".product_image"))
    {

        $('.product_image').fancybox({
            prevEffect : 'none',
            nextEffect : 'none',

            closeBtn  : false,
            arrows    : false,
            nextClick : true,

            helpers : {
                thumbs : {
                    width  : 50,
                    height : 50
                }
            }
        });

        $(".product_image_head").click(function(){
            $(".prev_head").click();
        });

    }

    $(document).on('click', '.login_show', function(){
        $("#popup_box").remove();
        $("body").append('<div id="popup_box" style="display:none"></div>');
        $("#popup_box").load("/login/", function(){
            $(document).on('click', '.login', function(){
                $.get("/login/",
                    {
                        'email': $("#email").val(),
                        'password': $("#password").val()
                    },
                    function(data){
                        if(data === 'true'){
                            $("#popup_box").fadeOut(300);
                            location.reload()
                        }
                        else {
                            $("#popup_box").html(data);
                        }
                    }
                );
            });
        });
        $("#popup_box").fadeIn(300);
        return false;
    });

    $(document).on('click', '.registration_show', function(){
        $("#popup_box").remove();
        $("body").append('<div id="popup_box" style="display:none"></div>');
        //$("#popup_box").css({"margin-top": "-160px"});
        $("#popup_box").load("/registration/");
        $("#popup_box").fadeIn(400);
        return false;
    });

    $(document).on('click', '#registration_button', function() {
        $.get("/registration/",
            {
                "csrftoken": getCookie("csrftoken"),
                "first_name": $("#first_name").val(),
                "email": $("#email").val(),
                "password": $("#password").val(),
                "password_again": $("#password_again").val()
            },
            function(data){
                alert(data);
                $("#popup_box").html(data);
            }
        );
    });


    $("#input-price").ionRangeSlider({
        type: "double",
        min: 0,
        max: 1500,
        from: 100,
        to: 1000
    });
    $("#input-size").ionRangeSlider({
        type: "double",
        min: 0,
        max: 1500,
        from: 100,
        to: 1000
    });
    $(".carousel").sliderkit({
        auto:false,
        shownavitems:4,
        circular:true
    });
    $('select').styler();


    $(".small-cart-img img").each(function(index, element){
        if ($(element).width() > $(element).height())
        {
            $(element).css({'width': 'auto', 'height': '100%'});
        }
    });



    /* ================  Корзина  ================ */

    $(document).on('click', '.add_product', function() {
        $.get("/cart/add_product/",
            {
                product_id: $(this).attr("data-id"),
                size: $('input[name=size]:checked').val(),
                count: $("#id_count").val(),
                color: $(".select_color_active .jq-selectbox__select-text").html()
            },
             function(msg){
                 alert(msg);
                 $('input[name=size]:checked').removeAttr("checked");
                 $("#id_count").val(1);
                 $("#top_count_cart").load("/cart/get_count_cart/");
            }
        );
        return false;
    });


    $(document).on('click', '.catalog_order_submit', function() {
        $.get("/cart/add_product/",
            {
                product_id: $(this).attr("data-id"),
                size: "",
                count: "1",
                color: ""
            },
             function(msg){
                 alert(msg);
                 $("#top_count_cart").load("/cart/get_count_cart/");
            }
        );
        return false;
    });

    $(document).on('click', '.change_count', function() {
        $.get("/cart/change_count_product/",
            {
                product_id: $(this).attr("data-id"),
                count: $(this).attr("data-count")
            },
            function(data) {
                $(".user_cart").html(data);
                $("#top_count_cart").load("/cart/get_count_cart/");
            }
        );
    });

    $(document).on('click', '.delivery_option input', function() {
        var price =  parseInt($(this).attr('data-sum'));
        var sum_cart = parseInt($("#cart_sum").attr('data-sum'));
        $("#delivery_sum").html(price);
        $("#all_sum").html(price + sum_cart);
    });


    $(document).on('click', '.small-cart-img img', function(){
        var link = $(this).attr('src');
        $(".cart-img img").attr('src', link);
    });





    $("#change_password").click(function(){
        var old_password = $("#id_old_password").val();
        var new_password = $("#id_new_password").val();

        $.get("/account/change_password/", {
            old_password: old_password,
            new_password: new_password
        },
        function(data){
            $("#id_old_password").val('');
            $("#id_new_password").val('');
            alert(data);
            if (data == "Ваш пароль изменён!") {
                location.reload()
            }
        });

        return false;
    });


    $(".cart-radiobt label").click(function(){
        var val = $(this).html();
        var select_color_active = $(".select_color_active");
        select_color_active.css('display', 'none');
        select_color_active.removeClass("select_color_active");

        $(".select_color_item").each(function(){
            if ($(this).attr('data-size') == val)
            {
                $(this).addClass("select_color_active");
                $(".select_color_active").css('display', 'inline-block');
            }
        });

        $(".jq-selectbox__dropdown").css('width', '152px');
        $(".jq-selectbox__dropdown ul").css('width', '152px');

    });


});