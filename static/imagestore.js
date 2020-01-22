const getCaretPosition = (jObject) => {
    const obj = jObject.get(0);
    obj.focus();

    if (document.selection) {
        const sel = document.selection.createRange();
        const clone = sel.duplicate();
        sel.collapse(true);
        clone.moveToElementText(obj);
        clone.setEndPoint("EndToEnd", sel);
        return clone.text.length;
    } else if (obj.selectionStart !== false) {
        return obj.selectionStart;
    } else {
        return 0;
    };
}

const getImageList = (url) => {
    $.getJSON(url, (data) => {
        const images = $("#imagestore_image_list td.image");
        images.empty();
        for (let i = 0; i < data.images.length; i++) {
            $(images.get(i)).append(`<a class="insert" href='${data.images[i].src}'>
            <img src='${data.images[i].src}' width="150" height="150"/></a><br><a href='${data.images[i].delete_src}'>Delete</a>`);
        }

        const link1 = $('#imagestore_prev');
        if (data.prev_url == "") {
            link1.addClass("disabled");
            link1.attr("href", "#");
        } else {
            link1.removeClass("disabled");
            link1.attr("href", data.prev_url);
        }

        const link2 = $('#imagestore_next');
        if (data.prev_url == "") {
            link2.addClass("disabled");
            link2.attr("href", "#");
        } else {
            link2.removeClass("disabled");
            link2.attr("href", data.next_url);
        }
    })
}

$(()=> {
    const contentField = $("form textarea[name=content]");
    $("#imagestore_prev", "#imagestore_next").click((evt)=> {
        evt.preventDefault();
        getImageList($(this).attr("href"));
    });
    $("#imagestore_output").on("load", ()=> {
        getImageList($('#imagestore_image_list').attr("href"));
    });
    /*$("#imagestore_image_list").on("click", "td.image a.insert",
    (evt)=> {
        evt.preventDefault();
        let content = contentField.val();
        const position = getCaretPosition(contentField);
        content = content.substring(0, position) + `
        <img href="${$(this).attr("href")}"/>` + content.substring(position);
        contentField.val(content);
    });*/
    $("#imagestore_image_list").on("click", "td.image a.delete", (evt)=> {
        evt.preventDefault();
        if (window.confirm("Delete image?")) {
            $.getJSON($(this).attr("href"), (data)=>{
                getImageList($("#imagestore_image_list").attr("href"));
            });
        }
    });
    getImageList($("#imagestore_image_list").attr("href"));
});