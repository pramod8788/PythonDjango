let form = document.getElementById("info-form")
let info = document.querySelector("input#id_info")
let desc = document.getElementById('id_desc')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

let box = document.getElementById("box")

form.addEventListener('submit', e=>{
    e.preventDefault()

    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('info', info.value)
    fd.append('desc', desc.value)

    $.ajax({
        type: 'POST',
        url: '/create-info/',
        data: fd,
        success: function(response){
            if(response.status == "True"){
                CreateInfo.innerHTML = ""
                spinner.classList.remove("not-visble")
                setTimeout(()=>{
                    spinner.classList.add("not-visble")
                    
                    box.innerHTML = redata.forEach(element => {
                        
                    });
                }, 500)
            }
        },
        error: function(error){
            console.log(error)
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})
