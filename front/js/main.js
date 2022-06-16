async function activate_script() {
    let btn = document.getElementById('activate').checked;
    await eel.activate(btn);
}
document.getElementById('activate').onclick = activate_script;

async function get_key() {
    var inputElements = document.getElementById('id1').value;
    await eel.get_key(inputElements);
}
document.getElementById('setting-btn').onclick = get_key;