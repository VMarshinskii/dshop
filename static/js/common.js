/**
 * Created by Vladislav on 06.01.2015.
 */

function resize() {
    /*if($(document).width() > 1700) {
        $("#all-content").css({"width":"1600px"});
        $(".header-info .header-info-one").css({"width":"585px"});
    }*/
    if($(document).width() > 1340) {
        $("#all-content").css({"width":"1285px"});
        $(".all-content").css({"width":"1285px"});
        $(".header-info .header-info-one").css({"width":"585px"});
        $("#center-block").css({"width":"700px"});
        $(".main-slider img").css({"width":"683px"});
        $(".main-slider").css({"height":"auto"});
        $(".photoslider-bullets").css({"height":"443px"});

        resize_goods(3, 192);
    }
    else {
        $("#all-content").css({"width": "1000px"});
        $(".all-content").css({"width": "1000px"});
        $(".header-info .header-info-one").css({"width":"400px"});
        $("#center-block").css({"width":"395px"});
        $(".main-slider img").css({"width":"375px"});
        $(".main-slider").css({"height":"244px"});
        $(".photoslider-bullets").css({"height":"244px"});

        resize_goods(2 ,159);
    }
}
function resize_goods(number, width) {
    //number -= ;
    var index = 1;

    $(".goodss .good").removeClass("mar0");
    $(".goodss .good").width(width);

    $(".goodss .good").each(function () {
        if(index%number == 0) {
            $(this).addClass("mar0");
        }
        index++;
    });

    //width: 192px;
    /*width: 159px;*/
}

$(document).ready(function (){
    resize();
});
$(window).resize(function(){
    resize();
});
jQuery(window).load(function(){
    jQuery(".photoslider-bullets").sliderkit({
        auto:true,
        circular:true,
        mousewheel:false,
        shownavitems:5,
        panelfx:"sliding",
        panelfxspeed:2000,
        panelfxeasing:"easeOutExpo" // "easeOutExpo", "easeInOutExpo", etc.
    });
});

$(".CartAdd").live('click', function(){
    var id = $(this).attr("data-id");

    $.get("/cart/change_count_product/",
        {
            product_id: id,
            cart_count: 1
        },
        function(data){
            $(".ContentBoxPage").html(data);
            $(".cart a").load("/cart/cart_top_ajax/");
        }
    );
});

$(".CartDelete").live('click', function(){
    var id = $(this).attr("data-id");

    $.get("/cart/change_count_product/",
        {
            product_id: id,
            cart_count: -1
        },
        function(data){
            $(".ContentBoxPage").html(data);
            $(".cart a").load("/cart/cart_top_ajax/");
        }
    );
});

$(".CartItemDelete").live('click', function(){
    var id = $(this).attr("data-id");

    $.get("/cart/change_count_product/",
        {
            product_id: id,
            cart_count: -1000
        },
        function(data){
            $(".ContentBoxPage").html(data);
            $(".cart a").load("/cart/cart_top_ajax/");
        }
    );
});

