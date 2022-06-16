async function activate_script() {
    let btn = document.getElementById('activate').checked;
    await eel.activate(btn);
}
document.getElementById('activate').onclick = activate_script;

async function get_key() {
    let inputElements = document.getElementsByClassName('form-control');
    var lst = [];
    for(var i=0; inputElements[i]; ++i){
        lst.push(inputElements[i].value)
    }
    await eel.get_key(lst);
}
document.getElementById('index-btn').onclick = get_key;