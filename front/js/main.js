async function activate_script() {
    let btn = document.getElementById('activate').checked;
    await eel.activate(btn);
}
document.getElementById('activate').onclick = activate_script;

async function set_key() {
    let inputElements = document.getElementsByClassName('form-control');
    var lst = [];
    for(var i=0; inputElements[i]; ++i){
        lst.push(inputElements[i].value)
    }
    await eel.set_key(lst);
}
document.getElementById('index-btn').onclick = set_key;

async function get_key() {
    let inputElements = document.getElementsByClassName('form-control');
    for(var i=0; inputElements[i]; ++i){
        inputElements[i].value = await eel.get_key(inputElements[i].id)();
    }
}
document.body.onload = get_key;