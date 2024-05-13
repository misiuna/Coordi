const table = document.querySelector("#twoCol");

/* Edit / Save Button */
table.addEventListener("click", (e) => {
  if (e.target.tagName === "BUTTON") {
    const button = e.target;
    const thCell = button.parentNode;
    let thCellId = thCell.getAttribute("id");
    console.log(thCellId);
    let thCellData = thCell.getAttribute("data-number");
    console.log(thCellData);
    if (button.textContent === `edit title ${thCellData}`) {
      const title = thCell.firstElementChild;
      /* create input */
      const input = document.createElement("input");
      input.type = "text";
      input.placeholder = title.textContent;
      /* insert input */
      thCell.insertBefore(input, title);
      thCell.removeChild(title);

      button.textContent = "save";
      button.style.background = "var(--color-top-nav)";
      button.style.color = "white";
    } else {
      input = thCell.firstElementChild;
      title = document.createElement("p");
      if (input.value === "") {
        alert("Title can not be blank");
        return;
      }
      title.textContent = input.value;

      title.setAttribute("id", thCellId);
      thCell.insertBefore(title, input);
      thCell.removeChild(input);
      button.textContent = `edit title ${thCellData}`;
      button.style.background = "white";
      button.style.color = "black";
    }
  }
});

/* adding rows */
const addBtn = document.querySelector("#add-row");
function addRow() {
  // Insert a row at the end of the table
  const rowCount = table.rows.length;
  table.insertRow(-1).innerHTML = `
        <tr>
            <td>
                <textarea name="answer" placeholder="Enter your respose ${rowCount} for column 1"></textarea>
            </td> 
            <td>
                <textarea name="answer" placeholder="Enter your respose ${rowCount} for column 2"></textarea>
            </td>
        </tr>
    `;
}
if (addBtn) {
  addBtn.addEventListener("click", function () {
    addRow();
  });
}

/* deleting rows */
const deleteBtn = document.querySelector("#delete-row");
function removeBtn() {
  const lastRow = table.rows[table.rows.length - 1];
  lastRow.remove();
}
if (deleteBtn) {
  deleteBtn.addEventListener("click", function () {
    removeBtn();
  });
}

/* finalize table */
const finalizeBtn = document.querySelector("#finalize-table");
function finalizeTable() {
  const editBtns = document.querySelectorAll(".btn-edit");
  const instructionText = document.querySelector(".go-content-wrapper p");
  editBtns.forEach((btn) => {
    if (btn.innerHTML === "save") {
      alert("Save your title name.");
      return;
    }
    btn.remove();
  });
  instructionText.innerHTML =
    "Now let save name your new GO and save it to your Custom Graphic Organizers Library, you can Assign it to your students from there.";

  instructionText.classList.remove("mb0");
  instructionText.style.borderBottom = "1px solid black";
  instructionText.style.paddingBottom = "20px";

  let instDelete = document.querySelector(".inst-delete");
  instDelete.remove();
  let instructionWrapper = document.querySelector(".instruction-btn-wrapper");
  let instructionInput = document.querySelector("#instruction");
  let instructionP = document.createElement("p");
  instructionP.setAttribute("id", "instruction");
  instructionWrapper.insertBefore(instructionP, instructionInput);
  instructionP.innerHTML = instructionInput.value;

  instructionInput.remove();

  const actionBtns = document.querySelectorAll(".btn-action");
  const btnFirst = actionBtns.firstChild;

  const saveInput = document.createElement("input");
  saveInput.className = "save-input";
  saveInput.placeholder = "Name for your custom GO";

  const saveBtn = document.createElement("button");
  saveBtn.className = "btn btn-assign btn-assign-seconraty btn-saveAs";
  saveBtn.innerHTML = "Save";

  const div = document.createElement("div");
  div.className = "saveAs-btn-wrapper";

  //const assignBtn = document.createElement("button");
  //assignBtn.className = "btn btn-assign btn-assign-primary";
  //assignBtn.innerHTML = "Assign";
  const actionButtonsWrapper = document.querySelector(".action-btns");

  actionButtonsWrapper.insertBefore(div, btnFirst);
  div.appendChild(saveInput);
  div.appendChild(saveBtn);
  console.log(saveBtn);
  saveBtn.onclick = function () {
    saveAs();
  };
  //actionButtonsWrapper.insertBefore(assignBtn, btnFirst);

  actionBtns.forEach((btn) => {
    btn.remove();
  });
}
if (finalizeBtn) {
  finalizeBtn.addEventListener("click", function () {
    finalizeTable();
  });
}

