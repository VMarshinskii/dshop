function getCookie(name) {
  var matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

$(document).ready(function(){

    if($("input").is("#id_size"))
    {
        $('#id_size').selectize({
            delimiter: ',',
            create: function(input) {
                return {
                    value: input,
                    text: input
                }
            }
        });
    }

    if($("select").is("#id_related_products"))
    {
        $('#id_related_products').selectize({
            delimiter: ','
        });
    }

    if($("select").is("#id_color"))
    {
        $('#id_color').selectize({
            delimiter: ','
        });
    }

    if($("select").is("#id_parent"))
    {
        var val = $("#id_parent").val();
        $("#id_parent").load("/admin/tree_categories/" + val + "/", function(){
            $("#id_parent").val(val);
        });
    }

    if($("select").is("#id_category"))
    {
        var val = $("#id_category").val();
        $("#id_category").load("/admin/tree_categories/" + val + "/", function(){
            $("#id_category").val(val);
        });
    }


    if($("textarea").is("#id_images")) {
        $("#id_images").hide();

        //$(".field-images").hide();

        if ($("div").is(".field-image")) {
            $(".field-image").hide();
        }

        var html = '<div class="adminBoxImg adminBoxImgLast"></div>';
        $("#id_images").after(html);

        var images = $("#id_images").val().split(";");
        for (var i = 0; i < images.length; i++) {
            var image = $("#id_image").val();
            var id_active = "";
            if (image == images[i]) {
                id_active = "hidden_image_active";
            }

            if (images[i] != "") {
                var html = '<div class="adminBoxImg">\
                                <img src="/static/uploads/' + images[i] + '" alt="">\
                                <div class="adminBoxSettingsImages">\
                                    <img class="adminBoxImgClose" src="/static/images/close_icon.png" data-image="' + images[i] + '" alt="Удалить">\
                                    <img class="adminBoxImgHead" src="/static/images/icon_writing.png" data-image="' + images[i] + '" id=' + id_active + ' alt="Главная">\
                                </div>\
                            </div>\
                            ';
                $(".adminBoxImgLast").before(html);
            }

        }

        var myDropzone = new Dropzone(".adminBoxImgLast",
            {
                url: "/admin/upload_image/",
                sending: function (file, xhr, formData) {
                    formData.append("csrfmiddlewaretoken", getCookie("csrftoken"));
                },
                success: function (file, response) {
                    var html = '<div class="adminBoxImg">\
                                <img src="/static/uploads/' + response + '" alt="">\
                                <div class="adminBoxSettingsImages">\
                                    <img class="adminBoxImgClose" src="/static/images/close_icon.png" data-image="' + response + '" alt="Удалить">\
                                    <img class="adminBoxImgHead" src="/static/images/icon_writing.png" data-image="' + response + '" alt="Главная">\
                                </div>\
                            </div>\
                            ';
                    $(".adminBoxImgLast").before(html);

                    var images = $("#id_images").val();
                    $("#id_images").val(images + ";" + response);

                    var image = $("#id_image").val();
                    if (image == "") {
                        $("#id_image").val(response);
                        $(".adminBoxImgHead").first().attr('id', 'hidden_image_active');
                    }
                }
            });
    }





    if($(".file-upload").is())
    {
        var path = $(".file-upload").children("a").attr("href");
        $(".file-upload").children("a").attr("href", '/' + path);
        $(".file-upload").children("a").html('<img width="260px" class="adminImageField" src="/' + path + '"/>');
        var content = $(".file-upload").html().replace("На данный момент: ", '');
        $(".file-upload").html(content);
    }


    $(document).on('click', '.adminBoxImgHead', function(){
        $("#hidden_image_active").attr('id', '');
        $(this).attr('id', 'hidden_image_active');
        var image = $(this).attr("data-image");
        $("#id_image").val(image);
    });

    $(document).on('click', '.adminBoxImgClose', function(){
        var image = $(this).attr("data-image");
        var images = $("#id_images").val().replace(";" + image, "");
        $("#id_images").val(images);
        $(this).parents(".adminBoxImg").remove();

        var image_one = $("#id_image").val();

        if (image == image_one)
        {
            var img = $(".adminBoxImgHead").first().attr('data-image');
            $("#id_image").val(img);
            $(".adminBoxImgHead").first().attr('id', 'hidden_image_active');
        }

    });


    if($("div").is(".field-colors")) {

        var id_size_colors = $("#id_size_color").val().split(";");
        var sizes = {};

        for (var j = 0; j < id_size_colors.length; j++)
        {
            var st = id_size_colors[j].split(":");
            sizes[st[0]] = st[1];
        }

        $(".field-sizes .item").each(function(){
            var key = $(this).attr('data-value');
            if (key in sizes)
            {
                $(this).attr('data-colors', sizes[key]);
            }
            else
            {
                $(this).attr('data-colors', '-1');
            }
        });


        $(".field-colors").find(".controls").html('');

        $(document).on('click', ".field-sizes .item", function () {
            $("#size_select").removeAttr('id');
            $(this).attr('id', 'size_select');

            var SelectSize = $(this);

            var Controls = $(".field-colors").find(".controls");
            Controls.hide(100);
            Controls.html('<div class="related-widget-wrapper" id="ajax_size_colors"></div>');
            $("#ajax_size_colors").load("/admin/size_colors/" + SelectSize.attr('data-colors') + "/", function(){
                $("#id_ajax_size_colors").selectize({
                    delimiter: ',',
                    onItemAdd: function(value, $item){
                        var select_size_colors = SelectSize.attr('data-colors');
                        if (select_size_colors == -1 || select_size_colors === undefined) {
                            SelectSize.attr('data-colors',',' + value);
                        } else {
                            SelectSize.attr('data-colors', select_size_colors + ',' + value);
                        }

                        $("#id_size_colors").val('');
                        $(".field-sizes .item").each(function(){
                             var id_size_colors = $("#id_size_colors").val();
                            $("#id_size_colors").val(id_size_colors + ";" + $(this).attr('data-value') + ":" + $(this).attr('data-colors'));
                        });
                    }
                });
                Controls.show(200);
            });
        });

    }

    if ($("div").is(""))
    {
        var path = $(".file-upload").children("a").attr("href");
        if(path){
            $(".file-upload").children("a").attr("href", '/' + path);
            $(".file-upload").children("a").html('<img width="260px" class="adminImageField" src="/' + path + '"/>');
            var content = $(".file-upload").html().replace("На данный момент: ", '');
            $(".file-upload").html(content);
        }
    }


});