document.addEventListener("DOMContentLoaded", function () {
  // toggle between views on GO Librry view
  document.querySelectorAll(".go-view-switch").forEach((view) => {
    view.onclick = function () {
      load_go_view(this.dataset.page);
    };
  });

  document.querySelectorAll(".pending").forEach((go) => {
    go.onclick = function () {
      alert(
        "Selected Graphic Organizer is still in developement. For demo purpouses try 'Two Column Chart'"
      );
    };
  });

  // default load view
  load_go_view("go-library-view");
});

//load view function
function load_go_view(view) {
  // make all views display none
  document.querySelectorAll(".view").forEach((element) => {
    element.style.display = "none";
  });
  // make each nav view no bottom border and font weight bold
  document.querySelectorAll("[data-page]").forEach((element) => {
    element.style.borderBottom = "none";
    element.style.fontWeight = "400";
  });

  navSwitch = document.querySelector(`[data-page=${view}]`);
  document.querySelector(`#${view}`).style.display = "block";
  navSwitch.style.borderBottom = "4px solid var(--color-top-nav)";
  navSwitch.style.fontWeight = "500";
}
