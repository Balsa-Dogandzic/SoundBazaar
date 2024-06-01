function functionClick() {
  var full_name = document.getElementById("full_name").value;
  var email = document.getElementById("email").value;
  var message = document.getElementById("message").value;

  if (full_name === "" || email === "" || message === "") {
    alert("Molimo vas da popunite sva polja.");
  } else {
    alert("Poruka je poslata.");
  }
}