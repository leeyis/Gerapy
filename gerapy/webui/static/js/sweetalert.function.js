swal.setDefaults({
    html: true, showLoaderOnConfirm: true, confirmButtonColor: '#DE489A', closeOnConfirm: true
});

function swalert(text, type, func) {
    if (!type) {
        type = 'info';
    }
    switch (type) {
        case 'info':
            swal({title: '提示', text: text, timer: 1500});
            break;
        case 'success':
            swal({title: '成功', text: text, type: type, timer: 1500});
            break;
        case 'error':
            swal({title: '错误', text: text, type: type});
            break;
        case 'warning':
            swal({
                title: '警告',
                text: text,
                type: type,
                showCancelButton: true,
                confirmButtonColor: "#ec4758",
                confirmButtonText: "确认",
                cancelButtonText: "取消",
                closeOnConfirm: true
            }, func);
            break;
    }
}