/* "save as" btn for custom GO */
function saveAs() {
  let type = table.getAttribute("id");
  let nameSave = document.querySelector(".save-input").value;
  let instruction = document.querySelector("#instruction").innerText;
  const instructionText = document.querySelector(".go-content-wrapper p");
  instructionText.remove();
  let numRows = table.rows.length - 1;
  let col1Title = document.querySelector("#col1-title").innerText;
  let col2Title = document.querySelector("#col2-title").innerText;

  fetch("/save_custom_go", {
    method: "POST",
    body: JSON.stringify({
      type: type,
      nameSave: nameSave,
      instruction: instruction,
      numRows: numRows,
      col1Title: col1Title,
      col2Title: col2Title,
    }),
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getToken("csrftoken"),
    },
  }).then(async (response) => {
    console.log(response);
  });

  let wrapperSaving = document.querySelector(".saveAs-btn-wrapper");
  wrapperSaving.style.margin = "auto 0px";
  wrapperSaving.style.width = "fit-content";
  let success = document.createElement("div");
  success.innerHTML =
    '<p class="success"><i class="fa-regular fa-circle-check"></i>saved succesfully!</p>';
  let input = document.querySelector(".save-input");
  let saveAsBtn = document.querySelector(".btn-saveAs");
  wrapperSaving.insertBefore(success, input);
  input.remove();
  saveAsBtn.remove();
}

/* "submit" btn for student */
let submitBtn = document.querySelector("#student-submit");
function submitAssignment() {
  let rowCount = table.rows.length;
  let colCount = 2;
  let go_id = table.getAttribute("class");
  let arr = [];
  for (let i = 0; i < rowCount - 1; i++) {
    for (let j = 1; j < colCount; j++) {
      //console.log(`.answer${i}`);
      //console.log(`.answer${i}${j}`);

      let answer1 = document.querySelector(`.answer${i}`).value;
      let answer2 = document.querySelector(`.answer${i}1`).value;
      //let answer01 = document.querySelector(`.answer${j}1`).value;
      //console.log(`${answer1}`, `${answer2}`);
      arr.push(`${answer1}`);
      arr.push(`${answer2}`);
    }
  }
  console.log(arr[0]);

  /*   let answer1 = document.querySelector(".answer0").value;
  let answer2 = document.querySelector(".answer01").value;
  let answer3 = document.querySelector(".answer1").value;
  let answer4 = document.querySelector(".answer11").value;
  let answer5 = document.querySelector(".answer2").value;
  let answer6 = document.querySelector(".answer21").value;
  let answer7 = document.querySelector(".answer3").value;
  let answer8 = document.querySelector(".answer31").value; */

  fetch("/submit_student", {
    method: "POST",
    body: JSON.stringify({
      go_id: go_id,
      answer1: arr[0],
      answer2: arr[1],
      answer3: arr[2],
      answer4: arr[3],
      answer5: arr[4],
      answer6: arr[5],
      answer7: arr[6],
      answer8: arr[7],
    }),
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getToken("csrftoken"),
    },
  }).then(async (response) => console.log(response));

  let success = document.createElement("div");
  success.innerHTML =
    '<p class="success"><i class="fa-regular fa-circle-check"></i>submission was succesfull!</p>';
  const mainDiv = document.querySelector(".go-content-wrapper");
  const instructionText = document.querySelector(".go-content-wrapper p");
  mainDiv.insertBefore(success, instructionText);
  instructionText.remove();
  table.remove();
  submitBtn.remove();
}

submitBtn.addEventListener("click", function () {
  submitAssignment();
});

// get token function
function getToken(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie != "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
