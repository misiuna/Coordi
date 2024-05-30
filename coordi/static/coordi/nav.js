// nav menu
function myFunction() {
  const x = document.querySelector(".navbar-nav");
  const flow = document.getElementById("header");
  const close = document.querySelector(".fa");
  if (x.style.display === "block") {
    x.style.display = "none";
    flow.style.display = "grid";
    close.classList = "fa fa-bars";
  } else {
    x.style.display = "block";
    flow.style.display = "block";
    close.classList = "fa fa-close";
  }
}