$(document).ready(function (){
    $(".contact-info .button").click(function(){
        $.get("/orders/create_order_phone/",
            function(data){
            $(".popupBox").html(data);
            $(".background").css('display', 'block');
            $(".popupBox").css('display', 'block');
        });
        return false;
    });

    $(document).on('click', '#orderPhoneButton', function(){
        var name = $("#orderPhoneName").val();
        var number = $("#orderPhoneNumber").val();

        $.get("/orders/create_order_phone/",
            {
                name: name,
                number: number
            },
            function(data){
                $(".popupBox").html(data);
            }
        );
    });

    $(".good-c a").click(function(){
        var id = $(this).attr("data-id");
        $.get("/cart/add_in_cart/",
            {
                product_id: id,
                cart_size: '',
                cart_count: 1,
                cart_color: ''
            },
            function(data){
                $(".popupBox").html(data);
                $(".background").css('display', 'block');
                $(".popupBox").css('display', 'block');
                $(".cart a").load("/cart/cart_top_ajax/");
            }
        );
        return false;
    });

    $(".sizes_list li").click(function(){
        $(".sizes_list_active").removeClass("sizes_list_active");
        $(this).addClass("sizes_list_active");
    });

    $(".CatalogPriceBox a").click(function(){
        var id = $(this).attr("data-id");
        $.get("/cart/add_in_cart/",
            {
                product_id: id,
                cart_size: $(".sizes_list_active").attr('data-size'),
                cart_count: 1,
                cart_color: $(".product_colors").val()
            },
            function(data){
                $(".popupBox").html(data);
                $(".background").css('display', 'block');
                $(".popupBox").css('display', 'block');
                $(".cart a").load("/cart/cart_top_ajax/");
            }
        );
        return false;
    });

    $(".cart a").load("/cart/cart_top_ajax/");
//    $(".OrderBoxAddressAdd").hide();

    $(".popupBoxLoginFormClose").live('click', function(){
        $(".background").css('display', 'none');
        $(".popupBox").css('display', 'none');
    });

    $(".popup_img_box_close").live('click', function(){
        $(".background").css('display', 'none');
        $(".popupBox").css('display', 'none');
    });

    $(".reg_client #id_register").click(function(){
        $(".OrderBoxPassword").fadeIn(200);
    });

    if ($("a").is(".product_image"))
    {
        $('.product_image:not(".slick-cloned")').fancybox({
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

        $(".galeryBoxImg").click(function(){
            $(".prev_head").click();
        });

    }

    $('.background').hover(
        function(){
            $(".popup_img_box_close").css('opacity', '1');
        },
        function(){
            $(".popup_img_box_close").css('opacity', '0.3');
        }
    );

    $(".background").click(function(){
        $(".background").css('display', 'none');
        $(".popupBox").attr("style", "display: none");
        $(".popupBox").html("");
    });

    $(".login_order").live('click', function(){
        $.get("/login/", function(data){
            $(".popupBox").html(data);
            $(".background").css('display', 'block');
            $(".popupBox").css('display', 'block');
            $("#id_login").mask("+7 (999) 999-9999");
        });
        return false;
    });

    $(".loginSubmit").live('click', function(){
        var link = $(".login_order").attr("data-link");
        $.post("/login/",
            {
                login: $("#id_login").val(),
                password: $("#id_password").val(),
                csrfmiddlewaretoken: $(".popupBox input[name='csrfmiddlewaretoken']").val()
            },
            function(data){
                if(data == "true")
                {
                    if(link == undefined)
                    {
                        window.location.replace("http://85.143.216.11/user/orders/");
                        window.location.href = "http://85.143.216.11/user/orders/";
                    }
                    else
                    {
                        window.location.replace(link);
                        window.location.href = link;
                    }
                }
        });
        return false;
    });

    $("#id_phone").mask("+7 (999) 999-9999");
    $("#id_login").mask("+7 (999) 999-9999");

    $("#id_type_delivery").live('click', function(){
        var price = $(this).attr('data-price');
        $("#OrderBoxConfirmationPriceCurrent span").html(price);
        var price_all = parseInt($("#OrderBoxConfirmationPriceSum span").html(), 10) + parseInt(price, 10);
        $("#OrderBoxConfirmationPriceAll span").html(price_all);
    });


    $(".video_file").each(function(indx, element){
        $(element).append("<span></span>");
        var left = $(element).children("img").position().left + (($(element).children("img").width() - 64) / 2);
        var top = $(element).children("img").position().top + (($(element).children("img").height() - 64) / 2);
        $(element).children("span").css({'top': top, 'left': left});
    });

    $(".video_file").click(function(){
        var url = 'http://85.143.216.11' + $(this).attr("href");
        var str = '<div class="player" id="videoplayer"></div><script type="text/javascript">this.player = new Uppod({m:"video",uid:"videoplayer",file:"'+ url +'",poster:"'+ url +'"});</script>'
        $(".popupBox").html(str);
        $(".background").css('display', 'block');
        $(".popupBox").css('display', 'block');
        $(".popupBox").css({'width':'500px', 'height': '375px', 'margin-left': '-250px', 'margin-top': '-171px', 'padding': '0'});
        return false;
    });


    $(".goods-img img").each(function(index, element){
        $(this).load(function(){
            if ($(element).width() > $(element).height())
            {
                $(element).css({'width': 'auto', 'height': '100%'});
            }
        });
    });


    $(document).on('click', '.delivery_mail_button', function(){
        alert("ok");
        var first_name = $("#id_first_name").val();
        var email = $("#id_email").val();

        $.get("/account/fun_add_view/",
            {
                first_name: first_name,
                email: email
            },
            function(data) {
                alert(data)
            }
        );
    });

});