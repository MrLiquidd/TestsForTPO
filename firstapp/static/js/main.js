function main() {
    var Name = document.getElementById("Name").value;
    localStorage.setItem('Name',Name);
    var Sur = document.getElementById('Sur').value;
    localStorage.setItem('Sur',Sur);
}