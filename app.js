let PORT = 5000;


let token = localStorage.getItem('token');

let userEl = document.querySelector('.login .user');
let msgListEl = document.querySelector('.mesages-list');

authButton.addEventListener('click', async () => {

    let res = await fetch(`http://localhost:${PORT}/auth`, {
        method: 'GET',  })
   

})

msgButton.addEventListener('click', async () => {

})