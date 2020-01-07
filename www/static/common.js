document.getElementById("previous").addEventListener("click", goBack);

function goBack() {
    history.go(-1);
}