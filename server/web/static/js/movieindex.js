$(document).ready(function(){
        $("#guess_btn").click(function(){
                location.reload();
        });
});
/*
$(document).ready(function(){
        var cursor=0;
        function getCookie(name){
                var c=document.cookie.match("\\b"+name+"=([^;]*)\\b");
                return c?c[1]:undefined;
        };
        /*Guess button reaction*//*
        $("#guess_btn").click(function(){
                cursor+=1;
                $.ajax({
                url:'/movieindex',
                type:'post',
                datatype:'json',
                data:jQuery.param({'cursor':cursor,'_xsrf':getCookie('_xsrf')}),
                success:function(data){
                        var movies=$.parseJSON(data)['rec'];
                        $('#movies .movie_block').each(function(i){
                                $(this).find('.movie_picture').html("<a href='/movie?mid="+movies[i].id+"'><img class='img-rounded movie_img' src='"+movies[i]['posters']['original']+"'/></a>");
                                $(this).find('.movie_info').find('.movie_title').html("<a href='/movie?mid="+movies[i].id+"'><strong class='title'>"+movies[i].title+"</strong></a>");
                                $(this).find('.movie_info').find('.movie_synposis').html("<span>Synopsis:"+movies[i].synposis+"</span>");
                                $(this).find('.movie_info').find('.movie_genre').html(movies[i].gener);
                        });
                },
                error: function (data, textStatus, jqXHR) { 
                        alert(data.responseText);
                },
        });
        });

});
*/