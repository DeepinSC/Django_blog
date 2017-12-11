    function get_data(){
            var return_value;
            $.ajax({
                async:false,
                url:"/api/blogs/",
                type:"GET",
                datatype:"json",
                success:function (data) {
                 return_value = data;

             },
             error: function(XMLHttpRequest, textStatus, errorThrown) {
                  console.log(textStatus.responseText);
                  alert(XMLHttpRequest.status);
              }

          });
            return return_value;
}

function get_blog_list(){

    var blog_data = get_data();
    var blog_main_div = document.getElementById("blogs");
        for(var i=0;i<blog_data.length;i++){
            var blog_post_div = document.createElement("div");
            blog_post_div.className = "blog-post";

            var title = document.createElement("a");
            var id = blog_data[i].id;
            title.className = "blog-post-title";
            title.href = "/blogs/"+id+"/";
            title.append(blog_data[i].title);

            var modify_time = document.createElement("p");
            modify_time.className = "blog-post-meta";
            modify_time.append(time_tostring(blog_data[i].modify_time));
            modify_time.append(" by: ");
            var owner = document.createElement("a");
            owner.append(blog_data[i].owner);
            modify_time.appendChild(owner);

            var abstract = document.createElement("p");
            $(abstract).text(removeHTMLTag(blog_data[i].content).substring(0,250)+"...");


            var category = document.createElement("p");
            category.className = "blog-post-meta";
            category.append("Category: "+blog_data[i].category);

            var tag = document.createElement("p");
            tag.className = "blog-post-meta";
            tag.append("Tag: "+blog_data[i].tag);

            blog_post_div.appendChild(title);
            blog_post_div.appendChild(modify_time);
            blog_post_div.appendChild(abstract);
            blog_post_div.appendChild(category);
            blog_post_div.appendChild(tag);
            blog_post_div.appendChild(document.createElement("hr"));
            blog_main_div.appendChild(blog_post_div);
        }
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '')
    {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++)
        {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '='))
            {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function removeHTMLTag(str) {
            str = str.replace(/<\/?[^>]*>/g,''); //去除HTML tag
            str = str.replace(/[ | ]*\n/g,'\n'); //去除行尾空白
            str = str.replace(/&[^;]*;/g,''); //去除&开头；结尾的html格式标签
            return str;
    }

function time_tostring(str){
    var date = str.split("T")[0];
    var time = str.split("T")[1].split(".")[0];
    return date + " " + time;
}