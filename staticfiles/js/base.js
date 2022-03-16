const dateInput = document.querySelector("#date");
const dateForm = document.querySelector("#date-form");

const urlParts = window.location.pathname.split("/");
const possibleDate = urlParts.pop() || urlParts.pop();

if (possibleDate.match(/^\d{4}-\d{2}-\d{2}$/)) {
  dateInput.value = possibleDate;
}

dateForm.onsubmit = function (e) {
  e.preventDefault();
  const date = dateInput.value;
  window.location.href = `/date/${date}`;
};

/**
 * @param {String} html representing a single element
 * @return {ChildNode}
 */
const htmlToElement = function (html) {
  const template = document.createElement("template");
  html = html.trim();
  template.innerHTML = html;
  return template.content.firstChild;
}

/**
 * @param {String} id of the modal
 * @param {String} title of the modal header
 * @param {String} action link to be passed in form action
 * @param {String} currentPath used to return to the current page
 * @param {String} btnClass used for confirmation button styling
 * @return {String}
 */
const createModalTemplate = function (id, title, action, currentPath, btnClass) {
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  return `
<div class="modal fade" id="${id}" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">${title}</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        this action cannot be undone
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">cancel</button>
        <form method="post" action="${action}">
          <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
          <input type="hidden" name="next" value="${currentPath}">
          <button type="submit" class="btn btn-outline-${btnClass}">confirm</button>
        </form>
      </div>
    </div>
  </div>
</div>`;
}
