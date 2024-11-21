let darkMode = localStorage.getItem('darkmode');
let themeSwitch = document.getElementById('themeswitch');

const enableDarkmode = () =>{
    document.body.classList.add("darkmode");
    localStorage.setItem('darkmode', 'active');
}
const disableDarkmode = () => {
    document.body.classList.remove("darkmode");
    localStorage.setItem('darkmode', null);
}
if(darkMode === 'active')enableDarkmode();



themeSwitch.addEventListener("click", ()=>{
    darkMode = localStorage.getItem('darkmode');
    darkMode !== "active" ? enableDarkmode() : disableDarkmode();
})