; (function () {
    // dialog
    const modal = new bootstrap.Modal(document.getElementById('modal'))

    htmx.on('htmx:afterSwap', function (e) {
        if (e.detail.target.id == 'dialog') {
            modal.show()
        }
    })

    htmx.on('htmx:beforeSwap', function (e) {
        if (e.detail.target.id == 'dialog' && !e.detail.xhr.response) {
            modal.hide()
            // e.detail.shouldSwap = false
        }
    })
    htmx.on('hidden.bs.modal', function (e) {
        document.getElementById('dialog').innerHTML = ""
    })
})()