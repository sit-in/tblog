  function article_del() {
    var msg = "您真的确定要删除吗？\n\n请确认！";
    if (confirm(msg)===true){
      return true;
    }else{
      return false;
    }
  }

  $(function(){
    // 内容展示页面使用省略号
    $('.J-ellipsis').each(function(i){
      var len = 100;
      if ($(this).text().length > len){
        //$(this).attr("title", $(this).text());
        var text = $(this).text().substring(0, len-1) + "...";
        $(this).text(text);
      }
    });

  });
