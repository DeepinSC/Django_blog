//获取当前博客id
function get_id(url){
    var ele = url.split("/");
    var id = ele[ele.length-2];
    return id;
}

//获取当前博客数据
function get_data(){
        var return_value;
        var url = window.location.href;
        var id = get_id(url);
        $.ajax({
            async:false,
            url:"/api/blogs/"+id,
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

//展示博客详情
function get_blog_detail(){


    var blog_data = get_data();
    var blog_main_div = document.getElementById("blogs");
            var blog_post_div = document.createElement("div");
            blog_post_div.className = "blog-post";

            var title = document.createElement("a");
            var id = blog_data.id;
            title.className = "blog-post-title";
            title.href = "/blogs/"+id+"/";
            title.append(blog_data.title);

            var modify_time = document.createElement("p");
            modify_time.className = "blog-post-meta";
            modify_time.append(blog_data.modify_time);
            modify_time.append(" by: ");
            var owner = document.createElement("a");
            owner.append(blog_data.owner);
            modify_time.appendChild(owner);

            var content = document.createElement("div");
            content.append(blog_data.content);

            var category = document.createElement("p");
            category.className = "blog-post-meta";
            category.append(blog_data.category);

            var tag = document.createElement("p");
            tag.className = "blog-post-meta";
            tag.append(blog_data.tag);

            blog_post_div.appendChild(title);
            blog_post_div.appendChild(modify_time);
            blog_post_div.appendChild(content);
            blog_post_div.appendChild(category);
            blog_post_div.appendChild(tag);
            blog_post_div.appendChild(document.createElement("hr"));
            blog_main_div.appendChild(blog_post_div);
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


//删除博客
function delete_blog(){
    var return_value;
        var id = get_id();
        $.ajax({
            async:false,
            url:"/api/blogs/"+id+"/",
            type:"DELETE",
            datatype:"json",
            headers:{"X-CSRFToken":getCookie('csrftoken')},//这行重要！直接解决CSRF问题！
            success:function (data) {
             return_value = data;
             window.location.href='/blogs/';

         },
         error: function(XMLHttpRequest, textStatus, errorThrown) {
              console.log(textStatus.responseText);
              alert(XMLHttpRequest.status);
          }

      });
        return return_value;
}



//跳转至编辑页面
function to_edit(){
    return window.location.href+"edit";
}

//载入数据到编辑页面
function fill_editor(){
    var blog_data = get_data();
    // 添加数据到标签
    if (blog_data!=null) {
        document.getElementById("title").value = blog_data.title;
        document.getElementById("editor").append(blog_data.content);
        document.getElementById("category").value = blog_data.category;
        document.getElementById("tag").value = blog_data.tag;
    }
}

// 提交更改
function submit_blog(){
    var blog_id = get_id(window.location.href);

    var blog_title = document.getElementById("title").value;
    var blog_content = document.getElementById("editor").html();
    var blog_category = document.getElementById("category").value;
    var blog_tag = document.getElementById("tag").value;
    var submit_json = {title: blog_title, content:blog_content,category:blog_category,tag:blog_tag};
    $.ajax({
        url:"/api/blogs/"+blog_id+"/",
        type:"PUT",
        dataType:"json",
        async:false,
        data:submit_json,
        success: function(return_value){
                    alert(submit_json);
                },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
                    alert(XMLHttpRequest.status);
        }
    });

}