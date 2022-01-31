// get all the stars
const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')

// get the form, confirm-box and csrf token
const form = document.querySelector('.rate-form')
const confirmBox = document.getElementById('confirm-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const handleStarSelect = (size) => {
    const children = form.children
    
    for(let i=0; i< children.length; i++){
        if(i <= size){
            children[i].classList.add('checked')
        }else{
            children[i].classList.remove('checked')
        }
    }
}

const handleSelect = (selection) => {
    switch(selection){
        case 'first': {
            handleStarSelect(1)
            return
        }
        case 'second': {
            handleStarSelect(2)
            return
        }
        case 'third': {
            handleStarSelect(3)
            return
        }
        case 'fourth': {
            handleStarSelect(4)
            return
        }
        case 'fifth': {
            handleStarSelect(5)
            return
        }
        default: {
            handleStarSelect(0)
        }
    }
}

const getNumericValue = (stringValue) => {
    let numericValue;
    if(stringValue == 'first'){
        numericValue = 1
    }
    else if(stringValue == 'second'){
        numericValue = 2
    }
    else if(stringValue == 'third'){
        numericValue = 3
    }
    else if(stringValue == 'fourth'){
        numericValue = 4
    }
    else if(stringValue == 'fifth'){
        numericValue = 5
    }
    else{
        numericValue = 0
    }
    return numericValue
}

if(one){
    const arr = [one, two, three, four, five]

    arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
        handleSelect(event.target.id)
    }))

    arr.forEach(item=> item.addEventListener('click', (event)=>{
        const val = event.target.id

        let isSubmit = false
        form.addEventListener('submit', e=>{
            e.preventDefault()
            if(isSubmit){
                return
            }
            isSubmit = true
            // Picture Id
            const image_id = e.target.id
            const val_num = getNumericValue(val)

            $.ajax({
                type: 'POST',
                url: '/image-rate/',
                data: {
                    'csrfmiddlewaretoken': csrf[0].value,
                    'el_id': image_id,
                    'rate': val_num
                },
                success: function(response){
                    console.log(response)
                    confirmBox.innerHTML = `<h1>Successfully rated with ${response.score}</h1>`
                },
                error: function(error){
                    console.log(response)
                    confirmBox.innerHTML = `<h1>Opps... Something went wrong</h1>`
                }
            })
        })
    }))
}

$('.like-form').submit(function(e){
    e.preventDefault()

    const image_id = $(this).attr('id')

    const likeText = $(`.like-btn${image_id}`).text()
    const trimLikeText = $.trim(likeText)
    
    const url = $(this).attr('action')

    $.ajax({
        type: 'POST',
        url: url,
        data: {
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            'post_id': image_id,
            'value': trimLikeText,
        },
        success: function(response) {
            if(trimLikeText === 'Unlike'){
                $(`.like-btn${image_id}`).text('Like')
            }else{
                $(`.like-btn${image_id}`).text('Unlike')
            }
        },
        error: function(response){
            console.log('error', response)
        }
    })
})
