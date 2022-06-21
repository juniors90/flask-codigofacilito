window.onload = function () {
  console.log("Hola");
  const divAlert = document.getElementById("custommsg");
  const msg = "Your email or password is invalid!.";
  const lista = `<ul class="list">
                    <li>${msg}</li>
                </ul>`;
  divAlert.innerHTML = lista;
  divAlert.style.display='block';
};
