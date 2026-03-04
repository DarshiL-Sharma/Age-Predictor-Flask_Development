/* particles generator */

const container = document.getElementById("particles")

for(let i=0;i<40;i++){

let p = document.createElement("span")

p.style.left = Math.random()*100+"vw"
p.style.top = Math.random()*100+"vh"
p.style.animationDuration = 8 + Math.random()*10 + "s"

container.appendChild(p)

}

/* form redirect */

const form = document.getElementById("nameForm")

form.addEventListener("submit",(e)=>{

e.preventDefault()

let name = document.getElementById("nameInput").value

window.location.href = "/name/" + name

})